import requests
from bs4 import BeautifulSoup
import urllib
import os
from random import choice


def get_proxy():
	proxy_url='https://www.sslproxies.org/'
	r = requests.get(proxy_url)
	soup = BeautifulSoup(r.content, 'html5lib')
	proxy = {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]),
		   									   map(lambda x:x.text, soup.findAll('td')[1::8]))))))}
	
	#print(proxy)
	return proxy


''' As we get a proxy lets do arequest using proxy '''
while True:
	try:
		proxy = get_proxy()
		url ="https://www.expressvpn.com/what-is-my-ip"		
		print('Using Proxy:{}'.format(proxy))
		r = requests.get(url, proxies=proxy, timeout=5)
		print(r.json())
		html = r.content
		soup = BeautifulSoup(html, 'html5lib')
		ip = soup.find('p', {'class': 'ip-address'})		
		break
	except:
		pass
print("Your ip is:",ip)






		    
	    

