from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
cnt = input('Enter count:')
count = float(cnt)
psn = input('Enter position:')
position = float(psn)

def Html(url, position):
    html = urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    i = 0
    for tag in tags:
        i = i + 1
        if i == position:
            return tag.get('href', None)

current = 0
while current <= int(count):
    print ('Retrieving: ', url)
    url = Html(url, position)
    current = current + 1
