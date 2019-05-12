#H is a dict
def func(s):
	M = 14000605
    hash = 0
    l = len(s)
    for i in range(l - 1, -1, -1):
        hash = (2*hash + H[s[i]]) % M
    return hash

