"""
Проверьте, является ли прочитанная строка палиндромом.

Палиндром -- это строка, которая читается одинаково слева направо и справа налево.
Пробелы это тоже символы, "СЕТУЙ УТЕС" это не то же самое что "СЕТУ ЙУТЕС",
поэтому в этой задаче эта строка полиндромом не является.

В качестве результата выведите "YES" или "NO" без кавычек.

Sample Input 1:
rotor

Sample Output 1:
YES

Sample Input 2:
python

Sample Output 2:
NO
"""

strng = input()
print("YES" if strng == ''.join(reversed(strng)) else "NO")
