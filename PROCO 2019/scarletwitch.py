n = int(input())
st = input()

ans = 0

def sol(string, count):
    # print(string)
    # input()
    s = 0
    e = 0
    stopped = 0
    l = len(string)
    global ans

    if "0" * string.count("0") + "1" * string.count("1") == string:
        return count

    for i in range(l):
        # print(string[i])
        if stopped == 0 and string[i] == "1":
            s = int(i)
            stopped = 1
        if stopped == 1 and string[i] == "0":
            stopped = 2
        if stopped == 2 and string[i] == "1":
            e = int(i)
            break
        if stopped == 2 and i == l - 1:
            e = l
            # print("hi")
    # print(s, e)
    x = string[s:e]
    y = x[::-1]
    # print(string)
    # input()

    return sol(string[0:s] + y + string[e:], count + 1)

print(sol(st, 0))
