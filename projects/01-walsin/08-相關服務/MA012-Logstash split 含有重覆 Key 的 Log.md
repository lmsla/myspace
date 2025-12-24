# MA012 - Logstash split 含有重覆 Key 的 Log 


## 含有重覆 Key 的 Log 範例

在該範例中，我們可以發現如果要以 grok 解析該 Log，會產生多個重覆 Label，但以 1、2、3 後贅字序列的方式區別每個 Label 也不是一個好方法。因此，這一次我們希望先用 ruby 將多組 Label 拆分為陣列，再使用 Split Plugin 的方式，再將此陣列拆為獨立一個 Log。

```
<166>Jul 4 15:02:51 xx-xxx BiMAPXXX[0000]: 10.10.10.10,XX00000-WWW,範例-GG,
Label: Security Update for Microsoft Update Time: 4/9/21 12:44:07 AM Severity: Important Product: Office CVE: , 
Label: Security Update for Microsoft Update Time: 4/9/21 12:46:18 AM Severity: Important Product: Office CVE: , 
Label: MS11-025 : Security Update for Update Time: 6/27/17 8:56:20 AM Severity: Important Product: Developer Tools, Runtimes, and Redistributables CVE: CVE-0000-0000
```

所以概念上，因為 Label 有三組，所以希望我們的 Log 由一組變為三組：

```
<166>Jul 4 15:02:51 xx-xxx BiMAPXXX[0000]:10.10.10.10,XX00000-WWW,範例-GG,
Label: Security Update for Microsoft Update Time: 4/9/21 12:44:07 AM Severity:Important Product: Office CVE:
```

```
<166>Jul 4 15:02:51 xx-xxx BiMAPXXX[0000]:10.10.10.10,XX00000-WWW,範例-GG,
Label: Security Update for Microsoft Update Time: 4/9/21 12:46:18 AM Severity:Important Product: Office CVE:
```

```
<166>Jul 4 15:02:51 xx-xxx BiMAPXXX[0000]:10.10.10.10,XX00000-WWW,範例-GG,
Label: MS11-025 : Security Update for Update Time: 6/27/17 8:56:20 AMSeverity: Important Product: Developer Tools, Runtimes, and RedistributablesCVE: CVE-0000-0000
```

## 使用 Ruby 將重覆性 Label 轉為陣列

先用 grok 將標頭解析，並將後面 Label 重覆的部份，統一收於 remain_log 中

```
grok { 
    match => {"message" => [ 
        "<%{NUMBER:log_id}>%{CISCOTIMESTAMP:event_time}%{SPACE}%{NOTSPACE:device_name}%{SPACE}%{WORD:module}\[%{NUMBER:module_event_id}\]:%{SPACE}%{IPV4:ip},%{DATA:user_computer_name},%{DATA:user_name},%{GREEDYDATA:remain_log}", 
        "%{GREEDYDATA:bimap_log}" 
    ]} 
}
```
透過 grok 好的 remain_log，丟進 ruby 中處理，以 Label 為 split 的元素，將其轉為陣列存放於 label_arr 中。

```
def register(params)
end 
def filter(event) 
    splitter = "Label: " 
        if !event.get("remain_log").nil? 
                if event.get("remain_log").include? splitter 
                        dataArr = event.get("remain_log").split(splitter).reject { |c| c.empty? } 
                        event.set("label_arr", dataArr) 
                else 
                        event.set("label_arr", [event.get("remain_log")]) 
                end 
        end 
        return [event] 
end
```

## 使用 Split Plugin 將 Log 拆分

因為使用 ruby 把重覆性的 Label 的轉成陣列，並存放於 label_arr 中，接下來就可以使用 logstash split plugin，將陣列的每一個元素，轉換為各別獨立的一段 Log。

```
split { 
    field => "label_arr" 
    target => "advise_information" 
}
```
透過 Split 後的資料，就會依照 Label 的重覆數量，轉為對應組數的 Log。

## 完整程式

Logstash :

```
filter {
    grok { 
        match => {"message" => [ 
                "<%{NUMBER:log_id}>%{CISCOTIMESTAMP:event_time}%{SPACE}%{NOTSPACE:device_name}%{SPACE}%{WORD:module}\[%{NUMBER:module_event_id}\]:%{SPACE}%{IPV4:ip},%{DATA:user_computer_name},%{DATA:user_name},%{GREEDYDATA:remain_log}", 
                "%{GREEDYDATA:bimap_log}" 
        ]} 
    } 
    ruby { 
        path => "./bimap.rb" 
    } 
    if [label_arr] { 
        split { 
            field => "label_arr" 
            target => "advise_information" 
        } 
    } 
    grok { 
        match => {"advise_information" => [ 
            "%{DATA:update_item}%{SPACE}Update Time:%{SPACE}%{DATA:update_time}%{SPACE}Severity:%{SPACE}%{DATA:severity}%{SPACE}Product:%{SPACE}%{WORD:product}%{SPACE}CVE:%{SPACE}%{GREEDYDATA:CVE},", 
            "%{DATA:update_item}%{SPACE}Update Time:%{SPACE}%{DATA:update_time}%{SPACE}Severity:%{SPACE}%{DATA:severity}%{SPACE}Product:%{SPACE}%{WORD:product}%{SPACE}CVE:%{SPACE}%{GREEDYDATA:CVE}", 
            "%{GREEDYDATA:advise_information_log}" 
        ]} 
    } 
    mutate { 
        remove_field => [ "label_arr", "advise_information", "reamin_log" ] 
    }
}
```
Ruby Code :

```
def register(params)
end 
def filter(event) 
    splitter = "Label: " 
        if !event.get("remain_log").nil? 
                if event.get("remain_log").include? splitter 
                        dataArr = event.get("remain_log").split(splitter).reject { |c| c.empty? } 
                        event.set("label_arr", dataArr) 
                else 
                        event.set("label_arr", [event.get("remain_log")]) 
                end 
        end 
        return [event] 
end
``` 