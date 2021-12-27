from MitmDumpMan.config import *
from MitmDumpMan.Process import AllEntrances
import json
from urllib.parse import unquote
from loguru import logger


def response(flow) -> None:
    """
    :param flow:
    :return:
    """
    # TODO:Batch Process logic
    for url in FilterURLS:
        if url in flow.request.url:
            logger.info(f'Starting Process Filter URLS: {url}')
            body = unquote(flow.response.text)
            data = json.loads(body)
            AllEntrances('xiaohongshu', data)
