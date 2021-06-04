from random import randint
from time import sleep
import requests
from bs4 import BeautifulSoup
import sqlite3


list1 = []
for n in range(1, 7):
    url = f'https://gemrielia.ge/category/43-comeuli/?page={n}'
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    info = (soup.find_all('a', {'class': 'articleTitle'}))
    for x in range(len(info)):
        list1.append((info[x]).text)
    sleep(randint(15, 20))
conn = sqlite3.connect("recepti.sqlite")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE receptebi

(id INTEGER PRIMARY KEY AUTOINCREMENT,
dasaxeleba VARCHAR
);''')
for each in range(len(list1)):
    a=(list1[each])
    cursor.execute('INSERT INTO receptebi (dasaxeleba) VALUES (?)',(a,))
    conn.commit()