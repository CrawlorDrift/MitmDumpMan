#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File         : process.py
# @Date         : 28-12-2021
# @Author       : Payne
# @Email        : wuzhipeng1289690157@gmail.com
# @Desc:
from config import *
import pymysql

__all__ = 'all_entrances'


def mysql_client(**kwargs):
    client = pymysql.connect(**MySQLClientParam)
    return client, client.cursor()


class StrategyFactory(object):
    strategy = {}

    @classmethod
    def get_strategy_by_source(cls, source):
        """Get the specific policy class from the source
        :param source:
        :return:
        """
        return cls.strategy.get(source)

    @classmethod
    def register(cls, strategy_source, strategy):
        """Registration policy type
        :param strategy_source:
        :param strategy:
        :return:
        """
        if strategy_source == "":
            raise Exception("strategyType can't be null")
        cls.strategy[strategy_source] = strategy


class ProcessBase(object):
    """
    Data processing base class
    """

    def get_source(self):
        pass

    def parse_process(self, results):
        pass


class XHS(ProcessBase):
    """
    @source: xiao hong shu
    """

    def get_source(self):
        return "xiaohongshu"

    def parse_process(self, results):
        """
        """
        # TODO: xiaohongshu process logic
        print(results)

    def collect_context(self):
        StrategyFactory.register(self.get_source(), XHS)


def init_strategy():
    """
    :return:
    """
    XHS().collect_context()


def all_entrances(source: str, results: str):
    """All entrances
    :param source:
    :param results:
    :return:
    """
    init_strategy()
    strategy = StrategyFactory.get_strategy_by_source(source=source)
    if not strategy:
        raise Exception("Please Check! Is there really this data source? ")
    return strategy().parse_process(results)


if __name__ == '__main__':
    all_entrances('xiaohongshu', '{asd:1}')
