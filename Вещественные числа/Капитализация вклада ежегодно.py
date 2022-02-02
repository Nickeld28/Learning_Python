"""
Вы открыли вклад в банке. Положили 100000 рублей под 11% годовых. Капитализация процентов происходит раз в год.
Какая сумма будет у вас через несколько лет?

Напишите программу, которая вычисляет сумму денег на вашем счету. Количество лет поступит на вход.

Для простоты считайте, что нет разницы между високосными и не високосными годами.

Капитализация процентов означает, что прибыль по вкладу будет добавлена в конце периода к тому же вкладу.
И в следующем периоде проценты будут начислены уже на большую сумму.
"""
# input data:
start_money, years, fix_percent = 100000, 5, 11


def capitalization(rub, year, percent):
    """ Считает капитализацию процентов на вкладе """
    if year == 0:
        return rub
    rub = rub + rub * percent / 100
    return capitalization(rub, year - 1, percent)


# calculation:
total_money = capitalization(start_money, years, fix_percent)

# format result:
format_total_money = float('{:.2f}'.format(total_money))

# print result:
print('Итого:', format_total_money, 'руб.')
