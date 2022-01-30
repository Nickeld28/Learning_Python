s = 'a3а344534п55п'
s += ' '
_list = []
for i in range(0, len(s)):
    if not s[i].isdigit():
        _list.append((s[i]))
    else:
        if s[i - 1].isdigit():
            continue
        tmp = s[i]
        for j in range(i + 1, len(s)):
            if s[j].isdigit():
                tmp += s[j]
            else:
                _list.append(int(tmp))
                break
_list.pop()
print(_list)
