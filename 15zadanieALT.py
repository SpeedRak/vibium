def f(x, a):
    p = 5 <= x <=54
    q = 50 <= x <=93
    return ((not p) and (q)) <= (x > a)
for a in range(1, 10000):
    c  = 0
    for x in range(100):
        if (f(x, a) == 0):
            c += 1
    if c == 20:
        print(a)
        break