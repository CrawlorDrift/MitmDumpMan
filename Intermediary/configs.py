#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File         : configs.py
# @Date         : 28-12-2021
# @Author       : Payne
# @Email        : wuzhipeng1289690157@gmail.com
# @Desc:
from typing import AnyStr, List, Dict
from environs import Env
from loguru import logger
from os.path import dirname, abspath, join

env = Env()
env.read_env()

# definition of dirs
ROOT_DIR = dirname(dirname(abspath(__file__)))

# definition of environments
DEV_MODE, TEST_MODE, PROD_MODE = "dev", "test", "prod"
APP_ENV = env.str("APP_ENV", DEV_MODE).lower()
APP_DEBUG = env.bool("APP_DEBUG", True if APP_ENV == DEV_MODE else False)
APP_DEV = IS_DEV = APP_ENV == DEV_MODE
APP_PROD = IS_PROD = APP_ENV == PROD_MODE
APP_TEST = IS_TEST = APP_ENV == TEST_MODE

# logs config
ENABLE_LOG_FILE = env.bool("ENABLE_LOG_FILE", True)
ENABLE_LOG_RUNTIME_FILE = env.bool("ENABLE_LOG_RUNTIME_FILE", True)
ENABLE_LOG_ERROR_FILE = env.bool("ENABLE_LOG_ERROR_FILE", True)

LOG_DIR = join(ROOT_DIR, env.str("LOG_DIR", "Logs"))

LOG_LEVEL_MAP = {DEV_MODE: "DEBUG", TEST_MODE: "INFO", PROD_MODE: "ERROR"}

LOG_LEVEL = LOG_LEVEL_MAP.get(APP_ENV)

if ENABLE_LOG_FILE:
    if ENABLE_LOG_RUNTIME_FILE:
        logger.add(
            env.str("LOG_RUNTIME_FILE", join(LOG_DIR, "runtime.log")),
            level=LOG_LEVEL,
            enqueue=True,
            rotation="1 week",
            retention="20 days",
        )
    if ENABLE_LOG_ERROR_FILE:
        logger.add(
            env.str("LOG_ERROR_FILE", join(LOG_DIR, "error.log")),
            level="ERROR",
            enqueue=True,
            rotation="1 week",
        )

# from environs import Env
# env = Env()

# Filter URL
# ResourceList: Dict = env.dict('URLS', {
#     "xiaohongshu": "xiaohongshu.com/api/sns/v10/search/notes"
# })

# Search key word List
# KeyWord: List[AnyStr] = env.list('KeyWord', [])

# Mysql Client Param
# MySQLClientParam: Dict = env.dict('MySQLClient', {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'password': '123123',
#     'database': '',
# })

ResourceList: Dict = {
    "xhs_lv": "xiaohongshu.com/api/sns/v10/search/notes"
    # "xhs_search": "xiaohongshu.com/api/sns/v10/search/notes"
}

MySQLClientParam: Dict = {
    "host": "10.21.200.48",
    "port": 3306,
    "user": "opinion",
    "password": "vDGM0lspmy=",
    "database": "opinion",
}
