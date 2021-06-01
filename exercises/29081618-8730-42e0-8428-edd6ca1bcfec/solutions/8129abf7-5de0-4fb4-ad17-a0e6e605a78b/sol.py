print('Podaj napis:')
s = input()
print(*[k for k in s.split() if len(k)!=4])
