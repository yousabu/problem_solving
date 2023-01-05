def digital_root(n):
    result = 0
    n_list = list(str(n))
    for i in n_list:
        result = result+int(i)
    if result > 9:
        result = digital_root(result)
    return result




x = digital_root(942)

print(x)


# def digital_root(n):
#     answ = 0
#     s = 0
#     x = str(n)
#     for i in range(0, len(x)):
#         s = s + int(x[i])
#     if len(str(s)) > 1:
#        s = digital_root(s)
#     answ = s # You could even return s directly
#     return answ