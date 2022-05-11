import pytest
import requests_mock

from app.constants import URL


def test_item_endpoint_success(client, response_text):
    """Тестирует успешное добавление постфикса к словам"""
    with requests_mock.Mocker() as m:
        m.get(f'{URL}item?id=1234', status_code=200, text=response_text)
        response = client.get('/item?id=1234')

    assert response.status_code == 200
    assert '™' in response.text


@pytest.mark.parametrize('endpoint', ['/', '/login', '/items'])
def test_404_error(client, endpoint):
    """Тестирует  поведение API при доступе к несуществующим endpoints"""

    response = client.get(endpoint)

    assert response.status_code == 404
    assert 'Page Not Found' in response.text


@pytest.mark.parametrize('query', ['', '?name=Joe'])
def test_item_without_id(client, query):
    """Тестирует поведение API при правильном endpoint, но без параметра id"""
    response = client.get(query)

    assert response.status_code == 404
    assert 'Page Not Found' in response.text
