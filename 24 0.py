f = open('24 0 file.txt').readline()
sogl = 'CDF'
glas = 'AU'
res = 0 
slovo = ''
for b in sogl: #проходимся по всем согласным и гласным, чтобы получить все комбинации согл|глас
    for a in glas:
        f = f.replace(b+a, '*') #Заменяем пары согл|глас на *

for i in range( len(f)):
    slovo += f[i]
    if slovo[-1] == '*':
        res = max(res, len(slovo))
    else:
        slovo = ''
print(res)

