# MA002 - 檢查 ELK 的 log 路徑和內容

## 檢查 elasticsearch 的 log：


```
root@bimap:/# cd /var/log/elasticsearch

root@bimap:/var/log/elasticsearch# ls -al bimap*

-rw-r--r-- 1 elasticsearch elasticsearch  6127 Oct 30 08:58 bimap-2021-10-29-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  5776 Oct 30 08:58 bimap-2021-10-29-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   488 Oct 31 08:58 bimap-2021-10-30-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   357 Oct 31 08:58 bimap-2021-10-30-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   484 Nov  1 08:57 bimap-2021-10-31-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   351 Nov  1 08:58 bimap-2021-10-31-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  4862 Nov  2 08:58 bimap-2021-11-01-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  4632 Nov  2 08:58 bimap-2021-11-01-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   489 Nov  3 08:58 bimap-2021-11-02-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   358 Nov  3 08:58 bimap-2021-11-02-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   487 Nov  4 08:57 bimap-2021-11-03-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   357 Nov  4 08:57 bimap-2021-11-03-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   482 Nov  5 08:58 bimap-2021-11-04-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   350 Nov  5 08:58 bimap-2021-11-04-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   484 Nov  6 08:57 bimap-2021-11-05-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   352 Nov  6 08:57 bimap-2021-11-05-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   481 Nov  7 08:57 bimap-2021-11-06-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   349 Nov  7 08:57 bimap-2021-11-06-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   482 Nov  8 08:58 bimap-2021-11-07-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   350 Nov  8 08:58 bimap-2021-11-07-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   484 Nov  9 08:57 bimap-2021-11-08-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   352 Nov  9 08:58 bimap-2021-11-08-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   482 Nov 10 08:57 bimap-2021-11-09-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   350 Nov 10 08:58 bimap-2021-11-09-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   847 Nov 11 08:00 bimap-2021-11-10-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   702 Nov 11 08:00 bimap-2021-11-10-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1019 Nov 12 08:00 bimap-2021-11-11-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   844 Nov 12 08:00 bimap-2021-11-11-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   730 Nov 13 08:00 bimap-2021-11-12-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   574 Nov 13 08:00 bimap-2021-11-12-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   748 Nov 14 08:00 bimap-2021-11-13-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   593 Nov 14 08:00 bimap-2021-11-13-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   736 Nov 15 08:00 bimap-2021-11-14-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   581 Nov 15 08:00 bimap-2021-11-14-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   731 Nov 16 08:00 bimap-2021-11-15-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   574 Nov 16 08:00 bimap-2021-11-15-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   741 Nov 17 08:00 bimap-2021-11-16-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   582 Nov 17 08:00 bimap-2021-11-16-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   796 Nov 18 08:00 bimap-2021-11-17-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   632 Nov 18 08:00 bimap-2021-11-17-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   750 Nov 19 08:00 bimap-2021-11-18-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   590 Nov 19 08:00 bimap-2021-11-18-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  2550 Nov 20 08:00 bimap-2021-11-19-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  2262 Nov 20 08:00 bimap-2021-11-19-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   916 Nov 21 08:00 bimap-2021-11-20-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   735 Nov 21 08:00 bimap-2021-11-20-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   917 Nov 22 08:00 bimap-2021-11-21-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   738 Nov 22 08:00 bimap-2021-11-21-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   944 Nov 23 08:00 bimap-2021-11-22-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   763 Nov 23 08:00 bimap-2021-11-22-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  2172 Nov 24 08:00 bimap-2021-11-23-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1989 Nov 24 08:00 bimap-2021-11-23-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch   950 Nov 25 08:00 bimap-2021-11-24-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch   767 Nov 25 08:00 bimap-2021-11-24-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  2034 Nov 26 08:00 bimap-2021-11-25-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1742 Nov 26 08:00 bimap-2021-11-25-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1445 Nov 27 08:00 bimap-2021-11-26-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1222 Nov 27 08:00 bimap-2021-11-26-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1271 Nov 28 08:00 bimap-2021-11-27-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1063 Nov 28 08:00 bimap-2021-11-27-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1920 Nov 29 08:00 bimap-2021-11-28-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1643 Nov 29 08:00 bimap-2021-11-28-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1413 Nov 30 08:00 bimap-2021-11-29-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1190 Nov 30 08:00 bimap-2021-11-29-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1470 Dec  1 08:00 bimap-2021-11-30-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1231 Dec  1 08:00 bimap-2021-11-30-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1563 Dec  2 08:00 bimap-2021-12-01-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1306 Dec  2 08:00 bimap-2021-12-01-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1469 Dec  3 08:00 bimap-2021-12-02-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1224 Dec  3 08:00 bimap-2021-12-02-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1365 Dec  4 08:00 bimap-2021-12-03-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1140 Dec  4 08:00 bimap-2021-12-03-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1317 Dec  5 08:00 bimap-2021-12-04-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1090 Dec  5 08:00 bimap-2021-12-04-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1284 Dec  6 08:00 bimap-2021-12-05-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1061 Dec  6 08:00 bimap-2021-12-05-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1314 Dec  7 08:00 bimap-2021-12-06-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1089 Dec  7 08:00 bimap-2021-12-06-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1332 Dec  8 08:00 bimap-2021-12-07-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1093 Dec  8 08:00 bimap-2021-12-07-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1322 Dec  9 08:00 bimap-2021-12-08-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1091 Dec  9 08:00 bimap-2021-12-08-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1414 Dec 10 08:00 bimap-2021-12-09-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1190 Dec 10 08:00 bimap-2021-12-09-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1295 Dec 11 08:00 bimap-2021-12-10-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1084 Dec 11 08:00 bimap-2021-12-10-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1312 Dec 12 08:00 bimap-2021-12-11-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1085 Dec 12 08:00 bimap-2021-12-11-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1284 Dec 13 08:00 bimap-2021-12-12-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1068 Dec 13 08:00 bimap-2021-12-12-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1400 Dec 14 08:00 bimap-2021-12-13-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1177 Dec 14 08:00 bimap-2021-12-13-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1365 Dec 15 08:00 bimap-2021-12-14-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1139 Dec 15 08:00 bimap-2021-12-14-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1384 Dec 16 08:00 bimap-2021-12-15-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1141 Dec 16 08:00 bimap-2021-12-15-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1638 Dec 17 08:00 bimap-2021-12-16-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1392 Dec 17 08:00 bimap-2021-12-16-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1767 Dec 18 08:00 bimap-2021-12-17-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1506 Dec 18 08:00 bimap-2021-12-17-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1357 Dec 19 08:00 bimap-2021-12-18-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1128 Dec 19 08:00 bimap-2021-12-18-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1377 Dec 20 08:00 bimap-2021-12-19-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1134 Dec 20 08:00 bimap-2021-12-19-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1357 Dec 21 08:00 bimap-2021-12-20-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1125 Dec 21 08:00 bimap-2021-12-20-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1436 Dec 22 08:00 bimap-2021-12-21-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1210 Dec 22 08:00 bimap-2021-12-21-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1352 Dec 23 08:00 bimap-2021-12-22-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1112 Dec 23 08:00 bimap-2021-12-22-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1467 Dec 24 08:00 bimap-2021-12-23-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1216 Dec 24 08:00 bimap-2021-12-23-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1483 Dec 25 08:00 bimap-2021-12-24-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1247 Dec 25 08:00 bimap-2021-12-24-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1379 Dec 26 08:00 bimap-2021-12-25-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1154 Dec 26 08:00 bimap-2021-12-25-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1326 Dec 27 08:00 bimap-2021-12-26-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1102 Dec 27 08:00 bimap-2021-12-26-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1556 Dec 28 08:00 bimap-2021-12-27-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1308 Dec 28 08:00 bimap-2021-12-27-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1935 Dec 29 08:00 bimap-2021-12-28-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1656 Dec 29 08:00 bimap-2021-12-28-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1357 Dec 30 08:00 bimap-2021-12-29-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1135 Dec 30 08:00 bimap-2021-12-29-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1635 Dec 31 08:00 bimap-2021-12-30-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1371 Dec 31 08:00 bimap-2021-12-30-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1286 Jan  1 08:00 bimap-2021-12-31-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1068 Jan  1 08:00 bimap-2021-12-31-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1336 Jan  2 08:00 bimap-2022-01-01-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1107 Jan  2 08:00 bimap-2022-01-01-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1345 Jan  3 08:00 bimap-2022-01-02-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1116 Jan  3 08:00 bimap-2022-01-02-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1418 Jan  4 08:00 bimap-2022-01-03-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1184 Jan  4 08:00 bimap-2022-01-03-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1648 Jan  5 08:00 bimap-2022-01-04-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1409 Jan  5 08:00 bimap-2022-01-04-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1482 Jan  6 08:00 bimap-2022-01-05-1.json.gz
-rw-r--r-- 1 elasticsearch elasticsearch  1236 Jan  6 08:00 bimap-2022-01-05-1.log.gz
-rw-r--r-- 1 elasticsearch elasticsearch 10058 Jan  6 16:43 bimap.log
-rw-r--r-- 1 elasticsearch elasticsearch     0 Oct 29 17:59 bimap_audit.json
-rw-r--r-- 1 elasticsearch elasticsearch  3560 Nov 28 18:25 bimap_deprecation.json
-rw-r--r-- 1 elasticsearch elasticsearch  1803 Nov 28 18:25 bimap_deprecation.log
-rw-r--r-- 1 elasticsearch elasticsearch     0 Oct 29 17:59 bimap_index_indexing_slowlog.json
-rw-r--r-- 1 elasticsearch elasticsearch     0 Oct 29 17:59 bimap_index_indexing_slowlog.log
-rw-r--r-- 1 elasticsearch elasticsearch     0 Oct 29 17:59 bimap_index_search_slowlog.json
-rw-r--r-- 1 elasticsearch elasticsearch     0 Oct 29 17:59 bimap_index_search_slowlog.log
-rw-r--r-- 1 elasticsearch elasticsearch 23182 Jan  6 16:43 bimap_server.json

```


