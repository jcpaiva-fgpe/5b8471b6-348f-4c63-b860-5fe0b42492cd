mies = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
print('Podaj datę urodzenia (Dzień.Miesiąc.Rok):')
print(mies[int(input().split('.')[1])-1])
