"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов
первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end

Sample Output 1:
3 21 22
10 6 19
20 16 -1

Sample Input 2:
1
end

Sample Output 2:
4
"""

lst, lst_res = [], []
for i in iter(input, 'end'):
    tmp = list(map(int, i.split()))
    lst.append(tmp)
    lst_res.append([0 for i in range(len(tmp))])
rng_i, rng_j = [i for i in range(len(lst))], [i for i in range(len(lst[0]))]
previous_i, next_i = [rng_i[-1]] + rng_i[:-1], rng_i[1:] + [0]
previous_j, next_j = [rng_j[-1]] + rng_j[:-1], rng_j[1:] + [0]
for i in range(len(lst)):
    for j in range(len(lst[0])):
        lst_res[i][j] = lst[previous_i[i]][j] + lst[next_i[i]][j] + lst[i][previous_j[j]] + lst[i][next_j[j]]
    print(*lst_res[i], sep=' ')





