import requests

responce = requests.get("https://newsapi.org/v2/everything",params = {
    "q" : "AI",
    "apiKey" : "YOUR-API-KEY"
})

data = responce.json()
print(data)
print(f"status is {data['status']} ")
for article in data["articles"][:7]:
    print(f"url is {article['url']}")
    print(f"id is : {article['source']['id']} and name is {article['source']['name']} \n and is description is {article['description']}")
    print(f" Author is  : {article['author']} and Title is {article['title']}")