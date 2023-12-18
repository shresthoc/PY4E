from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
numbers = []
count = 0
for tag in tags:
    numbers.append(float(tag.text))
    count = count + 1

print('Count', count)
print('Sum', sum(numbers))