import requests
import time

url=input('Enter the url: ')
response=requests.get(f'{url}')
print(f'{response.status_code}')
a= time.sleep(10)
print(f'{response.text}')
b= time.sleep(10)
print(f'{response.json}')
c= time.sleep(10)
print(response.headers)