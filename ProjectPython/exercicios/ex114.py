import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://chatgpt.com/')
except urllib.error.URLError:
    print('O site ChatGPT não está acessível no momento.')
else:
    print('Consegui acessar o site CHATGPT com sucesso!')
  