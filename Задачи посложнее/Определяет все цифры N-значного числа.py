# формула первой цифры n-значного числа:
# (num % 10 ** n) // 10 ** (n - 1)

num = 123
n = (len(str(num)))
for i in range(n, 0, -1):  # вывод в другом порядке: for i in range(1, n + 1):
    n_i = (num % 10 ** i) // 10 ** (i - 1)
    print(n_i)

# сумма всех цифр любого числа:
s = 0
for i in range(1, n + 1):
    n_i = (num % 10 ** i) // 10 ** (i - 1)
    s += n_i
print(s)

# перестановка всех цифр числа в обратрном порядке:
for i in range(1, n + 1):
    n_i = (num % 10 ** i) // 10 ** (i - 1)
    print(n_i, end='')

# или можно проще сделать через строку:
print('\n', str(num)[:: -1], sep='')

# выводит все цифры через разделитель:
list = []
for i in range(n, 0, -1):
    n_i = (num % 10 ** i) // 10 ** (i - 1)
    list.append(n_i)
print(*list, sep=', ')
