num = int(input())
if len(str(num)) != 3 or num % 1 != 0:
    print('Ошибка ввода, введите трехзначное целое число')
else:
    lst = []
    for i in range(3, 0, -1):
        n = (num % 10 ** i) // 10 ** (i - 1)
        lst.append(n)
    lst.append('\n')
    var = [0, 1, 2, 3, 0, 2, 1, 3, 1, 0, 2, 3, 1, 2, 0, 3, 2, 0, 1, 3, 2, 1, 0]
    for i in var:
        print(lst[i], sep='', end='')
