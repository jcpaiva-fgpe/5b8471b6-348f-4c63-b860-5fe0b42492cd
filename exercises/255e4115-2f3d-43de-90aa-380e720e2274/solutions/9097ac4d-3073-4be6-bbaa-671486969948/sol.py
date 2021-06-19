while True:
    print('Wpisz poniżej nazwisko i pesel obywatela:')
    try:
        name, pesel = map(str, input().split())
        plec, last = map(int, pesel[9:])
        sum_psl = sum([int(pesel[i])*j for i, j in enumerate([i for i in [1,3,7,9]*3][:-2])]) 
        d, m, r = pesel[4:6], pesel[2:4], pesel[:2]
    
    except ValueError: break
    
    status = (10 - sum_psl % 10)
    if status == last:
       zwroty = 'Pani' if plec % 2 == 0 else 'Pan', 'a' if plec % 2 == 0 else 'y'
       
       r = f'19{r}' if int(m) < 20 else f'20{r}'
       m = int(m) if int(m) < 20 else int(m)-20
       m = f'0{m}' if m < 10 else str(m) 
       
       data = f'{d}.{m}.{r}'
       from datetime import datetime
       tday = datetime.now()
       wiek = (tday.year - int(r)) - ((tday.year, tday.month, tday.day) > (int(r), int(m), int(d)))

    else: break
    
    print(zwroty[0], f'{name.title()}, urodzon{zwroty[1]}: {data}, legitymując{zwroty[1]} się numerem PESEL: {pesel}, aktualnie ma: {wiek}', 'lat' if wiek<=21 and wiek>3 else 'lata')
