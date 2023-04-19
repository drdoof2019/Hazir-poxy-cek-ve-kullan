import requests
from bs4 import BeautifulSoup
from random import choice
import re

def Proxy():
    dosyakaydet = input("Do you want to save the txt file of the ip addresses you will dig y/n:")
    deger = int(input("How many IP addresses do you want to dig:"))

    def GetProxy():
        url = 'https://www.sslproxies.org'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        return {'https': choice(list(map(lambda x: x[0]+':'+x[1],list(zip(list(map(lambda x: x.text, soup.find_all('td')[::8])), (map(lambda x: x.text, soup.find_all('td')[1::8])))))))}

    def UseProxy(url):
        count = 0
        while count < deger:
            try:
                proxy = GetProxy()
                r = requests.get(url,proxies=proxy,timeout=5)
                if r.status_code == 200:
                    s = f"{proxy}"
                    res_txt =re.sub(r"[{'} ]","", s)
                    l = list(res_txt)
                    l[0] = "" 
                    l[1:5] = []
                    del(l[1])
                    filtrelenmisproxy = "".join(l)
                    print('found working proxy= ', filtrelenmisproxy)
                    if dosyakaydet == "y":
                        with open("proxies.txt","a",encoding="utf-8") as dosya:
                            dosya.write(f"{filtrelenmisproxy}\n")
                    else:
                        pass
                    count += 1
            except:
                print('This proxy has been tried but not working: ', proxy)
                pass
        return r
    url ="https://api.ipify.org/"
    x =UseProxy(url)
    x.text
Proxy()
