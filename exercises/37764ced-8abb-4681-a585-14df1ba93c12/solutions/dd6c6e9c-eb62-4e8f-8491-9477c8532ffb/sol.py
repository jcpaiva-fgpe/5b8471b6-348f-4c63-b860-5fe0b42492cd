d = {}
while True:
    print('Podaj wynik:')
    res = input().split()
    try:
        if res[0] != 'koniec':
            d[res[0]] = float(res[1])
            maxv = max(d.values())
            maxk = [k for k, v in d.items() if v == maxv] 
            print('Lider:', *maxk, maxv)
        else: break
    except:
        break