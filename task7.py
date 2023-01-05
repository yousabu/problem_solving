def digital_root(n):
    result = 0
    for i in list(str(n)):
        result = result+int(i)
    return result



print(digital_root(16))