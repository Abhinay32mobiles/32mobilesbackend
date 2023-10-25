import json
import requests

articles = [
    {
        "title": "Sample Article 1",
        "content": "This is the content of the first article.",
        "publication_date": "2023-10-23",
        "image_url": "https://example.com/image1.jpg",
        "tags":[1]
    },
    {
        "title": "Sample Article 2",
        "content": "This is the content of the second article.",
        "publication_date": "2023-10-24",
        "image_url": "https://example.com/image2.jpg",
        "tags":[1]
    }
]
  # Your array of article JSON objects

api_url = "http://127.0.0.1:8000/api/articles/"

for article in articles:
    response = requests.post(api_url, json=article)
    print(f"Request URL: {api_url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")
    if response.status_code == 201:
        print(f"Article {article['title']} created successfully.")
    else:
        print(response.status_code, type(article))