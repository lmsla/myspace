# MA003 - indice 格式大小

## indices 容量計算：

- 計算方式以日為單位，並以容量單位：gb 為主 
- logstash-ltm  : 目前每日平均約 2.5gb
- logstash-paloalto : 目前每日平均約 13.4gb
- 目前加總每日平均約 40gb
- 硬碟總容量為 : 1000gb x 80% = 800gb (設定 80% 保存上限)
- 800 / 16 = 50 (建議保存天數)

## cat indices：

- 在 Dev Tools 介面下執行下列命令：

```
GET _cat/indices?v&s=index
```
```
health status index                           uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   logstash-ltm-20211126           iT2lXKoZTtmT73U9YSpHfQ   1   1      41534            0      3.7mb          3.7mb
yellow open   logstash-ltm-20211127           uP8eX0qzQQ6mAwJzmCtGSw   1   1      65222            0      5.6mb          5.6mb
yellow open   logstash-ltm-20211128           lcQ87pOUSG-PCaA-FgcZJQ   1   1      65760            0      5.6mb          5.6mb
yellow open   logstash-ltm-20211129           _-tHQC-WQ-GpItfQYUbfXA   1   1      67089            0      5.7mb          5.7mb
yellow open   logstash-ltm-20211130           fFzAZuMWR4i6XbLcQ4wRCw   1   1      72615            0      6.4mb          6.4mb
yellow open   logstash-ltm-20211201           ww4RajfkSQOp6y5_GIzXvg   1   1      92692            0      8.5mb          8.5mb
yellow open   logstash-ltm-20211202           6LhPJQTDR6O5bSGABNwqwA   1   1      86138            0      7.7mb          7.7mb
yellow open   logstash-ltm-20211203           HeLSufchQP23asiwtidirA   1   1      72784            0      6.3mb          6.3mb
yellow open   logstash-ltm-20211204           eVJX1iIbRRqobrfm5Fy6gA   1   1      67465            0      5.7mb          5.7mb
yellow open   logstash-ltm-20211205           kLps1OWQRYuSqzCt9hIBeA   1   1      68690            0      5.8mb          5.8mb
yellow open   logstash-ltm-20211206           Du9EnZoQTeCQ6zoS3uyyPw   1   1      78913            0        7mb            7mb
yellow open   logstash-ltm-20211207           fRvMW3ooSoaRVkpvB_id3A   1   1      70765            0        6mb            6mb
yellow open   logstash-ltm-20211208           1EdaKSNgQQ6dSQWh7d0jjQ   1   1      96105            0      8.7mb          8.7mb
yellow open   logstash-ltm-20211209           wgqIm_fMSS2du8vF3zWqvQ   1   1     664876            0    118.5mb        118.5mb
yellow open   logstash-ltm-20211210           M9uUdg1tTi2oPjz2967LDQ   1   1     911344            0    177.1mb        177.1mb
yellow open   logstash-ltm-20211211           chkXCvHrS0OLeeh2ODHBPQ   1   1     191888            0     29.5mb         29.5mb
yellow open   logstash-ltm-20211212           2MIOORlTT0K_berJ_CzwQA   1   1     169555            0     26.1mb         26.1mb
yellow open   logstash-ltm-20211213           saBi4Vf9QAaM-Di05rcG7Q   1   1    1045853            0    371.1mb        371.1mb
yellow open   logstash-ltm-20211214           G7084Ev6RGaRRSl1R0vWiQ   1   1    1040933            0    632.3mb        632.3mb
yellow open   logstash-ltm-20211215           38Y9V9WxQzqPLWuNYhO16Q   1   1    1036768            0    629.4mb        629.4mb
yellow open   logstash-ltm-20211216           tGEOiBcLTbOTGyvJ0Jf9qw   1   1    1146496            0    694.5mb        694.5mb
yellow open   logstash-ltm-20211217           JGd8G6d3R3SPtV_RYPMITw   1   1     985247            0    606.3mb        606.3mb
yellow open   logstash-ltm-20211218           08xRf8gERO6ZQ86DlP7kVA   1   1     184231            0     86.5mb         86.5mb
yellow open   logstash-ltm-20211219           qZ4keZRhSqyeW3txRajDjQ   1   1     181722            0     83.1mb         83.1mb
yellow open   logstash-ltm-20211220           M2ppcbqdSBKmrfmdn6Kn5Q   1   1    1102330            0      674mb          674mb
yellow open   logstash-ltm-20211221           TF-ZyZYRSISX7ICB_i08Tw   1   1    1107578            0    680.2mb        680.2mb
yellow open   logstash-ltm-20211222           LUbYBSqvTlOxznpCpTav-A   1   1    1489343            0      879mb          879mb
yellow open   logstash-ltm-20211223           wiXQZrk3RHKTBjuCC0bfBA   1   1    5396999            0      3.1gb          3.1gb
yellow open   logstash-ltm-20211224           Jt1yGeLBSSWUOnVb_4c7Vg   1   1    5557975            0      3.2gb          3.2gb
yellow open   logstash-ltm-20211225           HumQk-kQTYaGlzW9TxnuQg   1   1    2762569            0      1.4gb          1.4gb
yellow open   logstash-ltm-20211226           1DaD0Zz-QfyM5upuTWZPKw   1   1    2646123            0      1.3gb          1.3gb
yellow open   logstash-ltm-20211227           R5ZSjfh4QkSEApABFontzg   1   1    4934809            0      2.9gb          2.9gb
yellow open   logstash-ltm-20211228           0Xs7LY6FQ7ivfL7r2pbf8A   1   1    5595371            0      3.2gb          3.2gb
yellow open   logstash-ltm-20211229           F3GSZepISiW0-rF03N9ixQ   1   1    5766912            0      3.3gb          3.3gb
yellow open   logstash-ltm-20211230           xvoXme5xRWetAOpf3kpmxQ   1   1    2859646            0      1.7gb          1.7gb
yellow open   logstash-paloalto-20211111      bpv5WItiQaeEdj9gmxxLZQ   1   1    7193412            0      5.7gb          5.7gb
yellow open   logstash-paloalto-20211112      EC1i3Le_QweXBuDNQjs3jw   1   1    8741226            0      6.9gb          6.9gb
yellow open   logstash-paloalto-20211113      LjXfR1WbR7-fuF5Dmy34yQ   1   1    6485061            0      4.9gb          4.9gb
yellow open   logstash-paloalto-20211114      ZfA6J_DiRWaxOaphG4eTSw   1   1    6024722            0      4.6gb          4.6gb
yellow open   logstash-paloalto-20211115      -Oxcp55dSAWG2VlyXgDrWw   1   1    8371262            0      6.6gb          6.6gb
yellow open   logstash-paloalto-20211116      6R6oT2-vTaGjXD-ObK6wBA   1   1    8678852            0      6.9gb          6.9gb
yellow open   logstash-paloalto-20211117      f3Rv-2ARTPiN8NS-I5RU9g   1   1   19842391            0     15.1gb         15.1gb
yellow open   logstash-paloalto-20211118      qzYvr9FETU6dQKkO26xZ8w   1   1   45862866            0     33.8gb         33.8gb
yellow open   logstash-paloalto-20211119      YZ2TzAhaSk6u3hkOtH4ViQ   1   1   17226853            0     12.8gb         12.8gb
yellow open   logstash-paloalto-20211120      QI2N5xkfQPC3WFIsL_vX7A   1   1   45933865            0     33.1gb         33.1gb
yellow open   logstash-paloalto-20211121      q4BCNjDoSb-kC0RQKsBYmA   1   1   36178496            0     26.2gb         26.2gb
yellow open   logstash-paloalto-20211122      Mn1KGgqSRvWWZlG9gYhlCQ   1   1   18525296            0     14.1gb         14.1gb
yellow open   logstash-paloalto-20211123      dWLMgXJGQOCJXiSYoarZ4w   1   1   46916696            0     34.9gb         34.9gb
yellow open   logstash-paloalto-20211124      wr_6KVLjRfSRu7xX02bKKg   1   1   43115242            0     31.2gb         31.2gb
yellow open   logstash-paloalto-20211125      keobsA0QQoW6oxKr6LBhfA   1   1   19577561            0     14.8gb         14.8gb
yellow open   logstash-paloalto-20211126      9LphPQ9fSfSGMorozRZwKQ   1   1   17758876            0     13.6gb         13.6gb
yellow open   logstash-paloalto-20211127      wGligBd8QuuH-7WfFdfjYw   1   1    6432163            0      4.8gb          4.8gb
yellow open   logstash-paloalto-20211128      G4yXnc-ITWWtL0dECvlHzw   1   1   20406839            0     14.7gb         14.7gb
yellow open   logstash-paloalto-20211129      hEw0fuqFTi2GXFgvVX2YcQ   1   1    7910234            0      6.2gb          6.2gb
yellow open   logstash-paloalto-20211130      R7uuGhhIRi6HbOreEUIdoA   1   1    8026705            0      6.3gb          6.3gb
yellow open   logstash-paloalto-20211201      946S7QoWQKm-KJ74QORBtQ   1   1    7621466            0        6gb            6gb
yellow open   logstash-paloalto-20211202      mvDsOZ2kRJiqr7_PftLXOw   1   1   10591873            0      8.2gb          8.2gb
yellow open   logstash-paloalto-20211203      XZuj3iHiTPKtNKw2sMhX2w   1   1   22839205            0     17.2gb         17.2gb
yellow open   logstash-paloalto-20211204      C2fXzJiLRbS8AljdpHFzJA   1   1   52962883            0     37.1gb         37.1gb
yellow open   logstash-paloalto-20211205      Yp-XhmmOR5er3CLNgEeBjw   1   1   75135187            0     51.7gb         51.7gb
yellow open   logstash-paloalto-20211206      1uXu-lu1RGia-SpI5bAnLA   1   1   38619238            0     28.1gb         28.1gb
yellow open   logstash-paloalto-20211207      wvfDB0XKRxqMvXuwDueugg   1   1   53154962            0     38.5gb         38.5gb
yellow open   logstash-paloalto-20211208      sZwQhIt0Q4atJ3cDkIk6Ew   1   1   71665047            0     46.6gb         46.6gb
yellow open   logstash-paloalto-20211209      JRf3aerGR024Vf4vPjn0BQ   1   1   30983193            0     18.6gb         18.6gb
yellow open   logstash-paloalto-20211210      tWAEVGLHQA2huM_dIhRM3A   1   1    7810542            0        6gb            6gb
yellow open   logstash-paloalto-20211211      y9Jc4-qXQnGabR6nc6P07w   1   1    5914481            0      4.4gb          4.4gb
yellow open   logstash-paloalto-20211212      gFL75u0MQKqb-S5RtxEbjQ   1   1    5350788            0      3.9gb          3.9gb
yellow open   logstash-paloalto-20211213      npY9Q45MQ8G3mqny9_7_dw   1   1    7774350            0      6.1gb          6.1gb
yellow open   logstash-paloalto-20211214      WIzDh30oQYWDPUl0tpHDcg   1   1   14306099            0     10.1gb         10.1gb
yellow open   logstash-paloalto-20211215      pIbWCsxaQ6m3t47XmUIKzw   1   1   10622396            0      7.5gb          7.5gb
yellow open   logstash-paloalto-20211216      1DN55sJHT-KXFc6GXT1ROA   1   1    8142317            0      6.4gb          6.4gb
yellow open   logstash-paloalto-20211217      qOfzIDCMRuCEx5W9V9yltw   1   1    7622043            0        6gb            6gb
yellow open   logstash-paloalto-20211218      qPMwSTPyT2KxTqdA4eJGBw   1   1    5315264            0        4gb            4gb
yellow open   logstash-paloalto-20211219      udtjbQYHSdmy6a7VV-EM-g   1   1    4950930            0      3.7gb          3.7gb
yellow open   logstash-paloalto-20211220      PxAloLioRIC1yJjE7SBjuA   1   1    7580215            0      5.9gb          5.9gb
yellow open   logstash-paloalto-20211221      dMleJV6wQWKpI_x00ttOQg   1   1    7676893            0        6gb            6gb
yellow open   logstash-paloalto-20211222      nzjtX-FfQzOZBmVJ6h_2eA   1   1    7600838            0        6gb            6gb
yellow open   logstash-paloalto-20211223      szfoPPBWQcGuEP6hGHhDRQ   1   1    7974370            0      6.3gb          6.3gb
yellow open   logstash-paloalto-20211224      fdPJ4MFWQaOt0u2UzPXIhg   1   1    8255207            0      6.5gb          6.5gb
yellow open   logstash-paloalto-20211225      jIgRb_SOTM-Wj_T2VIXwKg   1   1    5708812            0      4.3gb          4.3gb
yellow open   logstash-paloalto-20211226      ZyF3juWZSSqlGS4RaFDsJg   1   1    5251294            0      3.9gb          3.9gb
yellow open   logstash-paloalto-20211227      hnDt-Qq4T7Ki3VrlnahbRA   1   1    7785144            0      6.1gb          6.1gb
yellow open   logstash-paloalto-20211228      uUPbKU12TpGE7M3-qx5IMg   1   1    7976863            0      6.3gb          6.3gb
yellow open   logstash-paloalto-20211229      nZjY_ZrNRZCl9fRGykYwpA   1   1    8364082            0      6.6gb          6.6gb
yellow open   logstash-paloalto-20211230      ZrKs9QudQLa9OO5IZrgWXA   1   1    3507029            0      3.2gb          3.2gb
yellow open   logstash-waf-20211126           GpJVspktQT2eAqY2YofCww   1   1        149            0      391kb          391kb
yellow open   logstash-waf-20211127           XGHY7R5vSNG0NtdMJyBB7A   1   1        206            0      459kb          459kb
yellow open   logstash-waf-20211128           zWDfU5KRR7WF2ehHIZXeiQ   1   1        189            0    365.6kb        365.6kb
yellow open   logstash-waf-20211129           y5sBg8oIQBqqJimNzcvvww   1   1        536            0    862.4kb        862.4kb
yellow open   logstash-waf-20211130           4tjFbPrjRiGokZ6lteNYQA   1   1        671            0    954.4kb        954.4kb
yellow open   logstash-waf-20211201           0lNt8SfWRxWo2TOo8JtnhQ   1   1        356            0      1.6mb          1.6mb
yellow open   logstash-waf-20211202           VFj57DxtRCm6_pnqsjp6bA   1   1        433            0      2.6mb          2.6mb
yellow open   logstash-waf-20211203           x14wF3qRRoWSkP030xmGjw   1   1        423            0      1.7mb          1.7mb
yellow open   logstash-waf-20211204           IHqBI5uzTMyVIXIzsg6HIQ   1   1        112            0    675.2kb        675.2kb
yellow open   logstash-waf-20211205           iygAhai9Qdujq9V1nO-gbw   1   1        163            0      1.2mb          1.2mb
yellow open   logstash-waf-20211206           GIxu893YSAyegL3zxFX-ig   1   1        353            0      1.8mb          1.8mb
yellow open   logstash-waf-20211207           uwNGqlJYS-e1AS0lrqXWnQ   1   1        429            0      2.8mb          2.8mb
yellow open   logstash-waf-20211208           0Fdz7a80SVO3xhq9SaGsSg   1   1        440            0      1.8mb          1.8mb
yellow open   logstash-waf-20211209           RBQAHBndR--nYpUrlfzLvA   1   1     155968            0     37.1mb         37.1mb
yellow open   logstash-waf-20211210           syqmnJZLSHaYQWnMSK1qQQ   1   1        516            0        3mb            3mb
yellow open   logstash-waf-20211211           gBvfh3poRtqOSn93Ags-Rw   1   1        207            0        1mb            1mb
yellow open   logstash-waf-20211212           4ccKCPZlQCWXPokjIPbUng   1   1        152            0    628.5kb        628.5kb
yellow open   logstash-waf-20211213           kMl5UUGcTruwXwjyaHJjpw   1   1        614            0      4.1mb          4.1mb
yellow open   logstash-waf-20211214           bIXmgahfTt2S-_9kU9mKlg   1   1        560            0        2mb            2mb
yellow open   logstash-waf-20211215           6p0wI309RY2GArjr5FJjFg   1   1        874            0      3.2mb          3.2mb
yellow open   logstash-waf-20211216           l9SN6eQAQFW2dK6LCkqC6g   1   1        720            0      4.2mb          4.2mb
yellow open   logstash-waf-20211217           YyZEFzPcTCi1a0yphiEJDg   1   1        644            0      2.6mb          2.6mb
yellow open   logstash-waf-20211218           918Ya8UZRcyLAlfDZWih-Q   1   1        355            0        1mb            1mb
yellow open   logstash-waf-20211219           NMf_tGFaSRGMw2qr7GNznw   1   1        625            0      1.4mb          1.4mb
yellow open   logstash-waf-20211220           0D1I5HmlSMag2RNttL5K4A   1   1        666            0      4.7mb          4.7mb
yellow open   logstash-waf-20211221           Kt0vZoz7TPCeSoPK52MDxA   1   1        755            0      3.2mb          3.2mb
yellow open   logstash-waf-20211222           N7vpiwmpSsmqZvrz2wk59g   1   1        711            0      3.9mb          3.9mb
yellow open   logstash-waf-20211223           cckNc3U1SbmKeKP2zxyZvw   1   1        624            0      4.2mb          4.2mb
yellow open   logstash-waf-20211224           JVwW7bx2R02BFm906kvLeg   1   1        561            0      2.5mb          2.5mb
yellow open   logstash-waf-20211225           k-xlDiaURmCCQmaQBhZ5TQ   1   1        274            0        1mb            1mb
yellow open   logstash-waf-20211226           nC7lTWmWTKy5NBZ28KZqPQ   1   1        235            0    777.1kb        777.1kb
yellow open   logstash-waf-20211227           Ow_8j1ouTOqUtiMqJbEf2w   1   1        662            0      2.8mb          2.8mb
yellow open   logstash-waf-20211228           8MhQrQJ1SPS_VZcdlgJXrw   1   1        573            0      3.3mb          3.3mb
yellow open   logstash-waf-20211229           q7HT5rMWQSmyW8L_5wV8iQ   1   1       1350            0      5.6mb          5.6mb
yellow open   logstash-waf-20211230           jt0tsTGuRhK9VZslc0PeGg   1   1        282            0        2mb            2mb
yellow open   logstash-winlogbeat-20211116    KQUkZCTkTua6RG4abIl5Kw   1   1       6707            0      5.5mb          5.5mb
yellow open   logstash-winlogbeat-20211117    s4WAchh2T7-rSAEMvvvJ4g   1   1       7588            0      6.1mb          6.1mb
yellow open   logstash-winlogbeat-20211118    vjpwAsDASraKNQPdQi6_4A   1   1       7632            0        6mb            6mb
yellow open   logstash-winlogbeat-20211119    jtwsNbNGR4SAf36SKsFwaw   1   1       8462            0      7.7mb          7.7mb
yellow open   logstash-winlogbeat-20211120    vSRUByAaRX2pGcStOsL0DQ   1   1       8041            0      7.1mb          7.1mb
yellow open   logstash-winlogbeat-20211121    IRm5VpnMRnCA1nAIJKxMNQ   1   1       8177            0      7.7mb          7.7mb
yellow open   logstash-winlogbeat-20211122    n0mOao0YTH-U7cPXvcxsCA   1   1     187099            0    137.2mb        137.2mb
yellow open   logstash-winlogbeat-20211123    W1sWeeFOSYSHpXKNKNo7wA   1   1     280834            0    201.1mb        201.1mb
yellow open   logstash-winlogbeat-20211124    z-D5jB-4SN-8njS9f9xq6Q   1   1     279064            0    197.1mb        197.1mb
yellow open   logstash-winlogbeat-20211125    SlFACn8jTIitwB6UBs4mOw   1   1     289823            0    292.4mb        292.4mb
yellow open   logstash-winlogbeat-20211126    q5l1i71BTH-IGJ-K0Trn8Q   1   1     290080            0    309.8mb        309.8mb
yellow open   logstash-winlogbeat-20211127    3N7QRdgxSmaA8xLHmm5bcA   1   1     230542            0    252.2mb        252.2mb
yellow open   logstash-winlogbeat-20211128    nC7UNsnvQumaFT1S2ysbXg   1   1     233493            0    254.8mb        254.8mb
yellow open   logstash-winlogbeat-20211129    rwDiBIclQm2JhxQJxDZQeA   1   1     283303            0    303.3mb        303.3mb
yellow open   logstash-winlogbeat-20211130    Quc6y7O-QsGhcWv2WaC0OQ   1   1     290012            0    310.9mb        310.9mb
yellow open   logstash-winlogbeat-20211201    GVxGGrRGRJenHHRmdm-uLQ   1   1     478352            0    446.9mb        446.9mb
yellow open   logstash-winlogbeat-20211202    XQ2beYxuTteZfUXS45CNsA   1   1     313463            0    322.8mb        322.8mb
yellow open   logstash-winlogbeat-20211203    hFoa-H3RSCOX63pf23NYJA   1   1     282060            0    310.2mb        310.2mb
yellow open   logstash-winlogbeat-20211204    EDcYsxMkSkypQA9Le0Z5Ew   1   1     264514            0    302.8mb        302.8mb
yellow open   logstash-winlogbeat-20211205    6CBS8Q5wQjqi7TARc2MYkw   1   1     263769            0    301.9mb        301.9mb
yellow open   logstash-winlogbeat-20211206    1iKpzIHuTG6tIzSBPZUZeQ   1   1     312986            0    354.2mb        354.2mb
yellow open   logstash-winlogbeat-20211207    RrwD_v2SRX6JIIItWauEjA   1   1     325524            0    368.8mb        368.8mb
yellow open   logstash-winlogbeat-20211208    QtvWWa8CThityp_ix3MWPA   1   1     335890            0    383.6mb        383.6mb
yellow open   logstash-winlogbeat-20211209    Az5TkQwCTI68LummhhFqvw   1   1     339954            0    390.1mb        390.1mb
yellow open   logstash-winlogbeat-20211210    K6sdMGcESAij_MUCFBUqOA   1   1     335023            0    387.5mb        387.5mb
yellow open   logstash-winlogbeat-20211211    Qvsl-vKsQcSdjGO9oRA8hQ   1   1     284095            0    336.9mb        336.9mb
yellow open   logstash-winlogbeat-20211212    G1hDbbfTSpaxDXyMz_8hJA   1   1     288142            0    341.1mb        341.1mb
yellow open   logstash-winlogbeat-20211213    w3HHb0MTQsKUkiGZGzS-lg   1   1     340501            0    394.5mb        394.5mb
yellow open   logstash-winlogbeat-20211214    bW9QKDFaR3C-TnTSRcZyJA   1   1     600944            0    575.1mb        575.1mb
yellow open   logstash-winlogbeat-20211215    XWBjt031S5ifwR_YgLGxmg   1   1     341755            0    393.9mb        393.9mb
yellow open   logstash-winlogbeat-20211216    KHA8qXgvSnWdQE6E2jRjxg   1   1     382926            0      427mb          427mb
yellow open   logstash-winlogbeat-20211217    0L8UkidrSSifktC1zQ9WiQ   1   1     343287            0    393.8mb        393.8mb
yellow open   logstash-winlogbeat-20211218    oHRAw1KBSUuB1fVkAql7PA   1   1     289600            0    340.5mb        340.5mb
yellow open   logstash-winlogbeat-20211219    RNIaJCxARum4BNIhtoeKmg   1   1     290611            0    341.9mb        341.9mb
yellow open   logstash-winlogbeat-20211220    H86bkjffQ6aeZ5g-ydmPvQ   1   1     347903            0      394mb          394mb
yellow open   logstash-winlogbeat-20211221    hnqo0A37TG6exthKP6lorw   1   1     373150            0    422.1mb        422.1mb
yellow open   logstash-winlogbeat-20211222    vFbb_ioVS2qAaZsYc_B88w   1   1     385832            0    427.9mb        427.9mb
yellow open   logstash-winlogbeat-20211223    L3vUUFWFRteI-6YhPcX30g   1   1     371104            0    411.8mb        411.8mb
yellow open   logstash-winlogbeat-20211224    ARHd6BWHQoyYxudAAS1_WQ   1   1     382093            0    420.5mb        420.5mb
yellow open   logstash-winlogbeat-20211225    UuIMm_5rQRyfqWwydNXXqQ   1   1     304708            0      342mb          342mb
yellow open   logstash-winlogbeat-20211226    tE4xRmroQICbhhmKbh6Hww   1   1     300149            0    339.7mb        339.7mb
yellow open   logstash-winlogbeat-20211227    954Ga0FtQHuERqCdfARv9g   1   1     359931            0    395.6mb        395.6mb
yellow open   logstash-winlogbeat-20211228    kivfzMUQTGS7iqR3V0PG4Q   1   1     447203            0      465mb          465mb
yellow open   logstash-winlogbeat-20211229    meAH7j53RwCTmimjk7vdDg   1   1     461774            0      465mb          465mb
yellow open   logstash-winlogbeat-20211230    aS07PxSyQ0mKh7cHg7S56w   1   1     154072            0    160.2mb        160.2mb
```


