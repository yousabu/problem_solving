def solution(strng, markers):
    s_list = strng.split("\n")
    n_list = []

    for item in s_list:
        s = ""

        for char in item:
            if char in markers:
                break
            else:
                s = s + char
        n_list.append(s.rstrip())

    return "\n".join(n_list)

# print(solution(' a #b\nc\nd $e f g=', ['#', '$']))


def solution2(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)

# print(solution2(' a #b\nc\nd $e f g=', ['#', '$']))

go = "sf a sfa fsddd$ w#  #asd"

print(go.split("   "))

# From vscode
