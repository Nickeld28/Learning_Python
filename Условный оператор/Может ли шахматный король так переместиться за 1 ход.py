"""
Может ли шахматный король перейти из одной клетки в другу за один ход?

Координаты каждой клетки задаются двумя числами от 1 до 8. Сначала номер столбца, потом номер строки.

В качестве результата выведите "YES" или "NO" (заглавными буквами, без кавычек).
"""

# input:
x1, y1, x2, y2 = (int(input()) for _ in range(4))

# checking for a change in any coordinate by 1
# and checking for any movement, you cannot move to the cell where you are
print("YES" if abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1 and not x2 - x1 == y2 - y1 == 0 else "NO")
