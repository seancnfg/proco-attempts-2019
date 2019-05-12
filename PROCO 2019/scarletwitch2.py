
def rev(str, ans):
    if len(str) == "1":
        return ans
    i = 0
    while i < len(str):
        if str[i] == '1':
            while str[i+1] == "1" and i+1 < len(str):
                i += 1
            while str[i+1] == "0" and i+1 < len(str):
                i += 1
        break

