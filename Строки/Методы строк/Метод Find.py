languages = "Языки: Python, PHP, SQL, HTML, Java."
langs_position = languages.find(": ")
print(langs_position)

languages = languages[langs_position + 2:]
print(languages)

second_language_start_pisition = languages.find(", ") + 2
second_language_end_pisition = languages.find(", ", second_language_start_pisition)
second_language = languages[second_language_start_pisition:second_language_end_pisition]
print(second_language)
last_language_position = languages.rfind(", ") + 2
last_language = languages[last_language_position:].strip(".")
print(last_language)
