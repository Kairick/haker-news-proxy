from flask import Flask
from werkzeug.exceptions import HTTPException

from app.routes import bad_request, hacker_news, not_found


def create_app():
    app = Flask(__name__)

    app.register_blueprint(hacker_news)
    app.register_error_handler(HTTPException, bad_request)
    app.register_error_handler(HTTPException, not_found)

    return app
