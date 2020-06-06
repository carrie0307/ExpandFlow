# coding=utf-8

from guniflask.context import configuration, bean

from expandflow.manager.base import BaseManager
from expandflow.manager.async_run import AsyncRunManager


@configuration
class ManagerConfig:

    @bean('expand_manager')
    def expand_manager(self) -> BaseManager:
        # 根据配置文件选择合适的manager
        return AsyncRunManager()