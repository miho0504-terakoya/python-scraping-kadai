import requests
from bs4 import BeautifulSoup


# タイトルを取得する対象のURL
url = 'https://news.yahoo.co.jp/articles/724c9072b5f7e93e362d29bf1caedb9485033636'

# GETリクエストを送信し、HTMLを取得する
response = requests.get(url)

# HTMLを解析する
soup = BeautifulSoup(response.text, 'html.parser')

# タイトルの要素を取得する
# CSSセレクタを使用して、タイトルを取得する
title_element = soup.select_one('#uamods > header > h1')

# タイトルのテキストを取得する
title_text = title_element.text


# タイトルを表示する
print(title_text)

