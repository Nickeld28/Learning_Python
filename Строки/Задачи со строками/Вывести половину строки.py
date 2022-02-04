"""
Выведите ровно половину строки. Если в строке нечетное число элементов, то округляйте её длину вниз.

Sample Input:
hello

Sample Output:
he
"""

strng = input()
half_str = len(strng) // 2
print(strng[:half_str])
