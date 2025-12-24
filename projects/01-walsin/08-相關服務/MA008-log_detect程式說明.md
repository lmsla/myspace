# MA008 - log-detect 程式說明

***
程式位置(ES - 10.190.253.46)：/home/disney/log-detect<br>
相關程式(備份於主目錄**05-程式備份**資料夾中)：<br>
machine-checking.sh<br>
alert.sh<br>
create-json-for-es.sh<br>
main.sh<br>
clean-up.sh
***

## 運作邏輯
- 透過 machine-checking.sh 以 DSL 語法撈出需要對比的資料 (此處用host.keyword)，每五分鐘做一次query，將五分鐘前到現在 (ex.11:55~12:00) 的所有**host.keyword**撈出來寫成$now_file.txt
- alert.sh 比對前後兩個檔案資料的差異寫入 result.csv，以此確認上一次撈資料到現在，有那些 host 新增或減少。
- create-json-for-es.sh ，將比對好的 result.csv 轉換成可用 cURL 寫入 ES 的 detect.json 。
- main.sh，主程式，依序執行前列三個程式，判斷是否有需要更新 host 的狀態後寫入 ES 。
	- host 有增有減才需要記錄定寫入 ES 。
	- 有可能撈出來的 host 一直都沒有增減 ，就不需重複寫入。
	

## Part 1 透過DSL語法撈ES中指定index資料

### machine-checking.sh
- line 3.4.5 -  $now、$last，用於DSL語法中的時間格式，告訴ES需要的資料時間區間 ; $now_file，資料轉成txt檔時用來區隔時間。
	- $last 中的**"5 minute ago"**可以調整為其他時間間隔，如10分鐘撈一次資料就是**"10 minute ago"**，此處如果變更，crontab中 main.sh 排程的時間也要改為每十分鐘執行一次。
	- 特別注意要 +"08:00" ，取出來的時間區間才不會錯 。

- line 13 - **"field": "host.keyword"**，需要監測的欄位，"host.keyword" 可以換成其他需要的欄位。
- line 8~58 的 ' 前 - DSL 語法
	- line 8 - **"http://localhost:9200/logstash-firewall-asa*/_search"** 搜尋指定 index 的資料 。
- line 58 -  **| jq '.aggregations' | jq .[].buckets | jq .[].key >> /home/disney/log-detect/check/$now_file.txt** ，使用 jq 選取資料並整理後轉成 $now_file.txt




```
  1 #!/bin/bash
  2
  3 now=`date +"%Y-%m-%dT%H:%M"+"08:00"`
  4 last=`date -d "5 minute ago" +"%Y-%m-%dT%H:%M"+"08:00"`
  5 now_file=`date +"%Y-%m-%dT%H:%M"`
  6
  7 #### machine checking
  8 curl -XGET "http://localhost:9200/logstash-firewall-asa*/_search" -H 'Content-Type: application/json' -d'
  9 {
 10   "aggs": {
 11     "2": {
 12       "terms": {
 13         "field": "host.keyword",
 14         "order": {
 15           "_count": "desc"
 16         },
 17         "size": 50
 18       }
 19     }
 20   },
 21   "size": 0,
 22   "fields": [
 23     {
 24       "field": "@timestamp",
 25       "format": "date_time"
 26     }
 27   ],
 28   "script_fields": {},
 29   "stored_fields": [
 30     "*"
 31   ],
 32   "runtime_mappings": {},
 33   "_source": {
 34     "excludes": []
 35   },
 36   "query": {
 37     "bool": {
 38       "must": [],
 39       "filter": [
 40         {
 41           "match_all": {}
 42         },
 43         {
 44           "range": {
 45             "@timestamp": {
 46               "gte": "'$last'",
 47               "lte": "'$now'",
 48               "format": "strict_date_optional_time"
 49             }
 50           }
 51         }
 52       ],
 53       "should": [],
 54       "must_not": []
 55     }
 56   }
 57 }
 58 ' | jq '.aggregations' | jq .[].buckets | jq .[].key >> /home/disney/log-detect/check/$now_file.txt
```
## Part 2 比較前後檔案差異，整理成所需格式寫入 result.csv

### alert.sh

- line 7	- 用 diff 比較現在與前五分鐘產生的 txt 檔之間的差異(排序**sort**)寫入 result.csv 。
- line 9、10 - 用 sed 整理 result.csv
	- **>** 代表後一個檔案比前一個檔案增加的內容，以**new**取代**>**。
	- **<** 代表後一個檔案比前一個檔案減少的內容，以**lost**取代**<**。
- line 11 - 在 result.csv 每一行的開頭加上 **"$last1"':00,** ，為每一筆資料加上時間戳。

