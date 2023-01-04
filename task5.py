def xo(s):
    x = 0
    o = 0
    for i in s:
        if i == 'o' or i == 'O':
            o = o+1
        elif i == 'x' or i == 'X':
            x = x+1
    if x == o:
        return True

    return False

####################

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo("sdfsfsXxoo"))