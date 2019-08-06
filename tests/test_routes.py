import pytest

def test_home_route(client):
    response = client.get('/?query=iseeyou')
    assert response.status_code == 200