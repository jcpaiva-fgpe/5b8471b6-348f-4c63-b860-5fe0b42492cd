przystanki = [ 'Szczecin', 'Nowogard', 'Koszalin', 'Słupsk', 'Gdynia', 'Gdańsk' ]
i = input()
j = input()
if i in przystanki and j in przystanki:
    if przystanki.index(i) < przystanki.index(j):
        print("Przystanki to:", *przystanki[przystanki.index(i)+1:przystanki.index(j)])
    else: 
        print("Przystanki to:", *przystanki[przystanki.index(j)+1:przystanki.index(i)][::-1])
else: 
    print("Brak takiego przystanku.")
