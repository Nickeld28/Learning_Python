s = 'a3b4c2e10b1'
_list = [int(i) for i in s if i.isdigit()]
_string = ''.join(str(i) for i in _list)
print(_list)
print(_string)
