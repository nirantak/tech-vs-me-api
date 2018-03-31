import requests

r = requests.get('https://techversus.me/feed.xml')
r.encoding = 'utf-8'

print(r.content)
