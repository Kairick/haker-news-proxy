from bs4 import BeautifulSoup

from app.constants import URL


def change_content(content: str) -> str:
    """Добавлем ™ ко всем словам из 6 букв"""
    soup = BeautifulSoup(content, 'html.parser')
    change_urls(soup)
    comments = soup.find_all("div", {"class": "comment"})
    for comment in comments:
        list_of_words = comment.text.split(' ')
        for i, word in enumerate(list_of_words[:]):
            if word.isalpha() and len(word) == 6:
                list_of_words[i] = f'{word}™'
        comment.string = ' '.join(list_of_words)
    return str(soup)


def change_urls(soup: BeautifulSoup):
    """Меняем урлы для подключения стилей и отображения картинок"""
    title = soup.find('link')
    if title:
        title['href'] = f'{URL}{title["href"]}'
    images = soup.find_all('img')
    for image in images:
        image['src'] = f'{URL}{image["src"]}'
