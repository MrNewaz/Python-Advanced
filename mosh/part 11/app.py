import requests


rest = requests.get('https://jsonplaceholder.typicode.com/posts')

print(rest.json())
