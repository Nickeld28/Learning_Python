"""
Нарисуйте равнобедренный треугольник из заданных символов и заданной высоты, как в примере.

Sample Input:
'#'
3
Sample Output:
  #
 ###
#####
"""

sym = '#'
n = 5
for i in range(n):
    print((sym + sym * i * 2).center(2 * n - 1))
