# MA013 - ES Template 設定 


## Kibana Dev Tools

### 查看 Template設定
- logstash-bimap：欲查看的Template 名稱。

```
GET _template/logstash-bimap
```

### 新增 Template

輸入以下內容：

- line 1 - ``PUT_template/walsin-temp``，walsin-temp：新建的 Template 名稱。
- line 4 - "order" 代表優先順序，數字越大優先順序越高。
- line 5 - "index _ patterns"，將此 template 設定套用在符合條件的 index_pattern。
- line 11~12 - "limit"，欄位最大數量。



```
  1 PUT _template/walsin-temp
  2 {
  3
  4     "order" : 3,
  5     "index_patterns" : [
  6       "logstash-*"
  7     ],
  8     "settings" : {
  9       "index" : {
 10         "mapping" : {
 11           "total_fields" : {
 12             "limit" : "2000"
 13           }
 14         },
 15         "refresh_interval" : "5s",
 16         "number_of_shards" : "1",
 17         "number_of_replicas" : "1"
 18       }
 19     },
 20     "mappings" : {
 21       "dynamic_templates" : [
 22         {
 23           "message_field" : {
 24             "path_match" : "message",
 25             "mapping" : {
 26               "norms" : false,
 27               "type" : "text"
 28             },
 29             "match_mapping_type" : "string"
 30           }
 31         },
 32         {
 33           "string_fields" : {
 34             "mapping" : {
 35               "norms" : false,
 36               "type" : "text",
 37               "fields" : {
 38                 "keyword" : {
 39                   "ignore_above" : 256,
 40                   "type" : "keyword"
 41                 }
 42               }
 43             },
 44             "match_mapping_type" : "string",
 45             "match" : "*"
 46           }
 47         }
 48       ],
 49       "date_detection" : false,
 50       "properties" : {
 51         "@timestamp" : {
 52           "type" : "date"
 53         },
 54         "destinationAddress" : {
 55           "type" : "ip"
 56         },
 57         "geoip" : {
 58           "dynamic" : true,
 59           "type" : "object",
 60           "properties" : {
 61             "ip" : {
 62               "type" : "ip"
 63             },
 64             "latitude" : {
 65               "type" : "half_float"
 66             },
 67             "location" : {
 68               "type" : "geo_point"
 69             },
 70             "longitude" : {
 71               "type" : "half_float"
 72             }
 73           }
 74         },
 75         "sourceAddress" : {
 76           "type" : "ip"
 77         },
 78         "@version" : {
 79           "type" : "keyword"
 80         },
 81         "src_geoip" : {
 82           "dynamic" : true,
 83           "type" : "object",
 84           "properties" : {
 85             "ip" : {
 86               "type" : "ip"
 87             },
 88             "latitude" : {
 89               "type" : "half_float"
 90             },
 91             "location" : {
 92               "type" : "geo_point"
 93             },
 94             "longitude" : {
 95               "type" : "half_float"
 96             }
 97           }
 98         },
 99         "dest_geoip" : {
100           "dynamic" : true,
101           "type" : "object",
102           "properties" : {
103             "ip" : {
104               "type" : "ip"
105             },
106             "latitude" : {
107               "type" : "half_float"
108             },
109             "location" : {
110               "type" : "geo_point"
111             },
112             "longitude" : {
113               "type" : "half_float"
114             }
115           }
116         }
117       }
118     },
119     "aliases" : { }
120
121 }
```