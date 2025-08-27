# Seleniumライブラリからwebdriverモジュールをインポート
from selenium import webdriver
from selenium.webdriver.common.by import By

#  Chromeブラウザ起動オプションを指定
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Google Chrome用のブラウザドライバーインスタンスを作成
chrome_driver = webdriver.Chrome(options=chrome_options)

# Googleのトップページを開く
chrome_driver.get('https://www.google.com')

# 検索ボックス要素（名前が 'q' の要素）を取得
search_box = chrome_driver.find_element(By.NAME, 'q')

# 検索ボックスの 'maxlength' 属性の値を取得
attribute_value = search_box.get_attribute('maxlength')

# 属性の値を出力
print(f'属性の値: {attribute_value}')

# ブラウザを閉じる
chrome_driver.quit()