import requests as req
import bs4 as bs


def is_part_in_list(str, words):
    for word in words:
        if word.lower() in str.lower().split():
            return True
    return False


KEYWORDS = ['дизайн', 'фото', 'web', 'python']


requests = req.get('https://habr.com/ru/articles/')
soap = bs.BeautifulSoup(requests.text, features="lxml")
articles = soap.select("article.tm-articles-list__item")


for article in articles:
    link = "https://habr.com" + article.select_one('a.tm-title__link')['href']
    artical_response = req.get(link)
    artical_soup = bs.BeautifulSoup(artical_response.text, features="lxml")
    articaltext = artical_soup.select_one('div.tm-article-presenter').text
    pretitle = artical_soup.select_one('div.tm-article-presenter')
    title = pretitle.select_one("h1")
    if is_part_in_list(articaltext, KEYWORDS):
        print(f"{pretitle.select_one('time')['datetime']} - {title.select_one('span').text} - {link}" )
    