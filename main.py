import requests as requests

#1
url = "https://www.naver.com"
data = {"val1" : "11"}
response = requests.get(url, data = data)

print(response.text)

