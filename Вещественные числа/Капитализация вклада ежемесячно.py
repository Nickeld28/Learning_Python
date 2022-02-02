"""
Вы открыли вклад в банке. Положили 100000 рублей под 13% годовых.
Что если теперь проценты будут капитализироваться в конце каждого месяца?

Напишите программу, которая вычисляет сумму денег на вашем счету. Количество лет поступит на вход.

Отбросьте копейки в результате.

Для простоты считайте, что все месяцы одинаковые.

В году 12 месяцев.

Никто не будет начислять каждый месяц все 13%. Они на то и "годовые".
"""

# input data:
start_money, years, fix_percent = 100000, 5, 13 / 12
months = years * 12


def capitalization(rub, month, percent):
    """ Считает капитализацию процентов на вкладе """
    if month == 0:
        return rub
    rub = rub + rub * percent / 100
    return capitalization(rub, month - 1, percent)


# calculation:
total_money = capitalization(start_money, months, fix_percent)

# format result:
format_total_money = float('{:.2f}'.format(total_money))

# print result:
print('Итого:', format_total_money, 'руб.')
