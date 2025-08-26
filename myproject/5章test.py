import requests
import pprint

response = requests.get('https://httpbin.org/get', params={'key': 'value'})
pprint.pprint(response.json())
