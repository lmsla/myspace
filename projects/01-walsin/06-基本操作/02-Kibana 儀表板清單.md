#### (4) Windows_Trace Metrics
#### (5) Windows_Trace Metrics  


# Kibana 儀表板清單

## 1. Windows
### ㄧ. Windows Security Overview
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/windows_security_overview.jpeg)

#### (1) Link_Windows :
快捷列，方便切換系列儀表板。
#### (2) Windows SecurityOverview Metrics Count :
security 事件數量統計。
#### (3) Windows SecurityOverview Metrics :
觸發事件總類。
#### (4) Windows SecurityOverview Metrics Target User :
目標 User 數量。
#### (5) Windows SecurityOverview Metrics Severity :
事件發生筆數按嚴重性分類統計。
#### (6) Windows SecurityOverview Metrics UniServer :
受監控 Server 數量。
#### (7) Windows SecurityOverview Metrics User :
User 數量。
#### (8) Windows SecurityOverview Datatable Server :
受監控 Server 總覽表格。
#### (9) Windows SecurityOverview Bar Count : 
受監控 Server 柱狀圖 (時序排列)。
#### (10) Windows SecurityOverview Datatable EventCodeOverview :
事件 (event) 總覽表格。
#### (11) Windows SecurityOverview Pie Description :
事件描述圓餅圖。
#### (12) Windows SecurityOverview Datatable SubjectUser :
用戶資訊總覽表格。
#### (13) Windows SecurityOverview Datatable TargetUser :
目標用戶資訊總覽表格。
#### (14) Windows SecurityOverview Discover :
日誌索引總表 (Discover)。

### 二. Windows LoginFailer
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/windows_%E7%99%BB%E5%85%A5%E5%A4%B1%E6%95%97.jpeg)
#### (1) Link_Windows :
快捷列，方便切換系列儀表板。
#### (2) Windows LoginFailure Metric CountLoginFailure :
大字報，統計登入失敗次數。
#### (3) Windows LoginFailure Metric UniLoginfailureUser :
大字報，統計登入失敗用戶數量。
#### (4) Windows LoginFailure Metric UniLoginfailureSERVERUSer :
大字報，統計登入失敗用戶及 Server 數量。
#### (5) Windows LoginFailure Metric UniLoginfailureIP :
大字報，統計登入失敗 IP。
#### (6) Windows LoginFailure Datatable CountLoginFailureUser :
表格，統計登入失敗用戶名、來源 IP 及登入失敗次數。
#### (7) Windows LoginFailure Line CountLoginfailureUser :
線型圖，標示出各時間段用戶登入失敗次數。
#### (8) Windows LoginFailure Datatable CountLoginFailureIP :
表格，統計失敗來源 IP 之登入失敗次數。
#### (9) Windows LoginFailure Bar CountSrcIPUser :
柱狀圖，以柱狀圖表示登入失敗用戶與登入失敗的關係。
#### (10) Windows LoginFailure Datatable CountServerIP :
表格，統計登入用戶試圖登入目標之次數。
#### (11) Windows LoginFailure Line CountServerIP :
線型圖，標示出各時間段登入失敗之 Server 之登入失敗次數。
#### (12) Windows LoginFailure Datatable CountAccountType :
表格，統計登入失敗帳戶類型之登入失敗次數。
#### (13) Windows LoginFailure Pie AccountType :
圓餅圖，顯示登入失敗帳戶類型之比例。
#### (14) Windows LoginFailure Discover :
日誌索引總表 (Discover)

### 三. Windows_AccountChange
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/windows_%E5%B8%B3%E6%88%B6%E8%AA%BF%E6%95%B4.jpeg)
#### (1) Link_Windows :
快捷列，方便切換系列儀表板。
#### (2)  Windows_AccountChange Metrics 4732 :
大字報，統計已新增至啟用安全性之**本機機組**的成員數，event code : 4732。
#### (3)  Windows_AccountChange Metrics 4733 :
大字報，統計從已啟用安全性之**本機群組**中，移除的成員數，event code : 4733。
#### (4)  Windows_AccountChange Metrics 4738 :
大字報，統計已變更使用者帳戶之成員數，event code : 4738。
#### (5)  Windows_AccountChange Metrics 4729 :
大字報，統計從已啟用安全性之**全域群組**中，移除的成員數，event code : 4729。
#### (6)  Windows_AccountChange Metrics 4780 :
大字報，統計系統管理員群組中帳戶已設定ACL的的成員數，event code : 4780。
#### (7)  Windows_AccountChange Bar Code :
柱狀圖，標示時間軸上出現各 event code 的資料筆數。
#### (8)  Windows_AccountChange Datatable Code :
表格，統計 event code 與其他表格中顯示資料之相對關係。 
#### (9)  Windows_AccountChange Discover :
日誌索引總表 (Discover)
### 四. Windows_Trace
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/windows_trace.jpeg)

