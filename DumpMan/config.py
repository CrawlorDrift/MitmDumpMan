#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File         : config.py
# @Date         : 28-12-2021
# @Author       : Payne
# @Email        : wuzhipeng1289690157@gmail.com
# @Desc:
from typing import AnyStr, List, Dict
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
    "xiaohongshu": "xiaohongshu.com/api/sns/v10/search/notes"
}
KeyWord: List[AnyStr] = []
MySQLClientParam: Dict = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123123',
    'database': '',
}
