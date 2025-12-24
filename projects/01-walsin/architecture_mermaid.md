```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#ff9900', 'edgeLabelBackground':'#1f2020', 'tertiaryColor': '#1f2020', 'mainBkg': '#1f2020', 'clusterBkg': '#1f2020', 'clusterBorder': '#666', 'lineColor': '#888'}}}%%
graph LR
    subgraph Equipment ["設備層 (Equipment Layer)"]
        direction TB
        FW[Firewall / WAF]:::orange
        AD[Active Directory]:::orange
        Cisco[Cisco Network]:::orange
        Win[Windows Servers]:::orange
        DB_Src[MSSQL]:::orange
    end

    subgraph Ingestion ["採集層 (Ingestion Layer)"]
        direction TB
        Logstash[Logstash Cluster<br/>(Normalization & Parsing)]:::blue
    end

    subgraph Storage ["數據儲存層 (Data Storage Layer)"]
        direction TB
        ES[Elasticsearch Cluster<br/>(Hot/Warm Architecture)]:::darkblue
    end

    subgraph Visualization ["視覺化監控層 (Visualization Layer)"]
        direction TB
        Kibana(Kibana):::grafana
        D1[威脅監控 Threat Mon.]:::purple
        D2[流量分析 Traffic Ana.]:::purple
        D3[身份識別 Identity Mgmt]:::purple
        D4[維運管理 Operations]:::purple
    end

    %% Connections
    FW --> Logstash
    AD --> Logstash
    Cisco --> Logstash
    Win --> Logstash
    DB_Src --> Logstash

    Logstash ==> ES

    ES ==> Kibana

    Kibana -.-> D1
    Kibana -.-> D2
    Kibana -.-> D3
    Kibana -.-> D4

    %% Styling Classes
    classDef orange fill:#ff9900,stroke:#333,stroke-width:2px,color:white,rx:5,ry:5;
    classDef blue fill:#007acc,stroke:#333,stroke-width:2px,color:white,rx:5,ry:5;
    classDef darkblue fill:#1a237e,stroke:#5c6bc0,stroke-width:2px,color:white,shape:cylinder;
    classDef purple fill:#7b1fa2,stroke:#ba68c8,stroke-width:2px,color:white,rx:10,ry:10;
    classDef grafana fill:#f57f17,stroke:#ffb74d,stroke-width:2px,color:white,shape:circle;

    %% Subgraph Styling
    style Equipment fill:#1f2020,stroke:#666,stroke-width:1px,color:#ddd
    style Ingestion fill:#1f2020,stroke:#666,stroke-width:1px,color:#ddd
    style Storage fill:#1f2020,stroke:#666,stroke-width:1px,color:#ddd
    style Visualization fill:#1f2020,stroke:#666,stroke-width:1px,color:#ddd
```
