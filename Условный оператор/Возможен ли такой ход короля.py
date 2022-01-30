"""
Программисты тоже любят играть в шахматы (в основном, на компьютере), и нередко за них это делают программы.
Напишите программу, которая принимает на вход четыре числа: сначала координаты начального положения короля
на шахматной доске, затем координаты клетки, куда игрок хочет походить. Вам необходимо вывести "YES",
если игрок может походить королем из клетки в клетку за один ход, и "NO" иначе. Гарантируется,
что изначально король находится на доске. Нумерация рядов и столбцов доски начинается с 1.
"""


def can_chess_king_to_move(x1, y1, x2, y2):
    ''' Takes the coordinates of the starting and ending positions of the king on the board.
        Returns YES if such a move is possible, otherwise NO '''

    if all([value > 0 and value < 9 for value in [x1, y1, x2, y2]]) \
            and not (x1 == x2 and y1 == y2) \
            and x2 - x1 in [-1, 0, 1] \
            and y2 - y1 in [-1, 0, 1]:
        return "YES"
    return "NO"


def test_can_chess_king_to_move(function):
    '''testing can_chess_king_to_move function'''

    print("Testcase #1:", end='')
    x1, y1 = 1, 1
    x2, y2 = 2, 1
    right_answer = "YES"
    test_result = function(x1, y1, x2, y2)
    print(' OK, ' if right_answer == test_result else ' Fail, ', end='')
    print(f'right answer: {right_answer}, your answer: {test_result}')

    print("Testcase #2:", end='')
    x1, y1 = 8, 8
    x2, y2 = 7, 7
    right_answer = "YES"
    test_result = function(x1, y1, x2, y2)
    print(' OK, ' if right_answer == test_result else ' Fail, ', end='')
    print(f'right answer: {right_answer}, your answer: {test_result}')

    print("Testcase #3:", end='')
    x1, y1 = 5, 3
    x2, y2 = 6, 4
    right_answer = "YES"
    test_result = function(x1, y1, x2, y2)
    print(' OK, ' if right_answer == test_result else ' Fail, ', end='')
    print(f'right answer: {right_answer}, your answer: {test_result}')

    print("Testcase #4:", end='')
    x1, y1 = 2, 7
    x2, y2 = 1, 6
    right_answer = "YES"
    test_result = function(x1, y1, x2, y2)
    print(' OK, ' if right_answer == test_result else ' Fail, ', end='')
    print(f'right answer: {right_answer}, your answer: {test_result}')

    print("Testcase #5:", end='')
    x1, y1 = 12, 12
    x2, y2 = 13, 13
    right_answer = "NO"
    test_result = function(x1, y1, x2, y2)
    print(' OK, ' if right_answer == test_result else ' Fail, ', end='')
    print(f'right answer: {right_answer}, your answer: {test_result}')

    print("Testcase #6:", end='')
    x1, y1 = 2, 2
    x2, y2 = 4, 3
    right_answer = "NO"
    test_result = function(x1, y1, x2, y2)
    print(' OK, ' if right_answer == test_result else ' Fail, ', end='')
    print(f'right answer: {right_answer}, your answer: {test_result}')

    print("Testcase #7:", end='')
    x1, y1 = 8, 8
    x2, y2 = 8, 8
    right_answer = "NO"
    test_result = function(x1, y1, x2, y2)
    print(' OK, ' if right_answer == test_result else ' Fail, ', end='')
    print(f'right answer: {right_answer}, your answer: {test_result}')

    print("Testcase #8:", end='')
    x1, y1 = 2, 2
    x2, y2 = 7, 0
    right_answer = "NO"
    test_result = function(x1, y1, x2, y2)
    print(' OK, ' if right_answer == test_result else ' Fail, ', end='')
    print(f'right answer: {right_answer}, your answer: {test_result}')

    print("Testcase #9:", end='')
    x1, y1 = -4, -3
    x2, y2 = -3, -2
    right_answer = "NO"
    test_result = function(x1, y1, x2, y2)
    print(' OK, ' if right_answer == test_result else ' Fail, ', end='')
    print(f'right answer: {right_answer}, your answer: {test_result}')

    print("Testcase #10:", end='')
    x1, y1 = 1, 1
    x2, y2 = 0, 0
    right_answer = "NO"
    test_result = function(x1, y1, x2, y2)
    print(' OK, ' if right_answer == test_result else ' Fail, ', end='')
    print(f'right answer: {right_answer}, your answer: {test_result}')

    print("Testcase #11:", end='')
    x1, y1 = 1, 1
    x2, y2 = 0, 1
    right_answer = "NO"
    test_result = function(x1, y1, x2, y2)
    print(' OK, ' if right_answer == test_result else ' Fail, ', end='')
    print(f'right answer: {right_answer}, your answer: {test_result}')


if __name__ == "__main__":
    x1, y1 = 1, 7
    x2, y2 = 2, 6
    test_can_chess_king_to_move(can_chess_king_to_move)

    print(all([value > 0 and value < 9 for value in [x1, y1, x2, y2]]))
    print(not (x1 == x2 and y1 == y2))
    print(x2 - x1 in [-1, 0, 1])
    print(y2 - y1 in [-1, 0, 1])
