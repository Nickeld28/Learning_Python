# Простой список покупок
mylist = []
print("Enter 5 items on shopping list")
# range starts from 0 and ends at 5-1 (so 0, 1, 2, 3, 4 executes your loop contents 5 times)
for i in range(5):
    shopping = input()
    mylist.append(shopping)
    # add input to the list
print(mylist)  # at this point your list contains the 5 things entered by user

m = []
for i in range(10):
    n = int(input())
    m.append(n)
print(sum(m))
