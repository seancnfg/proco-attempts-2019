import string
s = input()
x = 0
ans = "."
for i in list(string.ascii_lowercase):
    # print(s.count(i))
    if s.count(i) > x:
        x = s.count(i)
        ans = i

print(ans)
print(s)