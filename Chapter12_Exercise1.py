import socket
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter a link -')
try:
    if url.startswith('http://'):
        hostname = url.split('/')
        hostname = hostname[2]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((hostname, 80))

    elif url.startswith('https://'):
        hostname = url.split('/')
        hostname = hostname[2]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((hostname, 80))

    elif not url.startswith('http://'):
        hostname = url.split('/')
        hostname = hostname[0]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((hostname, 80))

    elif not url.startswith('https://'):
        hostname = url.split('/')
        hostname = hostname[0]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((hostname, 80))
except:
    print('You have entered an improperly formatted or non-exisent url')
    exit()

cmd = ('GET' + url + 'HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode())

mysock.close()
