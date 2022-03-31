# Intermediary

Intermediary is a forwarding middleware based on the specific implementation 
of mitmdump, use it can Easily automate grabs

## requirements

python >= 3.7

mitmproxy

```bash
python3 -m pip install -Ur requirements.txt
```

## File Tree

```text
.
├── Intermediary
│ ├── Process.py  # 处理策略工厂类
│ ├── config.py   # 配置文件
│ └── script.py   # mitmdump 处理脚本
├── README.md
├── requirements.txt
└── supervisord.conf
```

### Add new resource

1. first: You need edit  `Intermediary/config.py`, add some target resouce message in ResourceList Field
2. Sencond: add new Strategy and process logic

## RUN

```bash
# Base run
mitmdump -s DumpMan/script.py -p 8088
# Background run
mitmdump -s DumpMan/script.py -p 8088 > /dev/null 2>&1 &
# nohop
nohup mitmdump -s DumpMan/script.py -p 8088 > out.log 2>&1 &
```

### check Task

```bash 
# check jobs 
jobs -l
# check netstat
netstat -ntlp
# check Port occupancy
lsof -i:8090 
```

## TODO

Docker、Kubernetes 
