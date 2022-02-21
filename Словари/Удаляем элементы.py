"""
DELETE
В представленном словаре количество значений в кратно двум.
Необходимо удалить из исходного словаря каждую вторую пару ключ-значение и вывести в результат получившийся словарь.

Попробуйте решить эту задачу с помощью метода del.

Sample Input:
{"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}

Sample Output:
{'key1': 'value1', 'key3': 'value3'}
"""

dictionary = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
lst = []
for k in dictionary.keys():
    lst.append(k)
for i in range(1, len(lst), 2):
    del dictionary[lst[i]]
print(dictionary)
