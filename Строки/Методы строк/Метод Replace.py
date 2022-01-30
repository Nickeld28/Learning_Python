animal = "жыраф Шырокий"
animal = animal.replace("жы", "ши").replace("шы", "ши").replace("Шы", "Ши").title()
print(animal)

# или для простоты чтения кода можно писать так:

animal = "жыраф Шырокий"
animal = animal. \
    replace("жы", "ши"). \
    replace("шы", "ши"). \
    replace("Шы", "Ши"). \
    title()
print(animal)
