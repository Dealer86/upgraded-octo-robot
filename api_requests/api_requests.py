import requests

url = "http://localhost:8000/users"


response = requests.get(url)
print(response)
print(response.json())
print(response.status_code)

# response = requests.post(url, json={"name": "random_username", "email": "bestcoder@gmail.com"})
# print(response)
# print(response.json())

# response = requests.delete(url, params={"id": 1})
# print(response)
# print(response.json())

# response = requests.put(url + str(2), json={"name": "Awesomeness"})
# print(response)
# print(response.json())

