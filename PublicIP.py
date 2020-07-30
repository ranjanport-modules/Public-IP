#Author: amazing.python
from requests import get
ip = get('https://api.ipify.org').text
print(f'Public IP: {ip}')