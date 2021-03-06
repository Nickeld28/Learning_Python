"""
ПОНИМАНИЕ МЕТОДОВ
Начинающий разработчик написал программу, которая получает из первого аргумента командной строки фразу,
а после вырезает из неё лишние пробелы, преобразовывает её с помощью метода title и ставит в конце точку.

Однако после запуска программы ничего не изменилось, фраза выводится в исходном виде.
Исправьте код, чтобы он работала правильно.

Пример использования:
> python title.py "Leading growth: why strategy matters"
> Leading Growth: Why Strategy Matters.

Исправить решение:
import sys

text = sys.argv[1]

# Очищаем строку, применяем title и добавляем точку.
text.strip().title() + "."

# Выводим текст.
print(text)
"""

import sys

text = sys.argv[1]

# Очищаем строку, применяем title и добавляем точку.
text.strip().title() + "."

# Дописываем строку:
text = text.strip().title() + "."

# Выводим текст.
print(text)
