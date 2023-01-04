def persistence(n):
    if n < 10: return 0

    multiplier = 1

    while(n > 0):
        multiplier = (n % 10) * multiplier
        n = n // 10
    return persistence(multiplier) + 1