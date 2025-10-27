v = 0
n = 0
for y in range(9, 14):
    for x in range(y+1, 14):
        a = int('70370', 14) + x * 14 ** 3 + y 
        b = int('9063', x) + y * x ** 2
        c = int('15148', y)
        z = a + b - c
        if z > v:
            v = z
            n = z // (x+ y)

print(n)
        