import requests
with open('C:/Users/miron/Downloads/dataset_3378_3.txt') as file:
    link = file.readline().strip()
url = 'https://stepic.org/media/attachments/course67/3.6.3/'
n = 0
while True:
    r = requests.get(link)
    n += 1
    link = url + r.text
    if 'We' in r.text:
        break
print(n)
with open('C:/Users/miron/Downloads/output.txt', 'w') as out:
    out.write(r.text)
