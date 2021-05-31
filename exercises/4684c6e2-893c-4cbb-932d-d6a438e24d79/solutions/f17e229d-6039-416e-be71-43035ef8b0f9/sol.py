print('Podaj napis:')
napis = input().split()
d = {napis[i]: j.lower().count('a') for i, j in enumerate(napis)}
print(f'{max(d, key = d.get)}')
