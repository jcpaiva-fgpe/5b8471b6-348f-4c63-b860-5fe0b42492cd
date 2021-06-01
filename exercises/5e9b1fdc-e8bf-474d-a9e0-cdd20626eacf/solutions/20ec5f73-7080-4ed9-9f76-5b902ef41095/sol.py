ile_dzieci = int(input('Liczba dzieci: '))
dochod_percapita = int(input('Dochód na członka: '))
plus = 500
if dochod_percapita <= 800:
    print(f'Łączny zasiłek: {plus*(ile_dzieci)}')
elif dochod_percapita > 1200:
    print(f'Łączny zasiłek: {plus*(ile_dzieci-1)}')   
else:
    niepelnosprawne = str(input('Niepełnosprawne: ')).lower()
    if niepelnosprawne == 'tak' or dochod_percapita <= 800:
        print(f'Łączny zasiłek: {plus*(ile_dzieci)}')
    else: 
        print(f'Łączny zasiłek: 0')
