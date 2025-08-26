import requests
from bs4 import BeautifulSoup

#本文を取得する対象のURLを参照
url = 'https://news.yahoo.co.jp/articles/724c9072b5f7e93e362d29bf1caedb9485033636'

#GETリクエストを送信し、HTMLを取得
response = requests.get(url)

#HTMLを解析する
soup = BeautifulSoup(response.text, 'html.parser')

#本文の要素を取得
#CSSセレクタを使用して、本文を取得する
text_element = soup.select_one('#uamods > div.article_body.highLightSearchTarget > div:nth-child(1) > p')

#本文のテキストを取得する
text_text = text_element.text

#本文を表示する
print(text_text)

