# MA011 - Logstash根據時區, 截取部份日期年、月、日 


## 異常登入情境
在每日 0 點 - 8 點為不合理的登入時間，因此希望針對 hour 的部份單獨有個欄位判斷。

## 程式碼
根據 Log 的時區，轉為當地時區，並將 hour 單獨取出

```
filter {
    ruby {
        code => "require 'date'; datetime =
  DateTime.strptime(event.get('log_time'), '%m/%d/%Y:%H:%M:%S'); taipei_time =
  datetime.to_time + 8*60*60; event.set("recv_hour", taipei_time.hour);}}"
    }
}
```