#### (1) Link_Windows :
快捷列，方便切換系列儀表板。
#### (2) Windows_Trace Metrics Count :
大字報，統計事件總量。
#### (3) Windows_Trace Metrics UniTask :
大字報，統計觸發事件大類別數。
#### (4) Windows_Trace Metrics 
大字報，統計 server 數量。
#### (5) Windows_Trace Metrics 
大字報，統計觸發事件種類。
#### (6) Windows_Trace Metrics UniUser :
大字報，統計 user 數量。
#### (7) Windows_Trace Datatable Server :
表格，統計 Server 與其他表格中顯示資料之相對關係。 
#### (8) Windows_Trace Bar Count :
柱狀圖，標示時間軸上各 Server 觸發事件的資料筆數。
#### (9) Windows_Trace Datatable Channel :
表格，統計事件類型與其他表格中顯示資料之相對關係。
#### (10) Windows_Trace Bar Task :
線型圖，標示事件類型在時間軸上的觸發次數。
#### (11) Windows_Trace Datatable Task :
表格，統計 Task 與其他表格中顯示資料之相對關係。
#### (12) Windows_Trace Area Task :
線型圖，標示 Task 在時間軸上的觸發次數。
#### (13) Windows_Trace Datatable EventCodeOverview :
表格，統計 Event Code 與其他表格中顯示資料之相對關係。
#### (14) Windows_Trace Bar ServerEvent :
柱狀圖，以柱狀圖表示 Server 與 Event code 的關係。
#### (15) Windows_Trace Pie Succcess :
圓餅圖，標示審核結果之比例關係。
#### (16) Windows_Trace Discover :
日誌索引總表 (Discover)

## 2. Fortigate
### ㄧ. Forti Overview
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/forti_overview.jpeg)

#### (1) Forti_Link :
快捷列，方便切換系列儀表板。
#### (2) TOP 10 來源 IP 流量分析 :
表格，統計來源 IP 與其他表格中顯示的資料(上傳、下載流量)之相對關係。
#### (3) 總流量時序圖 : 
點線區域圖，標示時間軸上對應之上傳、下載流量。
#### (4) 中毒來源 IP 分析 :
表格，統計中毒來源 IP 與其他表格中顯示資料之相對關係。
#### (5) 中毒來源 IP 分析圖 :
柱狀圖，標示時間軸上對應之中毒來源 IP 筆數。
#### (6) 訪問應用程式類型分析 :
表格，統計訪問應用程式之類型與其他表格中顯示資料之相對關係。
#### (7) 訪問應用程式類型分析圖 :
柱狀圖，標示時間軸上對應之訪問應用程式類型的筆數。
#### (8) 網址過濾來源 IP 分析 :
表格，統計來源 IP 與其他表格中顯示資料之相對關係。
#### (9) 網址過濾來源 IP 分析圖 :
柱狀圖，標示時間軸上對應之來源 IP 筆數。

### 二. Forti Traffic
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/forti_traffic.jpeg)

