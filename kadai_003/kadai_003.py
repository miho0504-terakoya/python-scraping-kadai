from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
import time

#　ヘッドレスモードで起動するためのオプションを設定
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
email_addres = input('メールアドレスを入力してください：')
password = getpass('パスワードを入力してください：')

#　メールアドレスとパスワードの入力ラナンを見つける
parnet_element = chrome_driver.find_element(By.CSS_SELECTOR, '.sc-kNOymR.TvzZn') 
email_input = parnet_element.find_element(By.NAME, 'email')
password_input = parnet_element.find_element(By.NAME, 'password')


#　メールアドレスとパスワードを設定
email_input.send_keys(email_addres)
password_input.send_keys(password)

# ログインボタンをクリックしてログイン
form_login_button = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 
         "#root > div.sc-kNOymR.TvzZn > div.sc-lgpSej.gsAReM > div.sc-dntSTA.dQOsDP > button")
        )
    )
form_login_button.click()

# ログイン後、要素が読み込まれるまで待つ
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav > img ')))
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.sc-gwPKJL.bTdclZ')))
time.sleep(5)

# TERAKOYAのアカウント設定ページにアクセス
chrome_driver.get('https://terakoya.sejuku.net/account/profile')

# 最大30秒間 プロフィール画面が表示されるのを待つ
wait = WebDriverWait(chrome_driver, 30)
header_edit_button = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,
         "#root > div.sc-BvjM.dayVoP > div > div > main > div > div.sc-lfIzcI.gdQipL > button")
    )
)

# 編集ボタンをクリック
header_edit_button.click()

# 最大30秒間　自己紹介要素が表示されるまで待つ
wait = WebDriverWait(chrome_driver, 30)
input_box = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,
         "#root > div.sc-BvjM.dayVoP > div > div > main > div > div.sc-lfIzcI.gdQipL > div:nth-child(10) > div.sc-CqUPI.bZqAix > textarea")
    )
)

# 自己紹介欄に文字を入力する
input_box.send_keys("プログラミング学習中です！今はスクレイピングに挑戦しています！")

# 最大30秒間　更新ボタンが表示されるまで待つ
wait = WebDriverWait(chrome_driver, 30)
update_button = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,
         "#root > div.sc-BvjM.dayVoP > div > div > main > div > div.sc-lfIzcI.gdQipL > button.sc-dTvVRJ.bHRgJQ.sc-hZdRFE.fLGwDp")
    )
)

# 更新ボタンをクリック
update_button.click()

# Chromeを閉じる
chrome_driver.quit()