```
root@bimap:/var/log/elasticsearch# tail -f bimap.log | more

[2022-01-06T02:58:08,778][INFO ][o.e.c.m.MetadataMappingService] [bimap] [logstash-winlogbeat-20220106/lUOlK-8rQRaJSZg-PDvVbg] update_mapping [_doc]
[2022-01-06T02:58:24,828][INFO ][o.e.c.m.MetadataMappingService] [bimap] [logstash-winlogbeat-20220106/lUOlK-8rQRaJSZg-PDvVbg] update_mapping [_doc]
[2022-01-06T05:54:02,794][INFO ][o.e.c.m.MetadataMappingService] [bimap] [logstash-winlogbeat-20220106/lUOlK-8rQRaJSZg-PDvVbg] update_mapping [_doc]
[2022-01-06T05:55:32,826][INFO ][o.e.c.m.MetadataMappingService] [bimap] [logstash-winlogbeat-20220106/lUOlK-8rQRaJSZg-PDvVbg] update_mapping [_doc]
[2022-01-06T06:36:35,312][INFO ][o.e.c.m.MetadataMappingService] [bimap] [logstash-winlogbeat-20220106/lUOlK-8rQRaJSZg-PDvVbg] update_mapping [_doc]
[2022-01-06T06:36:41,411][INFO ][o.e.c.m.MetadataMappingService] [bimap] [logstash-winlogbeat-20220106/lUOlK-8rQRaJSZg-PDvVbg] update_mapping [_doc]
[2022-01-06T06:38:29,768][INFO ][o.e.c.m.MetadataMappingService] [bimap] [logstash-winlogbeat-20220106/lUOlK-8rQRaJSZg-PDvVbg] update_mapping [_doc]
[2022-01-06T07:30:14,015][INFO ][o.e.c.m.MetadataMappingService] [bimap] [logstash-winlogbeat-20220106/lUOlK-8rQRaJSZg-PDvVbg] update_mapping [_doc]
[2022-01-06T08:43:14,371][INFO ][o.e.c.m.MetadataMappingService] [bimap] [logstash-winlogbeat-20220106/lUOlK-8rQRaJSZg-PDvVbg] update_mapping [_doc]
[2022-01-06T08:43:19,184][INFO ][o.e.c.m.MetadataMappingService] [bimap] [logstash-winlogbeat-20220106/lUOlK-8rQRaJSZg-PDvVbg] update_mapping [_doc]

```


