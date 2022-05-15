from flask import Flask

from app.routes import hacker_news


def create_app():
    """Создает приложение с машрутами"""
    app = Flask(__name__)

    app.register_blueprint(hacker_news)

    return app
