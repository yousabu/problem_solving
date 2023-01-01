def balanced_parens(n):
    ans = []
    def generate(parens, opens, closes):
        if opens == n and closes == n:
            ans.append(parens)
            return
        elif opens == n:
            ans.append(parens+")"*(n-closes))
            return

        if opens > closes:
            generate(parens + ")", opens, closes + 1)
        generate(parens + "(", opens+1, closes)

    generate("", 0, 0)
    return ans

print(balanced_parens(3))



