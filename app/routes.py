import requests
from flask import Blueprint, request

from app.constants import URL
from app.utils import change_content

EXCLUDED_HEADERS = ['content-encoding', 'content-length',
                    'transfer-encoding', 'connection']
STATIC_EXTENSION = ['ico', 'gif', 'js', 'css']

hacker_news = Blueprint('hacker_news', __name__)


@hacker_news.route('/', methods=['GET'], defaults={'path': ''})
@hacker_news.route('/<path:path>')
def proxy(path):
    """Прокстирует запрос к hacker news"""
    response = requests.get(f'{URL}/{path}', params=dict(request.args))

    headers = [(name, value) for (name, value) in response.raw.headers.items()
               if name.lower() not in EXCLUDED_HEADERS]

    if path.split('.')[-1] in STATIC_EXTENSION:
        return response.content, response.status_code, headers
    else:
        content = change_content(response.text)
        return content, response.status_code, headers

