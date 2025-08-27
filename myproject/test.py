# 必要なライブラリをインポート

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

# ヘッドレスモードで起動するためのオプションを設定
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Chromeを立ち上げる
chrome_driver = webdriver.Chrome(options=chrome_options)

# TERAKOYAのトップページにアクセス
chrome_driver.get('https://terakoya.sejuku.net/register')

# 最大30秒間、ログインボタンが表示されるのを待つ
wait = WebDriverWait(chrome_driver, 60)
header_login_button = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 
         '#root > header > div.sc-jgyNOb.eGDJQH')
    )
)

# ログインボタンをクリックする
header_login_button.click()