```
  1 #!/bin/bash
  2
  3 now=`date +"%Y-%m-%dT%H:%M"`
  4 last=`date -d "5 minute ago" +"%Y-%m-%dT%H:%M"`
  5 last1=`date -d "5 minute ago" +"%Y-%m-%d %H:%M"`
  6
  7 diff <(sort /home/disney/log-detect/check/$last.txt) <(sort /home/disney/log-detect/check/$now.txt ) |grep -E "^>|^<" > /home/disney/log-detect/result.csv
  8
  9 sed -i 's/> /new,/g' /home/disney/log-detect/result.csv
 10 sed -i 's/< /lost,/g' /home/disney/log-detect/result.csv
 11 sed -i 's/^/'"$last1"':00,/g' /home/disney/log-detect/result.csv
```

## Part 3 將 result.csv 轉成 json file 

### create-json-for-es.sh

- line 15~24 - 轉換時間格式的 function ，將 result.csv 的時間戳做轉換。
- line 30~32 - QTIME、STATUS、HOST，result.csv 中的三個欄位。
-  line 33~34 - 將 QTIME 帶入 **function timeformat** 轉換時間格式，並用 strftime 轉成符合 ES 的時間格式。
-  line 35~42 - 格式編輯，轉成 json 格式並寫入 detect.json 

```
 1 #!/bin/bash
  2 ######################################################
  3 ## linux_top2ali :  2017-07-07
  4 ######################################################
  5 udrfile=$1
  6 ###################################################################
  7 #### step0: setup env
  8 ###################################################################
  9 if [ $# -lt 1 ] ;then
 10  echo "usage: $0 udrfile"
 11  exit
 12 fi
 13
 14 awk -F"," '
 15 function timeformat(csvtime) {       # 2022-01-28 02:22:00
 16     split(csvtime,XX," ");datex=XX[1]; timex=substr(XX[2],1,8);
 17     split(datex,dd,"-");year=dd[1];month=dd[2];day=dd[3];
 18     print dd[1]
 19     split(timex,tt,":");hour=tt[1];minute=tt[2];second=tt[3];
 20     realtime=sprintf("%04d %02d %02d %s %s %s",year,month,day,hour,minute,second);
 21     epoch=mktime(realtime);
 22     return epoch;    #
 23
 24 }
 25 BEGIN{
 26  indexname="log-detect"
 27  es_type="_doc"
 28 }
 29 {
 30  QTIME=$1
 31  STATUS=$2
 32  HOST=$3
 33  epoch=timeformat(QTIME)
 34     timestamp=strftime("%Y-%m-%dT%H:%M:%S+08:00",epoch);
 35  idxname="log-detect"oes_lastcode"-"NEXT_BILL_T
 36  title=sprintf("{\"index\": {\"_type\": \"%s\", \"_index\": \"%s\"}}\n",  es_type, idxname );
 37     str1=sprintf("{"); separator = ""
 38     str1=str1""sprintf("%s\"@timestamp\": \"%s\"",separator,timestamp);
 39    separator = ","
 40     str1=str1""sprintf("%s\"STATUS\": \"%s\"",separator,STATUS);
 41     str1=str1""sprintf("%s\"HOST\": %s",separator,HOST);
 42  print title str1 "}" > "/home/disney/log-detect/detect.json"
 43 }' $udrfile

```

## Part 4 main shell 主程式 

### main.sh

- line 6~8 - 依序執行 Part 1 ~ 3 的程式。
- line 10~15 - 判斷 result.csv 是否為空的
	- 若是有資料，程式往下走，將 detect.json 中的內容寫入ES。
	- 若是空的(前後兩個 txt 無差異，代表 host 沒有新增或減少) ，則中斷程式不寫入ES。
- line 17 - 用 cURL 將 detect.json 中的內容寫入ES。

```
  1 #!/bin/bash
  2
  3 var=`cat result.csv`
  4 echo $var
  5
  6 bash /home/disney/log-detect/machine-checking.sh
  7 bash /home/disney/log-detect/alert.sh
  8 bash /home/disney/log-detect/create-json-for-es.sh /home/disney/log-detect/result.csv
  9
 10 if [[-n "$var"]]; then
 11         echo "not empty"
 12 else
 13         echo "empty"
 14         exit
 15 fi
 16
 17 curl -s -XPOST "http://localhost:9200/_bulk?pretty" -H 'Content-Type: application/json' --data-binary @/home/disney/log-detect/detect.json
 18 echo `date` >> /home/disney/log-detect/record.txt
```

## Part 5 定時清除過時的資料

### clean-up.sh 


```
  1 #!/bin/bash
  2
  3 date=`date -d "1 day ago" +"%Y-%m-%d"`
  4
  5 rm -rf /home/disney/log-detect/check/$date*.txt
  6
  7 echo $date
```



