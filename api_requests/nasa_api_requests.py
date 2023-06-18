import os

import requests
api_key = "DEMO_KEY"

url = "https://api.nasa.gov/planetary/apod"

# response = requests.get(url, params={"api_key": api_key, "date": "2020-08-17"})
# print(response)
# body = response.json()
# print(body.keys())
# print(body["hdurl"])
# print(body["explanation"])

response = requests.get(url, params={'api_key': api_key, 'date': "2023-02-27"})
print(response)
print(response.links)
print(response.json())
x = response.json()
print(x["hdurl"])
# exp = x["explanation"].split(".")
# for a in exp:
#     print(a)











