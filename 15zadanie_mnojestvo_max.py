a = {x for x in range(1, 1000)}
def f(x, a):
    p = {x for x in range(2, 21, 2)}
    q = {x for x in range(3, 31, 3)}
    return ((x in a) <= (x not in p)) and ((x not in q) <= (x not in a))
for x in range(10000):
    if f(x, a) == 0:
        a.remove(x)
print(len(a))