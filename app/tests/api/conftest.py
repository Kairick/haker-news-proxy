import pytest

from app import create_app


@pytest.fixture()
def app():
    """Фикстура для создания тестового приложения Flask"""
    app = create_app()
    app.config.update({'TESTING': True, })

    yield app


@pytest.fixture()
def client(app):
    """Клиент для тестирования"""
    return app.test_client()


@pytest.fixture()
def response_text():
    """Фейковый ответ с hacker news"""
    return """
    <div class="comment">
     <span class="commtext c00">The visual description of the colliding files,
     at <a href="http://shattered.io/static/pdf_format.png" 
     rel="nofollow">http://shattered.io/static/pdf_format.png</a>,
     is not very helpful in understanding how they produced the PDFs, 
     so I took apart the PDFs and worked it out.<p>Basically, 
     each PDF contains a single large (421,385-byte) JPG image, followed by
     a few PDF commands to display the JPG. The collision lives entirely 
     in the JPG data - the PDF format is merely incidental here. 
     </p><div class="reply"> <p><font size="1"></font></p></div></span></div>
     """
