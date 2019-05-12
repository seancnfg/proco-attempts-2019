#
# a = input()
# b = input().split()
# c = []
# for i in b:
#     c.append(int(i))
# c.sort()
# d = []
# if len(c) == 1:
#     print(0)
# else:
#     while len(c) != 1:
#         c[0] = c[1] + c[0]
#         c.remove(c[1])
#         d.append(c[0])
#     c[0] = sum(d)
#     print(c[0])

a = int(input())
arr = list(map(int, input().split()))
arr.sort()
# x = 0
# found = 0
# for i in arr:
#     if i < 0:
#         found = 1
#     if i > 0 and found == 1:
#         x = i - 1 # 0 base indexing
#
# print(x)
# arr = arr[x + 1:] + arr[0:x + 1]
print(arr)

s = 0
for i in range(1, a + 1):
    # print(sum(arr[0:i]))
    s += sum(arr[0:i])

print(s - arr[0])