#### (1) Forti_Link :
快捷列，方便切換系列儀表板。
#### (2) 防火牆總流量 :
大字報，統計上傳與下載總流量。
#### (3) 來源 IP 訪問量 :
大字報，統計來源 IP 數量。
#### (4) 目標 IP 訪問量 :
大字報，統計目標 IP 數量。
#### (5) 服務器傳輸量 :
大字報，統計服務器(Service)數量。
#### (6) 總上傳流量 :
大字報，統計上傳總流量。
#### (7) 總下載流量 :
大字報，統計下載總流量。
#### (8) 總流量時序圖 :
點線區域圖，標示時間軸上對應之上傳、下載流量。
#### (9) TOP 10 來源 IP 流量分析 :
表格，統計來源 IP 與其他表格中顯示的資料(上傳、下載流量)之相對關係。
#### (10) 來源 IP 流量分析圖 :
柱狀圖，標示時間軸上對應之來源 IP 總流量。
#### (11) 目標 IP 流量分析 :
表格，統計目標 IP 流量與其他表格中顯示資料之相對關係。
#### (12) 目標 IP 流量分析圖 :
柱狀圖，標示時間軸上對應之目標 IP 總流量。
#### (13) 服務器流量分析 :
表格，統計服務器(Service)流量(上傳、下載)與其他表格中顯示資料之相對關係。
#### (14) 服務器流量分析圖 :
柱狀圖，標示時間軸上對應之服務器(Service)總流量。
#### (15) 文字雲 :
文字雲，以文字大小表示前10大 IP 來源國家。
#### (16) 文字雲 :
文字雲，以文字大小表示前10大 IP 目標國家。
#### (17) 流量等級分析 :
表格，統計流量等級。
#### (18) 流量行為分析 :
表格，統計流量行為。
#### (19) 流量行為等級分析圖 :
柱狀圖，標示時間軸上對應之行為與等級發生次數
#### (20) 傳輸協定分析 :
表格，統計協定名稱與其他表格中顯示資料之相對關係。
#### (21) Forti Traffic Discover :
日誌索引總表 (Discover)

### 三. Forti Virus
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/forti_virus.jpeg)

#### (1) Link_Windows :
快捷列，方便切換系列儀表板。
#### (2) 中毒數量 :
大字報，統計中毒次數。
#### (3) 中毒文件數量 :
#### (4) 來源 IP 數量 :
大字報，統計中毒來源 IP 數量。
#### (5) 目標 IP 數量 :
大字報，統計中毒目標 IP 數量。
#### (6) 各服務器中毒數量 :
大字報，統計各服務器中毒數量。
#### (7) 嚴重性等級分析 :
表格，統計各嚴重性等級事件發生次數。
#### (8) 事件類型分析 :
表格，統計各事件類型發生次數。
#### (9) 中毒來源 IP 分析 :
表格，統計中毒來源 IP 與其他表格中顯示資料之相對關係。
#### (10) 中毒來源 IP 分析圖 :
柱狀圖，標示時間軸上對應之中毒來源 IP 數量。
#### (11) 各服務器中毒分析圖 :
柱狀圖，標示時間軸上對應之各服務器中毒次數。
#### (12) 事件類型分析圖 :
柱狀圖，標示時間軸上對應之各事件類型發生次數。
#### (13) Forti Virus Discover
中毒日誌索引總表 (Discover)

### 四. Forti App
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/forti_application.jpeg)

#### (1) Forti_Link :
快捷列，方便切換系列儀表板。
#### (2) 訪問應用類型總數 :
大字報，統計訪問應用程式種類。
#### (3) 來源 IP : 
大字報，統計訪問應用程式之來源 IP 數量。
#### (4) 目標 IP :
大字報， 統計訪問應用程式之母標 IP 數量。
#### (5) 嚴重性等級分析 :
表格，統計訪問應用程式嚴重性與其他表格中顯示資料之相對關係。
#### (6) 訪問應用程式來源 IP 分析 :
表格，統計訪問應用程式之來源 IP 與其他表格中顯示資料之相對關係。
#### (7) 應用程式來源 IP 分析圖 :
柱狀圖，標示時間軸上對應之來源 IP 訪問應用程式次數。 
#### (8) 訪問應用程式類型分析 :
表格，統計訪問應用程式之類型與其他表格中顯示資料之相對關係。
#### (9) 訪問應用程式類型分析圖 :
柱狀圖，標示時間軸上對應之應用程式類型筆數。
#### (10) 訪問應用程式產品分析 :
表格，統計訪問應用程式之產品與其他表格中顯示資料之相對關係。
#### (11) 訪問網址分析 :
表格，統計訪問網址與其他表格中顯示的資料之相對關係。
#### (12) Forti App Discover
訪問應用程式日誌索引總表 (Discover)

### 五. Forti Webfilter
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/forti_webfilter.jpeg)

