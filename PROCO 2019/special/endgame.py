BIGNUM = 314159265358979
MOD = 14000605

input = int(raw_input())
for j in range(input):
    for i in range(3):
        input = (512*input + 2019) % MOD
    print input