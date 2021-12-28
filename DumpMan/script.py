from config import ResourceList
from process import all_entrances
import json
from urllib.parse import unquote
from loguru import logger


def response(flow) -> None:
    """
    :param flow:
    :return:
    """
    for source in ResourceList.keys():
        if ResourceList.get(source) in flow.request.url:
            logger.info(f'Starting Process Filter URLS: {ResourceList.get(source)}')
            body = unquote(flow.response.text)
            data = json.loads(body)
            all_entrances(source, data)
