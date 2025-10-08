def f(x, e):
    d = 150 <= x <= 400
    c = 210 <= x <= 630
    a = 70 <= x <= e
    return (d) <= (((not c) and (not a)) <= (not d))
e = 0
for e in range(100000):
    if all(f(x, e) for x in range(1000)):
        print(e/10)
        break
    
        

