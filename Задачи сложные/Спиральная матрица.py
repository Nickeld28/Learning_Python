"""
Выведите таблицу размером n×n, заполненную числами от 1 до n**2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input:

5
Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""


n = int(input())
_list = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(i, n - i):
        _list[i][j] = _list[i][j - 1] + 1
    for j in range(i + 1, n - i):
        _list[j][n - 1 - i] = _list[j - 1][n - 1 - i] + 1
    for j in range(n - 2 - i, i - 1, -1):
        _list[n - 1 - i][j] = _list[n - 1 - i][j + 1] + 1
    for j in range(n - 2 - i, i, -1):
        _list[j][i] = _list[j + 1][i] + 1
for number in _list:
    print(' '.join(map(str, number)))

#Program Executed in  4.5366242
"""
x,y,dx,dy, m = 0,0,0,1, [[0]*n for i in range(n)]
for i in range(n*n):
    m[x][y]=str(i+1)
    if x+dx>=n or x+dx<0 or y+dy>=n or y+dy<0 or m[x+dx][y+dy]:
        dx,dy = dy,-dx
    x,y = x+dx, y+dy
print("\n".join([" ".join(i) for i in m]))
"""