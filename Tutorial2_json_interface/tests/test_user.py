#!/usr/bin/env python3
import random

from flask.testing import FlaskClient

username = 'test'

def test_info(client: FlaskClient):
    response = client.get("/%s/info" % (username))
    json = response.get_json()
    print(json)
    assert json['money'] == 0
    assert json['capability'] == 0
