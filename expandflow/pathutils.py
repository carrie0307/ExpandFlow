# coding=utf-8

import os
from os.path import join
from functools import wraps

from guniflask.config import settings


def create_if_not_exists(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        path = func(*args, **kwargs)
        if isinstance(path, str):
            os.makedirs(path, exist_ok=True)
        return path

    return wrapper


class PathUtils(object):
    """
    返回业务常用路径
    """

    @property
    def home_dir(self):
        return settings['home']

    @property
    @create_if_not_exists
    def expand_dir(self):
        return join(self.home_dir, "expandmodels")

    @property
    @create_if_not_exists
    def data_dir(self):
        return join(self.home_dir, ".expand_data")

    @create_if_not_exists
    def expand_data_dir(self, expand_token: str):
        return join(self.data_dir, expand_token)

    @create_if_not_exists
    def expand_result_dir(self, expand_token: str):
        return join(self.expand_data_dir(expand_token), 'result')