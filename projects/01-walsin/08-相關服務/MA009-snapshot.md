# MA009 - snapshot 


## Step 1 . Register a repository

#### 1.
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/snapshot-Register_a_repository.png)
#### 2.
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/snapshot-Register_a_repository2.png)

#### 3. elasticsearch.yml 中必須先設定存放 snapshot 的路徑
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/ES_Yaml.PNG)
#### 4. 將上一步設定的路徑輸入 Location 後，點選下方 Register
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/snapshot-Register_a_repository3.png)


## Step 2 . Create policy

#### 1.Logistics
- Snapshot name 日期設定規則：
	- now/d-1d 取前一天的日期
	- now-1d/M 本月第一天
- Schedule : 設定什麼時候做 snapshot
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/SnapShot01.PNG)

#### 2.Snapshot settings
- Data stream and indices:
	- 指定要做 snapshot 的 index patterns 時間設定規則與上步驟的 Snapshot name 相同。
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/SnapShot02.PNG)

<logstash-firewall-fortigate-walsin-*{now-1d{yyyy_MM_dd}}>
#### 3.Snapshot retention 

![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/SnapShot03.PNG)

#### 4. 順利執行後，會產生新的 snapshot 在 Snapshots 清單下
![](https://gitlab.bimap.co/maintain/walsin/-/raw/main/images/SnapShot04.PNG)
