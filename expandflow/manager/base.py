# coding=utf-8

from abc import ABCMeta, abstractmethod



class BaseManager(metaclass=ABCMeta):
    @abstractmethod
    def run_expand(self, expand_options=None):
        pass

    @abstractmethod
    def stop_expand(self, expand_token: str):
        pass

    @abstractmethod
    def get_expand_status(self, expand_token: str):
        pass

    @abstractmethod
    def get_expand_result(self, expand_token: str):
        pass