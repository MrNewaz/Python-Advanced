import requests
from bs4 import BeautifulSoup

res = requests.get('https://stackoverflow.com/questions')

soup = BeautifulSoup(res.text, 'html.parser')

questions = soup.select('.question-summary')

for question in questions:

    print(question.select_one('.question-hyperlink').getText())
    print(question.select_one('.vote-count-post').getText())
