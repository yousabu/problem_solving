def digital_root(n):
    n_list = list(str(n))
    result = 0
    for i in n_list:
        result = result+int(i)

    print(result)



digital_root(16)