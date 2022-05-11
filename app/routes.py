from flask import Blueprint, Response, abort, render_template, request
import requests

from app.utils import change_content
from app.constants import URL

hacker_news = Blueprint('hacker_news', __name__, template_folder='templates')


@hacker_news.route('/item', methods=['GET'])
def item():
    item_id = request.args.get('id')
    if not item_id:
        abort(400)
    response = requests.get(f'{URL}item', params={'id': item_id})
    content = change_content(response.text)
    return Response(content.encode(encoding='UTF-8'), response.status_code)


def bad_request(e):
    return render_template('400.html'), 400


def not_found(e):
    return render_template('404.html'), 404
