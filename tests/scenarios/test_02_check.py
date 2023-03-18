import pytest
import json

@pytest.mark.tc1
#@pytest.mark.parametrize("input", [{"number": 50}, {"number": 100}])
def test_check1(client):
    resp = client.post('/check', json={"number": 50})
    assert resp.status_code == 200
    response_data = json.loads(resp.data)
    assert response_data["integer"] == 50
    assert response_data["result"] == "Low"

def test_check2(client):
    resp = client.post('/check', json={"number": 101.5})
    assert resp.status_code == 200
    response_data = json.loads(resp.data)
    assert response_data["integer"] == 101.5
    assert response_data["result"] == "High"


@pytest.mark.tc3
def test_check3(client):
    resp = client.post('/check', json={"number": 100})
    assert resp.status_code == 200
    response_data = json.loads(resp.data)
    assert response_data["integer"] == 100
    assert response_data["result"] == "Equal"

def test_check4(client):
    resp = client.get('/check', json={"number": 200})
    assert resp.status_code == 405

@pytest.mark.tc5
def test_check5(client):
    resp = client.post('/check', json={"number": ""})
    assert resp.status_code == 200
    response_data = json.loads(resp.data)
    #assert b'invalid literal for int()' in resp.data
    assert response_data['error'] != ""
