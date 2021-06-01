litera = 'A'
while True:
    print(f"Podaj słowo na literę {litera}:")
    slowo = input().upper()
    if slowo[0] == litera:
        litera = slowo[-1]
    else:
        print("Przegrałeś.")
        break
