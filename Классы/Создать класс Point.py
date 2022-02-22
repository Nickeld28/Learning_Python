"""
Пример создания класса Point
"""


class Point:
    """ Класс для предоставления координат точек на плоскости """
    x = 1
    y = 1


class_name = Point
print(dir(class_name))
for method in dir(class_name):
    print(method, '\t' * 7, exec('Point' + '.' + f'{method}'))

print('__doc__', ' ' * 20 + '\t', class_name.__doc__)
print('__name__', ' ' * 20 + '\t', class_name.__name__)
print('__qualname__', ' ' * 20 + '\t', class_name.__qualname__)
print('__dict__', ' ' * 20 + '\t', class_name.__dict__)
print('__base__', ' ' * 20 + '\t', class_name.__base__)
print('__bases__', ' ' * 20 + '\t', class_name.__bases__)
print('__basicsize__', ' ' * 20 + '\t', class_name.__basicsize__)
print('__init__', ' ' * 20 + '\t', class_name.__init__)
print('__call__()', ' ' * 20 + '\t', class_name.__call__())
print('__module__', ' ' * 20 + '\t', class_name.__module__)
print('__dictoffset__', ' ' * 20 + '\t', class_name.__dictoffset__)
print('__weakrefoffset__', ' ' * 20 + '\t', class_name.__weakrefoffset__)
print('__text_signature__', ' ' * 20 + '\t', class_name.__text_signature__)
print('__flags__', ' ' * 20 + '\t', class_name.__flags__)
print('__itemsize__', ' ' * 20 + '\t', class_name.__itemsize__)
print('__mro__', ' ' * 20 + '\t', class_name.__mro__)
