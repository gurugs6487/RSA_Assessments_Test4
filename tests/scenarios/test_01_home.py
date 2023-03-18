import pytest


def test_home1(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'<h1>Hello World !!!</h1>' in resp.data

@pytest.mark.xfail
def test_home2(client):
    resp = client.post('/')
    assert resp.status_code == 200

@pytest.mark.xfail
def test_home3(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'<h1>Hello World !!</h1>' in resp.data