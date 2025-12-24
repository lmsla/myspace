# MA005 - Mount Disk 操作手冊 

***
註：</br>
**192.168.101.xxx** - Nas 主機位置</br>
**/volume1/data_storage** - Nas上可供掛載的硬碟位置</br>
**/data/es_snapshot** - 本機要掛載至 Nas 的資料夾
***

### 1 . 確認 Nas 上可供掛載的硬碟位置

```
showmount -e 192.168.101.xxx
```
### 2 . 指定連結至 Nas 上的本機資料夾位置

```
mkdir /data
mkdir /data/es_snapshot
```

### 3 . 若缺少必須套件， 須安裝 nfs-common

```
sudo apt install nfs-common
```
### 4 . 編輯 fstab

```
vim /etc/fstab
```

```
加入：

192.168.101.xxx:/volume1/data_storage /data/es_snapshot nfs defaults 0 0
```

### 5 . 掛載 disk

```
mount /data/es_snapshot
```




