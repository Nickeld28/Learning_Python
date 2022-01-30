"""
Изучите алгоритм "решето Эратосфена" для нахождения всех простых чисел от 2 до n-1

Sample Input:

100
Sample Output:

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""

n = int(input())

eratosthenes = [elem for elem in range(2, n)]

for divisor in range(2, n):
    eratosthenes = [elem for elem in eratosthenes if (elem % divisor != 0) or elem == divisor]
print(eratosthenes)
