"""
Установка  Python - python.org
"""
# import this - печатает Python Zen
import turtle

x = 2 ** 100
print(type(x))
print(dir(x))
y = x
print(y == x)
print(x >= 5)
print(x is y)
print(type(x is y))
print(178 / 3)
print(type(178 / 3))
y = 15 / 3
print(type(y))
y = int(y)
print(type(y))
print('Hello world')
print("Hello" + " hello")
s = "2342355.3"
# x = int(s)  # ValueError: invalid literal for int() with base 10: '2342355.3'
x = int(float(s))
print(x)
x -= 1  # декрементация
x += 1  # инкрементация
# бесконечный цикл - while True:
x = 10
while True:
    x -= 1
    if x < 0:
        break  # использование break не желательно, если есть возможность его избежать
    print(x)
print("цикл окончен")

# пример без break
x = 10
while x >= 0:
    print(x)
    x -= 1
print("цикл окончен без break")

# тоже самое с циклом for
x = 10
start = x
stop = -1
step = -1
for x in range(start, stop, step):
    print(x)
print("цикл for окончен")

x = int(input())
y = int(input())
if x > 0 and y > 0:
    print(1)
else:
    if x < 0 < y:
        print(2)
    else:
        if x < 0 and y < 0:
            print(3)
        else:
            if x < 0 and y < 0:
                print(4)
            else:
                print('Никогда!')

# существует способ записать вложенные ветвления более компактно:
if x > 0 and y > 0:
    print(1)
elif x < 0 < y:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x < 0 and y < 0:
    print(4)
else:
    print('Никогда!')


def david():
    for st in range(6):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(50)
            turtle.left(360 / 3)
        turtle.end_fill()
        turtle.forward(50)
        turtle.right(60)


turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('green', 'yellow')
turtle.speed(10)

david()
turtle.backward(200)
david()
turtle.hideturtle()

