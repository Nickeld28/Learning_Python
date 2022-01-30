domain1 = "www.yandex.ru"
domain2 = "www.youtube.com"
domain3 = "www.rutracker.org"
domain4 = "yandex.ua"

# Определим какие домены заканчиваются на ".ru"
# Для этого можно использовать метод поиска "find":

print(domain1.find(".ru"))
print(domain2.find(".ru"))
print(domain3.find(".ru"))  # Но для domain3 "find" обнаружил соответствие ".ru" в составе имени "rutracker"
print(domain4.find(".ru"))

# попробуем применить метод endswith, он проверит заканчивается ли строка на ".ru":

print(domain1.endswith(".ru"))  # endswith нашел соответствие и вывел "true"
print(domain2.endswith(".ru"))
print(domain3.endswith(".ru"))
print(domain4.endswith(".ru"))

# допустим нам надо проверить начинается ли строка с "www.",
# для этого используем метод startwith:

print(domain1.startswith("www."))  # "true" - значит, строка начинается с "www."
print(domain2.startswith("www."))  # "true" - значит, строка начинается с "www."
print(domain3.startswith("www."))  # "true" - значит, строка начинается с "www."
print(domain4.startswith("www."))  # "false" - значит, строка не начинается с "www."
