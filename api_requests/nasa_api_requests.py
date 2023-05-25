import requests
api_key = "DEMO_KEY"

url = "https://api.nasa.gov/planetary/apod"

response = requests.get(url, params={"api_key": api_key, "date": "2020-08-17"})
print(response)
body = response.json()
print(body.keys())
print(body["hdurl"])
print(body["explanation"])


