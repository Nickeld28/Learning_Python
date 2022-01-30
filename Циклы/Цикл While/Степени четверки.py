"""На вход программе подается одно число, необходимо определить,
какой степенью четверки оно является и вывести ответ в следующем виде:

*исходное число* - это 4 в *получившаяся степень* степени

Гарантируется, что введенное число является степенью четверки и не является единицей.

Sample Input:

64
Sample Output:

64 - это 4 в 3 степени
"""

def find_power_of_4(number):
    '''looking for what power of four is an integer num'''

    power = 0
    tmp_result = 1
    while tmp_result != number:
        tmp_result *= 4
        power += 1
    return power


def test_find_power_of_4(function):
    '''testing find_power_of_4 function'''

    print("Testcase #1:", end='')
    number = 64
    power = 3
    test_result = function(number)
    print('OK' if power == test_result else 'Fail')

    print("Testcase #2:", end='')
    number = 1
    power = 0
    test_result = function(number)
    print('OK' if power == test_result else 'Fail')

    print("Testcase #3:", end='')
    number = 4
    power = 1
    test_result = function(number)
    print('OK' if power == test_result else 'Fail')

    print("Testcase #4:", end='')
    number = 16
    power = 2
    test_result = function(number)
    print('OK' if power == test_result else 'Fail')

if __name__ == "__main__":
    test_find_power_of_4(find_power_of_4)
try:
    number = int(input("Введите степень четверки: "))
    print('Введено корректное число')
except(TypeError, ValueError, NameError):
    print('ошибка ввода')


power = find_power_of_4(number)
print(number, '- это 4 в', power, 'степени')