#### (1) Forti_Link :
快捷列，方便切換系列儀表板。
#### (2) 網址過濾總數 :
大字報，統計網址篩選次數。
#### (3) 來源 IP 數量 : 
大字報，統計網址篩選來源 IP 數量。
#### (4) 目標 IP 數量 : 
大字報，統計網址篩選目標 IP 數量。
#### (5) 嚴重性等級分析 :
表格，統計網址篩選事件嚴重等級與其他表格中顯示資料之相對關係。
#### (6) 嚴重性等級分析圖 :
柱狀圖，標示時間軸上網址篩選事件各嚴重等級發生次數。
#### (7) 網址過濾來源 IP 分析 :
表格，統計篩選網址來源 IP 與其他表格中顯示資料之相對關係。
#### (8) 網址過濾來源 IP 分析圖 :
柱狀圖，標示時間軸上網址篩選之來源 IP 數量。
#### (9) 網址過濾分析 :
表格，統計訪問網址與其他表格中顯示資料之相對關係。
#### (10) 網址過濾分析表 :
柱狀圖，標示時間軸上對應之過濾網址訪問次數。
#### (11) Forti Webfilter Discover
網址篩選日誌索引總表 (Discover)
### 六. Forti Trace
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/forti_trace.jpeg)

#### (1) Forti Link :
快捷列，方便切換系列儀表板。
#### (2) Forti Alert Datatable Type :
表格，統計大類別。
#### (3) Forti Alert Datatable Subtype :
表格，統計子類別。
#### (4) Forti Alert Datatable Action :
表格，統計行為。
#### (5) Forti Alert Datatable Level :
表格，統計告警等級。
#### (6) Forti Alert Datatable Eventtype :
表格，統計事件類型。
#### (7) Forti Alert Datatable SrcIP :
表格，統計來源 IP。
#### (8) Forti Alert Datatable DestIP :
表格，統計目標 IP。
#### (9) Forti Alert Datatable Service :
表格，統計服務器(Service)類型。
#### (10) Forti Alert Datatable SrcName :
表格，統計來源主機名稱。
#### (11) Forti Alert Datatable Logdesc :
表格，統計 Logdesc。
#### (12) Forti Alert Datatable Protocol :
表格，統計 Protocol。
#### (13) Forti Alert Discover :
日誌索引總表 (Discover)


## 3. Citrix
### 一. Citrix Overview
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/citrix_overview-dashboard.jpeg)

#### (1) ErrorType :
大字報，統計各錯誤類型數量。
#### (2) citrix-Total bytes received :
大字報，統計總下載流量。
#### (3) citrix-Total bytes send :
大字報，統計總上傳流量。
#### (4) citrix-Not allow to access :
大字報，統計遭拒絕登入次數。
#### (5) citrix-User allowed :
表格，統計成功登入User與其他表格中顯示資料之相對關係。
#### (6) citrix-linechart-bytes-received :
線型圖，標示時間軸上各個時間點下載的總流量。
#### (7) citrix-linechart-bytes-send :
線型圖，標示時間軸上各個時間點上傳的總流量。
## 4. Identity
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/identity-dashboard.jpeg)

#### (1) identity-total-count :
大字報，統計資料總筆數。
#### (2) identity-count-line :
線型圖，標示時間軸上各個時間點的資料筆數。
#### (3) identity-告警觸發次數 :
大字報，統計告警總觸發次數。
#### (4) identity-alert-line :
線型圖，標示時間軸上各個時間點告警觸發次數。
#### (5) identity-alert-pie :
圓餅圖，顯示各告警類別的比例分佈。
#### (6) identity-成功登入次數 :
大字報，統計成功登入次數。
#### (7) identity-登入失敗次數 :
大字報，統計登入失敗次數。
#### (8) identity-login-line :
線型圖，標示時間軸上各個時間點的成功與失敗登入次數。
#### (9) identity-login-pie :
圓餅圖，顯示登入狀態的比例分佈。
#### (10) identity-總連線數 :
大字報，統計總連線次數。
#### (11) identity-檔案異動次數 :
大字報，統計檔案異動次數(open、close)。
#### (12) identity-file-line :
線型圖，標示時間軸上各個時間點的檔案異動次數。
#### (13) identity-file-table :
表格，統計檔案異動與其他表格中顯示資料之相對關係。
#### (14) identity-connection-table :
表格，統計連線相關之各資料係數。

## 5. Nac
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/nac-dashboard.jpeg)

