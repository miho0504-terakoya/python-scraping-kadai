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
latitude = json_data['results'][0]['geometry']['location']['lat']
longitude = json_data['results'][0]['geometry']['location']['lng']

# APIエンドポイントURLを指定する
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

# APIにGETリクエストを送信し、結果を取得する
response = requests.get(
    url,
    params={
      'location': f'{latitude},{longitude}',
      'language': 'ja',
      'radius': 500,
      'type': 'restaurant',
      'key': api_key
    }
)

# レスポンスのJSONデータを格納する
data = response.json()

# レストランの情報を抽出する
restaurants = []
for place in data['results']:
    restaurant = {
        'name': place['name'],
        'rating': place.get('rating', 'N/A'),
        'address': place.get('vicinity', 'N/A'),
        'types': place.get('types', []),
        'place_id': place['place_id']
    }
    restaurants.append(restaurant)

# レストランの情報を表示する
for restaurant in restaurants:
    print(restaurant['name'], restaurant['rating'], restaurant['address'])
