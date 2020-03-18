# coding=utf-8

import time
import requests
from guniflask.scheduling import async_run

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

