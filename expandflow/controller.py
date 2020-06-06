# coding=utf-8

import uuid
from flask import request, jsonify
import logging

from guniflask.web import blueprint, post_route, get_route
from expandflow.manager.base import BaseManager


log = logging.getLogger(__name__)


@blueprint('/api')
class ExpandController:
    def __init__(self, expand_manager: BaseManager):
        self.expand_manager = expand_manager

    @post_route('/submit-expand-task')
    def submit_spider_task(self):
        data = request.json
        sents = data.get('sents')
        expand_options = data.get('expand_options')
        callback = data.get('callback')
        ttype = expand_options['ttype']
        keyword = expand_options['keyword']
        expand_token = self._generate_expand_token()

        if expand_options is None:
            expand_options = {}
        expand_options.update(expand_token=expand_token, callback=callback)
        log.debug('run expand, callback: %s, options: %s', callback, expand_options)
        self.expand_manager.run_expand(expand_options)
        resp_data = {'callback': callback, 'expand_token': expand_token}
        return jsonify(resp_data)

    @get_route('/get-expand-result')
    def get_expand_result(self):
        expand_token = request.args.get('expand_token')
        # TODO
        pass

    def _generate_expand_token(self):
        return uuid.uuid4().hex
