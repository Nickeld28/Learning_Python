"""
Сделайте преобразование из lowerCamelCase в snake_case.

В индентификаторах есть только буквы.

Sample Input:
camelCase

Sample Output:
camel_case
"""


def lower_camel_case_to_snake_case(text):
    """ Transform text from lowerCamelCase to snake_case
        Arg: text in lowerCamelCase, contains letters only
        Returns new_text like snake_case
    """

    new_text = []
    for sym in text:
        new_text.append(sym) if sym.islower() else new_text.append('_' + sym.lower())
    return ''.join(new_text)


sample_text = 'lowerCamelCase'
sample_text = lower_camel_case_to_snake_case(sample_text)
print(sample_text)