#### (1) nac-severity-pie :
圓餅圖，顯示事件嚴重性的比例分佈。
#### (2) nac-severity-data table :
表格，統計各嚴重性發生次數。
#### (3) nac-CVE-data_table :
表格，統計 CVE 對照各嚴重性事件的發生次數。
#### (4) nac-update item - data table :
表格，統計更新項目的更新時間。
#### (5) nac-product-data_table :
表格，統計各產品更新次數。
#### (6) nac-app status-data table :
表格，統計 app 使用狀態與其他表格中顯示資料之相對關係。
#### (7) nac-user-update item-data table :
表格，統計 user 已更新項目個數。
#### (8) nac-discover :
nac 日誌索引總表 (Discover) 

## 6. Virus
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/virus-dashboard.jpeg)

#### (1) virus_類別集 :
大字報，統計已發現風險類別集數量。
#### (2) virus_感染狀況：
圓餅圖，顯示感染狀況的比例分佈。
#### (3) virus_受感染次數 :
大字報，統計受感染次數。
#### (4) virus_類別類型 :
大字報，統計已發現風險類型。
#### (5) virus_風險名稱 :
表格，統計發現的風險名稱及發現次數。
#### (6) virus-discover :
virus 日誌索引總表 (Discover) 

## 7. Cisco
### ㄧ. Cisco Threat
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/cisco-threat.jpeg)

#### (1) ASA_Link :
快捷列，方便切換系列儀表板。
#### (2) Cisco Threat Datatable Severity :
大字報，統計各嚴重性發生次數。
#### (3) Cisco Threat Datatable BlockTimes :
大字報，統計已阻擋次數。
#### (4) Cisco Threat Datatable IPSCount :
大字報，統計觸發 IPS 次數。
#### (5) Cisco Threat Datatable IPSNotBlocked:
大字報，統計觸發 IPS 後未被阻擋次數。
#### (6) Cisco Threat Bar IPSCount :
柱狀圖，標示時間軸上對應之 IPS 觸發次數。
#### (7) Cisco Threat Bar Action :
柱狀圖，標示時間軸上對應之 Action 發生次數。
#### (8) Cisco Threat Datatable SrcIP :
表格，統計來源 IP 與其他表格中顯示資料之相對關係。
#### (9) Cisco Threat Datatable DestinationIP :
表格，統計目標 IP 與其他表格中顯示資料之相對關係。
#### (10) Cisco Threat Datatable Action :
表格，統計 Action 與其他表格中顯示資料之相對關係。
#### (11) Cisco Threat Datatable QuestionURL :
大字報，統計各類可疑 URL 發現次數。
#### (12) Cisco Threat Datatable URLReputationSrcIP :
表格，統計來源 IP 與 IPS 次數之相對關係。
#### (13) Cisco Threat Datatable URLReputationDestinationIP :
表格，統計目標 IP 與 IPS 次數之相對關係。
#### (14) Cisco Threat Datatable URLReputation :
表格，統計可疑 URL 與其他表格中顯示資料之相對關係。
#### (15) Cisco Threat Bar QuestionURL :
柱狀圖，標示時間軸上對應之可疑 URL 發生次數。
#### (16) Cisco Threat Datatable IPReputation :
表格，統計 IP 類型與其他表格中顯示資料之相對關係。
#### (17) Cisco Threat Datatable IPSICategory :
柱狀圖，標示時間軸上對應之 IPSI 類型發生次數。
#### (18) Cisco Threat Datatable ACPolicy :
表格，統計 AC Policy 與其他表格中顯示資料之相對關係。
#### (19) Cisco Threat Datatable ACRuleame :
表格，統計 AC RuleName 與其他表格中顯示資料之相對關係。

### 二. Cisco Traffic
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/cisco-traffic.jpeg)

