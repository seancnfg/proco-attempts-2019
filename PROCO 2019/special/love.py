def func(num):
	x = 0
	for i in range(1, num + 1):
		if num % i == 0:
			x += 1
	return x

count = 1
for i in range(5000):
    if func(i) == 32:
        print(count, i, func(i))
        count += 1
# print(func(840))

