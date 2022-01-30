import requests

r = requests.get('http://example.com')  # простой get запрос
print(r.text)                           # вывод ответа от сервера

url = 'http://example.com'
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=par)       # передача параметров в запрос
print(r.url)    # Сформированный url-адрес с учетом параметров GET запроса
