import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
api_key = "DEMO_KEY"

date = '2000-08-17'
response = requests.get(url, params={'api_key': 'DEMO_KEY', 'sol': 1000})

data = response.json()
print(data["photos"])

