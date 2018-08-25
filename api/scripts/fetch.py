import requests

r = requests.get('https://tvm.nirantak.com/feed.xml')
r.encoding = 'utf-8'

print(r.content)
