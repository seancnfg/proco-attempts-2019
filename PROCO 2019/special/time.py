def T(num):
    x = 0
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i*i + j*j == num:
                x += 1
    return x

def I(num):
    x = 0
    while num > 0:
        if num % 10 == 0:
            x += 1
        num /= 10
    return x

def M(num):
    x = 0
    while num > 0:
        x += 1
        num /= 10
    return x

def E(num):
    x = 0
    while num > 0:
        x += num % 10
        num /= 10
    return x


for i in range(1000000000):
    input = i
    if T(input) == 12 and \
       I(input) == 4 and \
       M(input) == 8 and \
       E(input) == 16 and \
       input % 2 == 1:
       print "We're in the endgame now"
    else:
        pass