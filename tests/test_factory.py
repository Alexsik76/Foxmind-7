from race_table import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'


def test_report(client):
    response = client.get('/report/')
    assert b'Daniel Ricciardo' in response.data


def test_report_drivers(client):
    response = client.get('/report/drivers/')
    assert b'Daniel Ricciardo' in response.data


def test_error(client):
    response = client.get('/report/drivers/?driver_id=AAA')
    assert b'Driver not found' in response.data


def test_get_driver(client):
    response = client.get('/report/drivers/?driver_id=SVF')
    assert b'Sebastian Vettel' in response.data
