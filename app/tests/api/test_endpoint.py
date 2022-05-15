import requests_mock

from app.constants import URL


def test_endpoint_success(client, response_text):
    """Тестирует успешное добавление постфикса к словам"""
    with requests_mock.Mocker() as m:
        m.get(f'{URL}/item?id=1234', status_code=200, text=response_text)
        response = client.get('/item?id=1234')

    assert response.status_code == 200
    assert '™' in response.text
