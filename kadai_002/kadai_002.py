import requests
import pprint
from getpass import getpass

#APIキーを指定
api_key = getpass('APIキーを入力してください：')

#検索キーワードを変数serch_stationに格納
serch_station = input('駅名を入力してください：')

#GoogleMap Data APIのURL(周辺検索用)
url = 'https://maps.googleapis.com/maps/api/geocode/json'

#入力された駅の緯度経度を取得する
response = requests.get(
    url,
    params={
        'key': api_key,
        'address': serch_station
    }
)

#レスポンスのJSONを取得
json_data = response.json()

#JSONの中身を確認
pprint.pprint(json_data)

#取得したデータの緯度経度を表示
for item in json_data['']



