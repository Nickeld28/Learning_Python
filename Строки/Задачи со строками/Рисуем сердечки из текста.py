"""
Прочитайте число  k. Выведите сердечко в строку k раз подряд.

 .-.  .-.
|   \/   |
\        /
 `\    /`
   `\/`


Sample Input 1:
1

Sample Output 1:

 .-.  .-.
|   \/   |
\        /
 `\    /`
   `\/`

Sample Input 2:
2

Sample Output 2:
 .-.  .-.  .-.  .-.
|   \/   ||   \/   |
\        /\        /
 `\    /`  `\    /`
   `\/`      `\/`

"""
k = int(input())
heart = ' .-.  .-. ', '|   \/   |', '\        /', ' `\    /` ', '   `\/`   '
for part in heart:
    print(part * k, sep='', end='\n')
