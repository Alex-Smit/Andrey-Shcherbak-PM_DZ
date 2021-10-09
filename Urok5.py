import bs4
import requests

response = requests.get('https://itc.ua/')


instance_page = bs4.BeautifulSoup(response.text, "html.parser")

content = instance_page.find('main', {'id': 'content'})
rows = content.find_all('div', {'class': 'row'})

_urls = []
_list_news = []
for row in rows:

    h2_tag = row.find('h2')
    if not h2_tag:
        continue

    tag_a = h2_tag.find('a')
    url = tag_a.get('href')

    if not url:
        continue

    if url in _urls:
        continue

    title = tag_a.get_text()

    info_tag = row.find('div', {'class': 'entry-header'})
    time = info_tag.find('time').get('datetime')
    author = info_tag.find('a').get_text()

    response = requests.get(url)
    instance_page = bs4.BeautifulSoup(response.text, "html.parser")

    content_text = instance_page.find('div', {"class": 'post-txt'})
    text = content_text.find_all('p')
    _text = ""
    for obj_p in text:
        _text += obj_p.get_text()

    _urls.append(url)
    _article = {
        'url': url,
        'title': title,
        'time': time,
        'author': author,
        '_text': _text
    }
    _list_news.append(_article)


for i in _list_news:
    print(i)