#### (1) ASA_Link :
快捷列，方便切換系列儀表板。
#### (2) Cisco Traffic Metrics Bytes :
大字報，統計總流量、下載及上傳流量。
#### (3) Cisco Traffic Metrics UniSrcIP :
大字報，統計來源 IP 數量。
#### (4) Cisco Traffic Metrics UniDestIP :
大字報，統計目標 IP 數量。
#### (5) Cisco Traffic Metrics Application :
大字報，統計目標 Application 數量。
#### (6) Cisco Traffic Area BytesInOut :
線型圖，標示出各時間段上傳及下載流量。
#### (7) Cisco Traffic Area BytesDuration :
線型圖，標示出各時間段總流量與連線時長。
#### (8) Cisco Traffic Bar Top10DestBytes :
柱狀圖，標示時間軸上各時間段前10大目標 IP 總流量。
#### (9) Cisco Traffic Datatable sourceAddress :
表格，統計來源 IP 與其他表格中顯示資料之相對關係。
#### (10) Cisco Traffic Bar Top10SrcBytes :
柱狀圖，標示時間軸上各時間段前10大來源 IP 總流量。
#### (11) Cisco Traffic Datatable destinationAddress :
表格，統計目標 IP 與其他表格中顯示資料之相對關係。
#### (12) Cisco Traffic Bar Top10User :
柱狀圖，以柱狀圖標示前10大 User 之總流量。
#### (13) Cisco Traffic Bar Top10Application :
柱狀圖，以柱狀圖標示前10大 Application 之總流量及上傳流量。
#### (14) Cisco Traffic Bar Top10SourceCountry :
柱狀圖，以柱狀圖標示前10大來源國家之總流量及上傳流量。
#### (15) Cisco Traffic Bar Top10DestinationCountry :
柱狀圖，以柱狀圖標示前10大目標國家之總流量及上傳流量。
#### (16) Cisco Traffic Bar Map SrcCountry :
地圖，在地圖上以圖示大小及顏色表示來源國家之總流量。
#### (17) Cisco Traffic Datatable sourceCountry :
表格，統計來源國家與其他表格中顯示資料之相對關係。
#### (18) Cisco Traffic Datatable destinationCountry :
表格，統計目標國家與其他表格中顯示資料之相對關係。
#### (19) Cisco Traffic Datatable URLCategory :
表格，統計 URL 類型與其他表格中顯示資料之相對關係。
#### (20) Cisco Traffic Datatable Host :
表格，統計 Host 與其他表格中顯示資料之相對關係。
#### (21) Cisco Traffic Discover :
Cisco Traffic日誌索引總表 (Discover)

### 三.Cisco Trace
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/cisco-trace.jpeg)

#### (1) ASA_Link :
快捷列，方便切換系列儀表板。
#### (2) Cisco Trace Datatable agentType :
表格，統計產品類型與其他表格中顯示資料之相對關係。
#### (3) Cisco Trace Datatable Application :
表格，統計 Application 與其他表格中顯示資料之相對關係。
#### (4) Cisco Trace Datatable action :
表格，統計 action 與其他表格中顯示資料之相對關係。
#### (5) Cisco Trace Datatable severity :
表格，統計 severity 與其他表格中顯示資料之相對關係。
#### (6) Cisco Trace Datatable sourceAddress :
表格，統計來源 IP 與其他表格中顯示資料之相對關係。
#### (7) Cisco Trace Datatable destinationAddress :
表格，統計目標 IP 與其他表格中顯示資料之相對關係。
#### (8) Cisco Trace Datatable IPReputaion :
表格，統計 IP 類型與其他表格中顯示資料之相對關係。
#### (9) Cisco Trace Datatable HTTPResponse :
表格，統計 HTTP Response 與其他表格中顯示資料之相對關係。
#### (10) Cisco Trace Datatable Host :
表格，統計 Host 與其他表格中顯示資料之相對關係。
#### (11) Cisco Trace Datatable Reason :
表格，統計 Reason 與其他表格中顯示資料之相對關係。
#### (12) Cisco Trace Datatable URLCategory :
表格，統計 URL 類型與其他表格中顯示資料之相對關係。
#### (13) Cisco Trace Datatable URLReputation :
表格，統計 URL Reputation 與其他表格中顯示資料之相對關係。
#### (14) Cisco Trace Datatable ACPolicy :
表格，統計 AC Policy 與其他表格中顯示資料之相對關係。
#### (15) Cisco Trace Datatable ACRuleName :
表格，統計 AC RuleName 與其他表格中顯示資料之相對關係。
#### (16) Cisco Trace Datatable User :
表格，統計 User 與其他表格中顯示資料之相對關係。
#### (17) Cisco Trace Bar Bytes :
柱狀圖，標示時間軸上各時間段上傳及下載流量。
#### (18) Cisco Trace IPS Count :
柱狀圖，標示時間軸上各時間段 IPS 次數。
