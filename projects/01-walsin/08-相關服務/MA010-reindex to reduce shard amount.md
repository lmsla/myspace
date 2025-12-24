# MA010 - reindex to reduce shard amount 


## Shard 管理

Shard 是 ES Cluster 管理的最小單位，並沒有一定的限制。主要目的是可以將資料分散於多台 Node，假如資料量大時，多台 Node 也可較好分擔 indexing 的需求，但如資料量並不像防火牆、網路設備一般，如此龐大，則可以少一點為佳。

在初期管理 Elasticsearch 時，錯估 index size 是常事，假以時日之後，則需要調整 index，否則時常會出現 shard 爆量的錯誤。一般來說，假如一天資料在 1G 左右，則可以考慮以月為單位來當成儲存的單位，或是保持在一個 shard 為 30G 的大小。


## Reindex

index 每日儲存 1G，一個月有 30 個 index，則可以考慮以月來切分 index，此時我們利用 es api 處理 reindex 的行為。

我們希望 4 月份的每一個 index，都放置於 windows-202004 這一個 index 中。例如：windows-20200401、windows-20200402 ......，reindex 至 windows-202004。


通常使用我們會將 **wait_ for_ completion** 為 false，不等待 reindex 的時間，**requests_ per_ second** 為 3000，避免 loading 過大。

```
POST _reindex?wait_for_completion=false&requests_per_second=3000&refresh=true
{
  "source": {
    "index": "windows-202004*"
  },
  "dest": {
    "index": "windows-202004"
  }
}
```

## Check Task Status

因為我們設定 request_per_seconds 為 3000，所以資料量大的話，需要一點時間，所以當 api 執行成功之後，會返回一個 task id，然後可以用 task api 查詢狀態。

如果 task 回傳的狀態中，completed 為 true，total 與 created 一致的話，基本上就完成了。假如不一致，則是有可能產生了 failure，可以在 failure 的欄位中查看錯誤訊息。

```
GET /_tasks/FvSJFfacTj-YS3wkm8chwA:929864780
```
```
{
  "completed" : true,
  "task" : {
    "node" : "FvSJFfacTj-YS3wkm8chwA",
    "id" : 929938964,
    "type" : "transport",
    "action" : "indices:data/write/reindex",
    "status" : {
      "total" : 2207344,
      "updated" : 0,
      "created" : 2207344,
      "deleted" : 0,
      "batches" : 2208,
      "version_conflicts" : 0,
      "noops" : 0,
      "retries" : {
        "bulk" : 0,
        "search" : 0
      },
      "throttled_millis" : 735780,
      "requests_per_second" : 3000.0,
      "throttled_until_millis" : 0
    },
    "description" : "reindex from [logstash-windows-202201*] to [logstash-windows-202201][_doc]",
    "start_time_in_millis" : 1644908229517,
    "running_time_in_nanos" : 2038569567525,
    "cancellable" : true,
    "headers" : { }
  },
  "response" : {
    "took" : 2038569,
    "timed_out" : false,
    "total" : 2207344,
    "updated" : 0,
    "created" : 2207344,
    "deleted" : 0,
    "batches" : 2208,
    "version_conflicts" : 0,
    "noops" : 0,
    "retries" : {
      "bulk" : 0,
      "search" : 0
    },
    "throttled" : "12.2m",
    "throttled_millis" : 735780,
    "requests_per_second" : 3000.0,
    "throttled_until" : "0s",
    "throttled_until_millis" : 0,
    "failures" : [ ]
  }
}
```