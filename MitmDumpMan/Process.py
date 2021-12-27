#!/usr/bin/env python
# ~*~ coding: utf-8 ~*~
"""
https://www.cnblogs.com/failymao/archive/2020/03/10/12455840.html
"""

__all__ = 'AllEntrances'


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


class SuperProcess(object):

    def get_source(self):
        pass

    def parse_process(self):
        pass


class XHS(SuperProcess):
    """
    @source: xiao hong shu
    """

    def __init__(self, results):
        self.results = results

    def get_source(self):
        return "xiaohongshu"

    def parse_process(self):
        # TODO: xiaohongshu process logic
        print(self.results)

    def collect_context(self):
        StrategyFactory.register(self.get_source(), XHS)


def Init_Strategys(results: str):
    """
    :return:
    """
    XHS(results).collect_context()


def AllEntrances(source: str, results: str):
    """All entrances
    :param source:
    :param results:
    :return:
    """
    Init_Strategys(results=results)
    strategy = StrategyFactory.get_strategy_by_source(source=source)
    if not strategy:
        raise Exception("Please Check! Is there really this data source? ")
    return strategy().parse_process()


if __name__ == '__main__':
    AllEntrances('xiaohongshu.com', '{}')
