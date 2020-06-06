import requests
from conf import expandflow
import json


base_url = ""
server_address = expandflow.server_address
headers = {'Content-Type': 'application/json'}


def test_submit_expandtask():
    url = 'http://{}/api/submit-expand-task'.format(server_address)
    sents = ['sent1', 'sent2', 'sent3']
    task_token = '3a10dcaa-4da9-417f-b0c2-5169f2a91f71'
    callback = 'http://127.0.0.1:8068/api/keyword-expansion/expansion-callback?task_token={}'.format(task_token)
    expand_options = {'keyword': 'keyword', 'ttype': 'Description'}
    data = {
        "sents": sents,
        "callback": callback,
        "expand_options": expand_options

    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200
