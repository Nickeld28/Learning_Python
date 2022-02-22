"""
Шифр Цезаря заключается в замене каждого символа входной строки на символ,
находящийся на несколько позиций левее или правее его в алфавите.

Для всех символов сдвиг один и тот же. Сдвиг циклический,
т.е. если к последнему символу алфавита применить единичный сдвиг, то он заменится на первый символ, и наоборот.

Напишите программу, которая шифрует текст шифром Цезаря.

Используемый алфавит -− пробел и малые символы латинского алфавита: ' abcdefghijklmnopqrstuvwxyz'

Формат ввода:
На первой строке указывается используемый сдвиг шифрования: целое число.
Положительное число соответствует сдвигу вправо. На второй строке указывается непустая фраза для шифрования.
Ведущие и завершающие пробелы не учитывать.

Формат вывода:
Единственная строка, в которой записана фраза: Result: "..." ,
где вместо многоточия внутри кавычек записана зашифрованная последовательность.

Sample Input 1:
3
i am caesar

Sample Output 1:
Result: "lcdpcfdhvdu"

Sample Input 2:
-2
az

Sample Output 2:
Result: "zx"

Sample Input 3:
27
abc

Sample Output 3:
Result: "abc"
"""

alphabet = ' abcdefghijklmnopqrstuvwxyz'  # используемый алфавит
shift, text = int(input()), input().strip().lower()  # вводные данные, смещение и текст для зашифровки
shift_mod = abs(shift)  # смещение по модулю
# если shift выходит за пределы алфавита, возвращаем его в диапазонL: -len(alphabet) <= shift <= len(alphabet)
shift = shift % (len(alphabet) * shift // shift_mod) if (shift_mod > len(alphabet)) else shift
encryption_alphabet = alphabet[shift:] + alphabet[:shift]  # делаем смещение подстановочного алфавита
encryption_dict = {k: v for k, v in zip(alphabet, encryption_alphabet)}  # делаем словарь для шифрования
print('Result: "', end='')
for symbol in text:  # шифруем и выводим каждый символ в тексте
    print(encryption_dict[symbol], end='')
print('"')
