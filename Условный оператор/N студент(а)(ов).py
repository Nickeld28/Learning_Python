"""
Напишите программу, которая будет получать на вход количество,
а выводить это число и правильное склонение слова "студент" латиницей ("student", "studenta", "studentov").


Между числом и словом должен быть ровно один пробел.

Sample Input:

3
Sample Output:

3 studenta
"""

n = int(input())
s = str(n) + ' student'
print(s + 'a' if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14)
      else s if n % 10 == 1 and n % 100 != 11 else s + 'ov')
