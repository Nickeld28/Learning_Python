"""
Сыграем в упрощенную змейку.

Вы начинаете в клетке с координатами (x, y) = (0, 0) и длиной 1. Далее дается последовательность символов через пробел:

l, r, u, d — движение на одну клетку влево, вправо, вверх или вниз соответственно,

* — яблоко, которое увеличивает длину змейки на 1,

# — стена, которая уменьшает длину змейки на 1.

Выведите через пробел координаты x и y итоговой позиции змейки на момент конца игры.
На следующей строке выведите длину змейки на момент конца игры. Считается, что поле бесконечное,
а змейка не умеет кусать саму себя. То есть конец игры наступает, когда длина змейки становится равна 0,
либо когда заканчивается последовательность символов.

Sample Input 1:
l u d d * d l u r * l * # d

Sample Output 1:
-2 -2
3

Sample Input 2:
l r r * d d # r # l l l d

Sample Output 2:
2 -2
0
"""


def snake_game(script: list, x=0, y=0, length=1):
    for i in script:
        if length == 0:
            break
        elif i == 'l':
            x -= 1
        elif i == 'r':
            x += 1
        elif i == 'u':
            y += 1
        elif i == 'd':
            y -= 1
        elif i == '*':
            length += 1
        elif i == '#':
            length -= 1
    print(x, ' ', y, '\n', length, sep='')


snake_game(input().split())
