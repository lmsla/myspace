# MA004 - housekeeping 設定

## 建立 housekeeping：

- 程式路徑：/home/disney/bin/housekeeping.sh
- 日誌路徑：/home/disney/bin/indices.log

```
$ vim /home/bimap/bin/housekeeping.sh
```
```
#!/bin/bash

ESIP="localhost"
datex=`date -d "-3 day" +%Y_%m_%d`
datey=`date -d "-1 month" +%Y_%m`
logdir="/home/disney/bin"

echo date >>  $logdir/indices.log
echo "--------------------------------------------------------------------" >>$logdir/indices.log
curl -XGET "http://$ESIP:9200/_cat/indices/logstash-citrix-walsin-$datey" >>$logdir/indices.log
curl -XGET "http://$ESIP:9200/_cat/indices/logstash-nac-walsin-$datey"  >>$logdir/indices.log
curl -XGET "http://$ESIP:9200/_cat/indices/logstash-virus-walsin-$datey"  >>$logdir/indices.log
curl -XGET "http://$ESIP:9200/_cat/indices/logstash-identity-walsin-$datey"  >>$logdir/indices.log
curl -XGET "http://$ESIP:9200/_cat/indices/logstash-waf-walsin-$datey"  >>$logdir/indices.log
curl -XGET "http://$ESIP:9200/_cat/indices/logstash-firewall-fortigate-walsin-$datex"  >>$logdir/indices.log
curl -XGET "http://$ESIP:9200/_cat/indices/logstash-firewall-asa-walsin-$datex"  >>$logdir/indices.log
curl -XGET "http://$ESIP:9200/_cat/indices/logstash-windows-ad_server-$datex"  >>$logdir/indices.log
curl -XGET "http://$ESIP:9200/_cat/indices/logstash-windows-notes_server-$datey"  >>$logdir/indices.log
curl -XGET "http://$ESIP:9200/_cat/indices/logstash-windows-infra_client-$datey"  >>$logdir/indices.log

#curl http://$ESIP:9200/_cat/indices | grep $datex >> $logdir/indices.log
#curl http://$ESIP:9200/_cat/indices | grep $datey >> $logdir/indices.log

curl -XDELETE "http://$ESIP:9200/logstash-citrix-walsin-$datey"
curl -XDELETE "http://$ESIP:9200/logstash-nac-walsin-$datey"
curl -XDELETE "http://$ESIP:9200/logstash-virus-walsin-$datey"
curl -XDELETE "http://$ESIP:9200/logstash-identity-walsin-$datey"
curl -XDELETE "http://$ESIP:9200/logstash-waf-walsin-$datey"
curl -XDELETE "http://$ESIP:9200/logstash-firewall-fortigate-walsin-$datex"
curl -XDELETE "http://$ESIP:9200/logstash-firewall-asa-walsin-$datex"
curl -XDELETE "http://$ESIP:9200/logstash-windows-ad_server-$datex"
curl -XDELETE "http://$ESIP:9200/logstash-windows-notes_server-$datey"
curl -XDELETE "http://$ESIP:9200/logstash-windows-infra_client-$datey"

```

- 設定 crontab ( 定時任務 ) :

```
$ crontab -e 
```
```
# 設定每日10點執行
* 10 * * * sh /home/disney/bin/housekeeping.sh       
```