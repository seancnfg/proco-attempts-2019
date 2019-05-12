n = int(input())
arr = list(map(int, input().split()))

print(arr)
mult = 1

for i in arr:
    mult *= i

print(mult / (arr[1] - arr[0]))