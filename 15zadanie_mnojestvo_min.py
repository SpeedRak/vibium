a = set()
def f(x, a):
    q = {1, 12}
    p = {12, 13, 14, 15, 16}
    return (x not in a) <= ( (x not in q) and (x not in p))
for x in range(1000):
    if f(x, a) == 0:
        a.add(x)
print(len(a))
