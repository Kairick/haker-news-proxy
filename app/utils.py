import re

from bs4 import BeautifulSoup, Tag

from app.constants import URL


def change_content(content: str) -> str:
    """Добавляет ™ ко всем словам из 6 букв"""
    changed_content = re.sub(URL, '/', content)
    soup = BeautifulSoup(changed_content, 'lxml')
    change_links(soup.find_all('a'))
    change_text(soup.find_all('span'))
    change_text(soup.find_all('p'))
    return str(soup)


def change_links(links: list):
    """Добавляет ™ к ссылкам"""
    for link in links:
        if link.text:
            list_of_words = add_tm_sign(link)
            link.string = ' '.join(list_of_words)


def change_text(spans: list):
    """Добавляет ™ к остальному тексту"""
    for span in spans:
        if span.text:
            for tag in span.contents:
                if not tag.name:
                    list_of_words = add_tm_sign(tag)
                    tag.replace_with(' '.join(list_of_words))


def add_tm_sign(tags: Tag) -> list:
    """Возвращает список с добавлением ™ к словам из 6 букв"""
    words = tags.text.split(' ')
    for i, word in enumerate(words[:]):
        temp_word = word.strip().strip('.,():;!?\'"[]<>|*&^%#{}')
        if temp_word.isalpha() and len(temp_word) == 6:
            words[i] = word.replace(temp_word, f'{temp_word}™')
    return words
