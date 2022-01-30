"""
Времена года
Напишите программу, которая вводит номер месяца и выводит название времени года на английском языке.
При вводе неверного номера месяца должно быть выведено слово 'NO'.

Входные данные
Входная строка содержит единственное число – номер месяца (возможно, неверный).

Выходные данные
Нужно вывести название времени года (на английском языке), соответствующее введённому номеру месяца
('winter' – зима, 'spring' – весна, 'summer' – лето, 'autumn' – осень).
Если введён неверный номер месяца, программы должна вывести слово 'NO'.

Sample Input 1:

4
Sample Output 1:

spring
Sample Input 2:

25
Sample Output 2:

NO
"""

def what_season(mounth_number: int):
    """returns season by month_number or "NO" if month_number is incorrect"""
    season = {(3, 4, 5): 'spring', (6, 7, 8): 'summer', (9, 10, 11): 'autumn', (1, 2, 12): 'winter'}
    for key in season:
        if mounth_number in key:
            return season[key]
    return 'NO'


print(what_season(int(input())))
