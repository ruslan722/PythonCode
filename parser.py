import requests
import re


responce = requests.get('http://kptc.ru/news.php?by=all')
if responce.status_code == 200:
    responce.encoding = 'windows-1251'
    html = responce.text

    with open(file='html.log', mode='w', encoding='utf-8') as f:
        f.write(html)

    regex = r"<a class='item1'[^>]+>([^<]+)"
    for item in re.finditer(regex, html):
        if len(item.regs) != 2:
            continue
        start, stop = item.regs[1]
        text = html[start:stop]
        print(text)