import json

import pytest

endpoint = "api/v1/book/wish_list"

def test_one(flask_client):
    result = flask_client.get(
        endpoint
    )
    print(result)
    assert 1 >3
