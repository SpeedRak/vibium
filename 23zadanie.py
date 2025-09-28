def f(n, k):
    if k == 9:
        return 1
    else:
       return f(n*2, k+1) + f(n*2+1, k+1)

print(f(1, 0))