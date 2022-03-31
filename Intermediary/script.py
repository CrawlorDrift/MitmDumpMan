#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File         : script.py
# @Date         : 28-12-2021
# @Author       : Payne
# @Email        : wuzhipeng1289690157@gmail.com
# @Desc:    Intercept entry
import json
from mitmproxy import ctx
from loguru import logger
from process import all_entrances

from urllib.parse import unquote
from configs import ResourceList

# def request(flow) -> None:
#     """Before request Transfer
#     :param flow:
#     :return:
#     """
#     ctx.log.info(str(flow.request.url))
#     ctx.log.info(str(flow.request.method))
#     ctx.log.info(str(flow.request.path))


def response(flow) -> None:
    """response Intercept processing
    :param flow:
    :return:
    """
    for source in ResourceList.keys():
        if ResourceList.get(source) in flow.request.url:
            body = unquote(flow.response.text)
            data = json.loads(body)
            results = data["data"]["items"] or []
            logger.info(f"First UserId: {results[0]['note']['id']} Processing...: ")
            all_entrances(source, results)
