while True:
    print('Wpisz poniżej nazwisko i pesel obywatela:')
    try:
        name, pesel = map(str, input().split())
        gender, last = int(pesel[9]), int(pesel[10])
        sum_psl = int(pesel[0]) + int(pesel[1]) * 3 + int(pesel[2]) * 7 + int(pesel[3]) * 9 + int(pesel[4]) + int(pesel[5]) * 3 + int(pesel[6]) * 7 + int(pesel[7]) * 9 + int(pesel[8]) + gender * 3
        d, m, r = pesel[4:6], pesel[2:4], pesel[:2]

    except ValueError: break
    
    status = (10 - sum_psl % 10)
    if status == last:
       zwroty = 'Pani' if gender % 2 == 0 else 'Pan', 'a' if gender % 2 == 0 else 'y'
       
       r = f'19{r}' if int(m) < 20 else f'20{r}'
       m = int(m) if int(m) < 20 else int(m) - 20
       m = f'0{m}' if m < 10 else str(m) 
    
       data = f'{d}.{m}.{r}'
       import datetime
       aktualnie = datetime.datetime.now()
       wiek = (aktualnie.year - int(r)) - ((aktualnie.year, aktualnie.month, aktualnie.day) > (int(r), int(m), int(d))) 

    else: break

    print(zwroty[0], f'{name.title()}, urodzon{zwroty[1]}: {data}, legitymując{zwroty[1]} się numerem PESEL: {pesel}, aktualnie ma: {wiek}', 'lat' if wiek<=21 and wiek>3 else 'lata')
    