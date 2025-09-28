def f(x, a):
    return (a % 9 == 0) and (  (280 % x == 0) <= ((a%x!=0)  <=  (730%x!=0))  )
a = 1
while True:
    if all(for x in range(1, 1001) f(x, a)):
        print(a)
        break
    a += 1