import requests
with open('C:/Users/miron/Downloads/dataset_3378_2 (1).txt') as file:
    link = file.readline().strip()
r = requests.get(link)
count_lines = r.text.splitlines()
print(len(count_lines))
print(r.text)
if 'No.' in r.text:
    print('YES')