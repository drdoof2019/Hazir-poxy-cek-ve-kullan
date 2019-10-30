import requests
from bs4 import BeautifulSoup
from random import choice

def GetProxy():
    url = 'https://www.sslproxies.org'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return {'https': choice(list(map(lambda x: x[0]+':'+x[1],list(zip(list(map(lambda x: x.text, soup.find_all('td')[::8])), (map(lambda x: x.text, soup.find_all('td')[1::8])))))))}

def UseProxy(url):
    while True:
        try:
            proxy = GetProxy()
            r = requests.get(url,proxies=proxy,timeout=5)
            if r.status_code == 200:
                print('Çalışan proxy = ', proxy)
                break
        except:
            print('Bu proxy denendi ancak çalışmıyor : ', proxy)
            pass
    return r

url = 'https://www.youtube.com/'
x = UseProxy(url)
print(x.text)
