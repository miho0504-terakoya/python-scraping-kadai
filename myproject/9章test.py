from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
from bs4 import BeautifulSoup
import time

#　ヘッドレスも＾ドで起動するためのオプションを設定
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#　Chromeを立ち上げる
chrome_driver = webdriver.Chrome(options=chrome_options)

#　TERAKOYAのトップページにアクセス
chrome_driver.get('https://terakoya.sejuku.net/register')


# 最大30秒間、ログインボタンが表示されるのを待つ
wait = WebDriverWait(chrome_driver, 30)
header_login_button = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#root > header > div.sc-bhVsRh.hZBqIC")
        )
    )


#　ログインボタンをクリックする
header_login_button.click()

#　メールアドレスとパスワードを入力する
email_address = input('メールアドレスを入力してください：')
password = getpass('パスワードを入力してください：')

# メールアドレスとパスワードの入力欄を見つける
arnet_element = chrome_driver.find_element(By.CSS_SELECTOR, '.sc-kNOymR.TvzZn') 
email_input = chrome_driver.find_element(By.NAME, 'email')
password_input = chrome_driver.find_element(By.NAME, 'password')

# メールアドレスとパスワードを設定
email_input.send_keys(email_address)
password_input.send_keys(password)

# ログインボタンをクリックしてログイン
form_login_button = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#root > div.sc-kNOymR.TvzZn > div.sc-lgpSej.gsAReM > div.sc-dntSTA.dQOsDP > button")
    )
                               )
form_login_button.click()


# ログイン後、要素が読み込まれるまで待つ

timeline_button = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'li[data-e2e="navi-timeline"] a')
    )
)
time.sleep(5)

timeline_button.click()

# ログイン後、最新の投稿が表示されるまで待つ

wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'a[data-e2e="study_reports"]')
    )
)

# ページのHTMLをBeautifulSoupで解析する

soup = BeautifulSoup(chrome_driver.page_source, 'html.parser')

# 最新の投稿を取得

latest_post = soup.find('a', {'data-e2e': 'study_reports'})

# 最新投稿の href を表示


print('Latest post href:')
print('https://terakoya.sejuku.net' + latest_post['href'])

# ブラウザを閉じる

chrome_driver.quit()