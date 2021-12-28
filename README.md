# MitmDumpMan

MitmDumpMan is a forward middleware

## requirement 

python >= 3.6

mitmproxy

```bash
python3 -m pip install -Ur requirements.txt
```

### File Tree 

```text
.
├── MitmDumpMan
│   ├── Process.py  # 处理策略工厂类
│   ├── config.py   # 配置文件
│   └── script.py   # mitmdump 处理脚本
├── README.md
├── requirements.txt
└── supervisord.conf
```

新增源步骤

1. config.py中增加