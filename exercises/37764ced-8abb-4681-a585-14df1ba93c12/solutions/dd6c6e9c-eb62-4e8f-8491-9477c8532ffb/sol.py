dic={}
while True:
    print('Podaj wynik:')
    res = input().split()
    dic[res[0]] = float(res[1])
    maxv = max(dic.values())
    maxk = [k for k, v in dic.items() if v == maxv] 
    print('Lider:', *maxk, maxv)
