print('Liczba dzieci:')
ile_dzieci = int(input())
print('Dochód na członka:')
dochod_percapita = int(input())
plus = 500
if dochod_percapita <= 800:
    print(f'Łączny zasiłek: {plus*(ile_dzieci)}')
elif dochod_percapita > 1200:
    print(f'Łączny zasiłek: {plus*(ile_dzieci-1)}')   
else:
    print('Niepełnosprawne:')
    niepelnosprawne = input().lower()
    if niepelnosprawne == 'tak' or dochod_percapita <= 800:
        print(f'Łączny zasiłek: {plus*(ile_dzieci)}')
    else: 
        print(f'Łączny zasiłek: 0')
