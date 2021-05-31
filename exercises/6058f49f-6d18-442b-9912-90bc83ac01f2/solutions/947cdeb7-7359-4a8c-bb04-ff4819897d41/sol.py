print('Podaj tekst:')
napis = input().split()
res = [napis[i] for i in range(len(napis)) if napis[i][-1] == '.']
print('Znaleziono skróty:', *res)
