#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File         : process.py
# @Date         : 28-12-2021
# @Author       : Payne
# @Email        : wuzhipeng1289690157@gmail.com
# @Desc: process logic

from config import *
import pymysql
from loguru import logger

__all__ = "all_entrances"
# logger.add(
#     'runtime_{time}.log',
#     rotation='00:00',
#     level="ERROR",
#     diagnose=True,
#     enqueue=True,
#     compression='zip',
#     backtrace=True,
# )


class StrategyFactory(object):
    strategy = {}

    @classmethod
    def get_strategy_by_source(cls, source: AnyStr):
        """Get the specific policy class from the source
        :param source: AnyStr
        :return:
        """
        return cls.strategy.get(source)

    @classmethod
    def register(cls, strategy_source: AnyStr, strategy: object):
        """Registration policy type
        :param strategy_source:
        :param strategy:
        :return:
        """
        if strategy_source is None:
            raise Exception("strategyType can't be null")
        cls.strategy[strategy_source] = strategy


class ProcessBase(object):
    """
    Data processing base class
    """

    @classmethod
    def collect_context(cls):
        """
        StrategyFactory.register
        """
        StrategyFactory.register(cls().get_source(), cls)

    def get_source(self) -> str:
        pass

    def parse_process(self, results):
        """
        @res
        """
        pass

    @staticmethod
    def mysql_client():
        client = pymysql.connect(**MySQLClientParam)
        return client, client.cursor()

    def storage(self, sql_query):
        client, cursor = self.mysql_client()
        logger.info(f"Process sql: {sql_query}")
        cursor.execute(sql_query)
        client.commit()


class XHS_Search(ProcessBase):

    def get_source(self):
        return "xhs_search"

    def parse_process(self, results: Dict):
        for result in results:
            note_id = result["note"]["id"]
            title = (
                result["note"]["title"]
                if result["note"]["title"]
                else result["note"]["desc"]
            )
            desc = result["note"]["desc"]
            liked_count = result["note"]["liked_count"]
            note_type = result["note"]["type"]
            user_name = result["note"]["user"]["nickname"]
            user_id = result["note"]["user"]["userid"]
            tag_info = result["note"]["tag_info"]
            timestamp = result["note"]["timestamp"]
            geo_info = result["note"]["geo_info"]
            comment_str = f"""("{note_id}", "{title}", "{user_name}", "{user_id}", "{liked_count}")"""
            insert_query = f"""insert ignore into xiaohongshu_comment_note_2(`note_id`, `title`, `user_name`, `user_id`, `liked_count`)
                                        values {comment_str} on duplicate key update liked_count = {liked_count};"""
            self.storage(sql_query=insert_query)


class XHS_Lv(ProcessBase):
    """
    @source: xiao hong shu
    """

    def get_source(self):
        return "xhs_lv"

    def parse_process(self, results: Dict):
        for result in results:
            note_id = result["note"]["id"]
            title = (
                result["note"]["title"]
                if result["note"]["title"]
                else result["note"]["desc"]
            )
            desc = result["note"]["desc"]
            liked_count = result["note"]["liked_count"]
            note_type = result["note"]["type"]
            user_name = result["note"]["user"]["nickname"]
            user_id = result["note"]["user"]["userid"]
            tag_info = result["note"]["tag_info"]
            timestamp = result["note"]["timestamp"]
            geo_info = result["note"]["geo_info"]
            comment_str = f"""("{note_id}", "{title}", "{user_name}", "{user_id}", "{liked_count}")"""
            insert_query = f"""insert ignore into xiaohongshu_comment_note(`note_id`, `title`, `user_name`, `user_id`, `liked_count`)
                                        values {comment_str} on duplicate key update liked_count = {liked_count};"""
            self.storage(sql_query=insert_query)


def init_strategy():
    XHS_Lv.collect_context()
    # XHS_Search.collect_context()


def all_entrances(source: str, results: str) -> object:
    """All entrances
    :param source:
    :param results:
    :return:
    """
    # init strategy
    init_strategy()
    # Build In
    strategy = StrategyFactory.get_strategy_by_source(source=source)
    if not strategy:
        raise Exception("Please Check! Is there really this data source? ")
    return strategy().parse_process(results)


if __name__ == "__main__":
    all_entrances("xhs_lv", "Hello")
    all_entrances("xhs_search", "Hello")
