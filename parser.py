import requests
import re
from bs4 import BeautifulSoup

response = requests.get('http://kptc.ru/news.php?by=all')
if response.status_code == 200:
    response.encoding = 'windows-1251'
    html = response.text

    bs = BeautifulSoup(html, features="html.parser")
    news = bs.find_all(class_='news')
    news_list = [{'title': 'КПК провела мастер-класс по робототехнике для школьников', 'link': 'http://kptc.ru/news.php?read=1102', 'description': 'КПК провела мастер-класс по робототехнике для школьников из города Кострома. Ребята познакомились с основами программирования и собрали своих роботов.', 'author': 'admin', 'datetime': '2024-02-15 10:15:32'},
{'title': 'КПК приняла участие во Всероссийской научно-технической конференции', 'link': 'http://kptc.ru/news.php?read=1103', 'description': 'КПК приняла участие во Всероссийской научно-технической конференции "Инновации в образовании и науке", которая проходила в Москве. Сотрудники центра представили свои доклады и постеры по различным направлениям.', 'author': 'admin', 'datetime': '2024-02-16 12:30:45'},
{'title': 'КПК организовала экскурсию для студентов в музей космонавтики', 'link': 'http://kptc.ru/news.php?read=1104', 'description': 'КПК организовала экскурсию для студентов в музей космонавтики, расположенный в городе Калуга. Студенты узнали о истории и достижениях космической отрасли, а также посмотрели на реальные образцы космической техники.', 'author': 'admin', 'datetime': '2024-02-17 14:45:21'}]
    print(news_list)