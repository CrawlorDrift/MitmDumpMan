# MitmDumpMan

MitmDumpMan is a forward middleware

## requirements

python >= 3.6

mitmproxy

```bash
python3 -m pip install -Ur requirements.txt
```

## File Tree

```text
.
├── DumpMan
│   ├── Process.py  # 处理策略工厂类
│   ├── config.py   # 配置文件
│   └── script.py   # mitmdump 处理脚本
├── README.md
├── requirements.txt
└── supervisord.conf
```

### add new resource 

1. first: You need edit  `DumpMan/config.py`, add some target resouce message in ResourceList Field
2. Sencond: add new Strategy and process logic

## RUN

```bash
# Base run
mitmdump -s DumpMan/script.py -p 8888
# Background run
nohub mitmdump -s DumpMan/script.py -p 8888 &
# Abandon the log to run in the background
nohub mitmdump -s DumpMan/script.py -p 8888 >> /usr/local/node/output.log 2>&1 &
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
