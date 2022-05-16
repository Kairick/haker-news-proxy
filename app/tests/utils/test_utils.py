import pytest
from bs4 import BeautifulSoup

from app.utils import add_tm_sign, change_links, change_text


@pytest.mark.parametrize(
    "tag, expected", [
        ('<div>I am a .doctor!</div>', ['I', 'am', 'a', '.doctor™!']),
        ('<h1>(Parent & \'parent\')</h1>', ['(Parent™', '&', '\'parent™\')']),
        ('<a>Кто пришëл? Я пришëл.</a>', ['Кто', 'пришëл™?', 'Я', 'пришëл™.']),
    ]
)
def test_add_tm_sign_success(tag: str, expected: list):
    """Тестирует работу функции add_tm_sign"""
    soup = BeautifulSoup(tag, 'lxml')

    actual_1 = add_tm_sign(soup)

    assert expected == actual_1


def test_change_links():
    """Тестирует подмену слов в тексте ссылок"""
    string_link = '<a href="submit">{submit}</a>'
    actual_link = '<a href="submit">{submit™}</a>'
    soup = BeautifulSoup(string_link, 'lxml')

    change_links(soup.find_all('a'))

    assert soup == BeautifulSoup(actual_link, 'lxml')


def test_change_text():
    """Тестируем подмену слов в тегах span не трогая теги внутри  span"""
    span = ('<td><span class="hnmore"><a href="front?day=2022-05-13">day</a>'
            'Some <answer!></span')
    result = ('<td><span class="hnmore"><a href="front?day=2022-05-13">day</a>'
              'Some <answer™!></span>')
    soup = BeautifulSoup(span, 'lxml')

    change_text(soup.find_all('span'))

    assert soup == BeautifulSoup(result, 'lxml')
