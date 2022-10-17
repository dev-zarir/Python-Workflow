from requests import get, post

resp=get('https://api.ipify.org/')

print('Your IP:',resp.text)
