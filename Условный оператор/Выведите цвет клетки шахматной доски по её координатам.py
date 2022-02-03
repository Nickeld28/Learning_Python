"""
Выведите цвет клетки доски по её координатам.

Координаты клетки заданы двумя числами от 1 до 8. Сначала номер столбца, потом номер строки.
"""
# input
x, y = int(input()), int(input())

# even or odd sum of coordinates will help you find the color of the cell
print("BLACK" if (x + y) % 2 == 0 else "WHITE")
