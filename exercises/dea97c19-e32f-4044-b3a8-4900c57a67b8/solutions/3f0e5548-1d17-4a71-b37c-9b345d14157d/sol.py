print('Wpisz nazwę do piramidy:')
c = str(input())
for i in range(len(c)): print(*c[0:i+1].upper())
