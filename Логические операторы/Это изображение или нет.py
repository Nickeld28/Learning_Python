# ЭТО ИЗОБРАЖЕНИЕ?

# Задание
# Напишите программу, которая первым аргументом командной строки принимает название файла,
# а после выводит True если это изображение, и False в противном случае.
# Определять изображение это или нет нужно по расширению файла: png, jpeg, jpg или gif.
# Учитывайте, что имя может быть набрано в разных регистрах.
#
# Пример использования в командной строке Windows:
# > python program.py photo.png
# > True
# > python program.py photo.jpg
# > True
# > python program.py ROOM.PNG
# > True
# > python program.py video.mp4
# > False

import sys
file_name = sys.argv[1]
ft1 = file_name.lower().endswith(".png")
ft2 = file_name.lower().endswith(".jpeg")
ft3 = file_name.lower().endswith(".jpg")
ft4 = file_name.lower().endswith(".gif")
print(ft1 or ft2 or ft3 or ft4)

# можно было даже так:
# print(file_name.endswith((".png", ".jpg", ".jpeg", ".gif")))
# а на этапе получения параметра можно было привести регистр в порядок:
# filename = sys.argv[1].lower()

