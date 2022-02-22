"""
Прочитайте идентификатор записанный в snake_case. Превратите его в lowerCamelCase.

В индентификаторах есть только буквы и символы "_".

Sample Input:
snake_case

Sample Output:
snakeCase
"""


def snake_case_to_upper_camel_case(text):
    """ Transform text from snake_case to UpperCamelCase
        Arg: text in snake_case, contains letters and '_' only
        Returns new_text like UpperCamelCase
    """

    text = ''.join(text.title().split('_'))
    return text


sample_text = 'snake_case_snake_case'
sample_text = snake_case_to_upper_camel_case(sample_text)
print(sample_text)
