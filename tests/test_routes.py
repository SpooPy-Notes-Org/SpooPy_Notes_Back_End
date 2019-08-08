import pytest

def test_home_route_exists(client):
    response = client.get('/?query=')
    assert response.status_code == 200

def test_one_word(client):
    response = client.get('/?query=ransom')
    assert response.status_code == 200

def test_long_word(client):
    response = client.get('/?query=iseeyouiseeyouiseeyouiseeyou')
    assert response.status_code == 200

def test_multiple_words(client):
    response = client.get('/?query=i see you')
    assert response.status_code == 200

def test_special_characters(client):
    response = client.get('/?query=&\'*@"!$%.#?')
    assert response.status_code == 200

def test_space_in_front(client):
    response = client.get('/?query= ransom')
    assert response.status_code == 200

def test_space_at_end(client):
    response = client.get('/?query=ransom ')
    assert response.status_code == 200

def test_only_spaces(client):
    response = client.get('/?query=      ')
    assert response.status_code == 200

def test_many_spaces_followed_by_char(client):
    response = client.get('/?query=      ?')
    assert response.status_code == 200
    
def test_query_mispelled(client):
    response = client.get('/?querrrry=ransom')
    assert response.status_code == 404

def test_route_mistyped(client):
    response = client.get('/query=ransom')
    assert response.status_code == 404

