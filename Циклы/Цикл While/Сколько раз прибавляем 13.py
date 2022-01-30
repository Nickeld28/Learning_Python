"""
Прибавляем 13
На вход программе подается целое число, необходимо определить, сколько раз к нему можно прибавить 13,
пока оно не станет больше 284. В результате нужно вывести ответ в следующем формате:

к *исходное число* можно прибавить тринадцать *получившееся число* раз, тогда это будет удовлетворять условию

Гарантируется, что исходное число меньше 284.

Sample Input:

32
Sample Output:

к 32 можно прибавить тринадцать 19 раз, тогда это будет удовлетворять условию
"""

def count_case_add_13_before_284(number):
    '''Counting how many times we can add number 13 before 284'''

    n = number
    counter = 0
    while n < 284:
        n += 13
        counter += 1
    return counter


def test_count_case_add_13_before_284(function):
    '''testing find_power_of_4 function'''

    print("Testcase #1:", end='')
    number = -28
    counter = 24
    test_result = function(number)
    print(' OK, ' if counter == test_result else ' Fail, ', end='')
    print(f'right answer: {counter}, your answer: {test_result}')

    print("Testcase #2:", end='')
    number = 0
    counter = 22
    test_result = function(number)
    print(' OK, ' if counter == test_result else ' Fail, ', end='')
    print(f'right answer: {counter}, your answer: {test_result}')

    print("Testcase #3:", end='')
    number = 24
    counter = 20
    test_result = function(number)
    print(' OK, ' if counter == test_result else ' Fail, ', end='')
    print(f'right answer: {counter}, your answer: {test_result}')

    print("Testcase #4:", end='')
    number = 283
    counter = 1
    test_result = function(number)
    print(' OK, ' if counter == test_result else ' Fail, ', end='')
    print(f'right answer: {counter}, your answer: {test_result}')

    print("Testcase #5:", end='')
    number = 32
    counter = 20
    test_result = function(number)
    print(' OK, ' if counter == test_result else ' Fail, ', end='')
    print(f'right answer: {counter}, your answer: {test_result}')

if __name__ == "__main__":
    test_count_case_add_13_before_284(count_case_add_13_before_284)
    number = int(input("Введите число меньше 284: "))


    counter = count_case_add_13_before_284(number)
    print(f'к {number} можно прибавить тринадцать {counter} раз, тогда это будет удовлетворять условию')
