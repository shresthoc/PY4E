import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location:')
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
print('Retrieving', url)
print('Retrieved', len(data), 'characters')
counts = tree.findall('.//count')
print('Count:', len(counts))
sum = 0
for count in counts:
    sum = sum + int(count.text)
print('Sum:', sum)


