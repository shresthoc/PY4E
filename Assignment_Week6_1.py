import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location:')
print('Retrieving', url)
data = urllib.request.urlopen(url)
data = data.read().decode()
info = json.loads(data)
print('Retrieved', len(data), 'characters')
num = 0
total = 0
counts = list()
comments = info['comments']
for comment in comments:
    counts.append(comment['count'])

print('Count:', len(counts))
print('Sum:', sum(counts))
