"""
Крайние буквы
На вход программе подается слово, необходимо проверить первую и последнюю буквы в этом слове.
Если обе буквы являются буквой "ы" (в любом регистре), необходимо вывести "ыыы". Если одной из двух букв является "ы",
а другой "й" (обе буквы могут быть в любом регистре), нужно вывести "огонь".
Во всех остальных случаях нужно выводить фразу "какие-то странные буквы попались".

Sample Input:
Ыааааы

Sample Output:
ыыы
"""

s = input().lower()
edges = s[0] + s[-1]
if 'ы' in edges:
    if s[0] == s[-1]:
        print('ыыы')
    elif 'й' in edges:
        print('огонь')
    else:
        print("какие-то странные буквы попались")
else:
    print("какие-то странные буквы попались")
