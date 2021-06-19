while True:
    print('Wpisz nazwisko i numer PESEL:')
    try:
        name, pesel = map(str, input().split())
        
        # wzor: 1*a + 3*b + 7*c + 9*d + 1*e + 3*f + 7*g + 9*h + 1*i + 3*j,
        sum_psl = sum([int(pesel[i])*j for i, j in enumerate([i for i in [1,3,7,9]*3][:-2])])
        plec, last = map(int, pesel[9:])
        r, m, d = map(str, [pesel[i:i+2] for i in range(0,5,2)])
        
    
    except ValueError: break
    
    status = 10 - int(str(sum_psl)[-1])
    if status == last:
       zwroty = 'Pani' if plec % 2 == 0 else 'Pan', 'a' if plec % 2 == 0 else 'y'
       
       r = f'19{r}' if int(m) < 20 else f'20{r}'
       m = int(m) if int(m) < 20 else int(m) - 20
       m = f'0{m}' if m < 10 else str(m) 
       
       data = f'{d}.{m}.{r}'
       import datetime
       tday = datetime.datetime.now()
       wiek = (tday.year - int(r)) - ((tday.month, tday.day) < (int(m), int(d)))

    else: break

    print(zwroty[0], f'{name.title()}, urodzon{zwroty[1]}: {data}, legitymując{zwroty[1]} się numerem PESEL: {pesel}, aktualny wiek w latch: {wiek}')