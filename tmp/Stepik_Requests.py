import requests

with open('dataset_3378_3.txt') as file:
    url = file.readline().strip()
    text = requests.get(url)
    while text.text[0:2] != 'We':
        url = 'https://stepic.org/media/attachments/course67/3.6.3/' + text.text
        text = requests.get(url)
        print(url)
    print(text.text)
