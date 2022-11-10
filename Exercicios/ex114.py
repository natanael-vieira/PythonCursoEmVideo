import urllib
import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento!')
else:
    print('Site Pudim está on-line!')
    print(site.read()) # Serve para ler o html do site.
