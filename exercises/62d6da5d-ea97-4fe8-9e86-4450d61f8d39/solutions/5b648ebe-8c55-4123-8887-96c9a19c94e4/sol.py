print("Poniżej wpisz datę w formacie DD.MM.RRRR:")
print('Twoje tymczasowe haslo to: ', sep="", *list(map(lambda x:int(x)*2, input().split('.'))))