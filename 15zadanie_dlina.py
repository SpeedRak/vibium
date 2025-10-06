def f(x, a):
    d = 7 <= x <= 68
    c = 29 <= x <= 100
    return (d) <= (((not c) and (not a)) <= (not d))
res = 10**10
for nach in range(1, 1000):
    for kon in range(nach, 1000):
        if all(f(x, nach <= x <= kon) for x in range(1000)):
            res = min(kon - nach, res)
print(res)