"""
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча
и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""

n = int(input())
total_table_dict = {}
for games in range(n):
    team1, team1_score, team2, team2_score = input().split(';')
    if team1 not in total_table_dict:
        total_table_dict[team1] = [1, 0, 0, 0, 0]
    else:
        total_table_dict[team1][0] += 1
    if team2 not in total_table_dict:
        total_table_dict[team2] = [1, 0, 0, 0, 0]
    else:
        total_table_dict[team2][0] += 1
    if int(team1_score) > int(team2_score):
        total_table_dict[team1][1] += 1
        total_table_dict[team1][4] += 3
        total_table_dict[team2][3] += 1
    elif int(team1_score) == int(team2_score):
        total_table_dict[team1][2] += 1
        total_table_dict[team1][4] += 1
        total_table_dict[team2][2] += 1
        total_table_dict[team2][4] += 1
    else:
        total_table_dict[team1][3] += 1
        total_table_dict[team2][1] += 1
        total_table_dict[team2][4] += 3
for team, team_results in total_table_dict.items():
    print(f'{team}:', end='')
    print(*team_results)
