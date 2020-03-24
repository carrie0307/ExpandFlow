# coding=utf-8

import time
import requests
from guniflask.scheduling import async_run

from os.path import join
import json

from expandflow.pathutils import PathUtils
from .base import BaseManager


class AsyncRunManager(BaseManager):

    def __init__(self):
        self.path_utils = PathUtils()

    def run_expand(self, expand_options=None):
        self.async_run_expand(expand_options=expand_options)

    @async_run
    def async_run_expand(self, expand_options=None):
        time.sleep(4)

        expand_token = expand_options['expand_token']
        # 临时写一个结果存储函数，使得人工研判部分能够获取到关键词拓展的结果
        json_data = [{'keyword': '信工所', 'context': 'iie'}, {'keyword': '自动化所', 'context': 'nlpr'},
                     {'keyword': '计算所', 'context': 'ict'}, {'keyword': '电子做', 'context': 'electronic'}]
        with open(join(self.path_utils.expand_result_dir(expand_token), "result.json"), 'w') as f:
            json.dump(json_data, f, ensure_ascii=False)

        url = expand_options['callback']
        if not url:
            raise ValueError('Cannot get the expand callback url ')
        data = {"expand_token": expand_options['expand_token']}
        requests.post(url, json=data)


    def _load_expand_model(self, expand_name: str):
        # TODO
        pass

    def stop_expand(self, expand_token: str):
        # TODO
        pass

    def get_expand_status(self, expand_token: str):
        # TODO
        pass

    def get_expand_result(self, expand_token: str):
        # TODO
        pass

