import requests
import pprint
from getpass import getpass

#APIキーを指定
api_key = getpass('APIキーを入力してください:')

#検索キーワードを変数serch_worldに格納
serch_world = input('検索キーワードを入力してください:')


#Youtybe　Data　APIのURL
url = 'https://www.googleapis.com/youtube/v3/search'

#データを取得
response = requests.get(
    url,
    params={
        'key':api_key,
        'part': 'snippet',
        'q': serch_world,
        'type': 'video',
        'maxResults': 10
    }
)

#レスポンスのJSONを取得
json_data = response.json()

#JSONの中身を確認
pprint.pprint(json_data)

#取得した動画のタイトルとURLを表示
for item in json_data['items']:
    video_title = item['snippet']['title']
    video_url = f'https://www.youtube.com/watch?v={item["id"]["videoId"]}'
    print(f'{video_title}:{video_url}')
    