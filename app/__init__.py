from flask import Flask
from werkzeug.exceptions import BadRequest, NotFound

from app.routes import bad_request, hacker_news, not_found


def create_app():
    """Создает приложение со всеми обработчиками ошибок и машрутами"""
    app = Flask(__name__)

    app.register_blueprint(hacker_news)
    app.register_error_handler(NotFound, not_found)
    app.register_error_handler(BadRequest, bad_request)

    return app
