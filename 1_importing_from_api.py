from requests import Request, Session
import json

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'id':'1'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '1df5b2ef-e38c-46ec-9d8d-b649bafd746',
}

session = Session()
session.headers.update(headers)


response = session.get(url, params=parameters)
data = json.loads(response.text)
print(data)