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

### 新增源步骤

1. config.py中增加{"资源名称":"符合urn字段"}
2. Process 中新增策略,以及对应处理逻辑

## RUN

```bash
mitmdump -s DumpMan/script.py -p 8888
```