n = int(input())
st = input()

count = 0
finding = 0
for i in st:
    if i == "1":
        finding = 1
    if i == "0" and finding == 1:
        count += 1
        finding = 0

print(count)