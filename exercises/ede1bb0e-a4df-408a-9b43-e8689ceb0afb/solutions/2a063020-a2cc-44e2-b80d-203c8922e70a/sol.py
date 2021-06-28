day = int(input("Wpisz dzień urodzin:\n"))
month = input("Wpisz miesiąc urodzin (np. luty, maj itd.):\n")

if month == 'grudzień':
	astro_sign = 'Strzelec' if (day < 22) else 'Koziorożec'
elif month == 'styczeń':
	astro_sign = 'Koziorożec' if (day < 20) else 'Wodnik'
elif month == 'luty':
	astro_sign = 'Wodnik' if (day < 19) else 'Ryby'
elif month == 'marzec':
	astro_sign = 'Ryby' if (day < 21) else 'Baran'
elif month == 'kwiecień':
	astro_sign = 'Baran' if (day < 20) else 'Byk'
elif month == 'maj':
	astro_sign = 'Byk' if (day < 21) else 'Bliźnięta'
elif month == 'czerwiec':
	astro_sign = 'Bliźnięta' if (day < 21) else 'Rak'
elif month == 'lipiec':
	astro_sign = 'Rak' if (day < 23) else 'Lew'
elif month == 'sierpień':
	astro_sign = 'Lew' if (day < 23) else 'Panna'
elif month == 'wrzesień':
	astro_sign = 'Panna' if (day < 23) else 'Waga'
elif month == 'październik':
	astro_sign = 'Waga' if (day < 23) else 'Skorpion'
elif month == 'listopad':
	astro_sign = 'Skorpion' if (day < 22) else 'Strzelec'
print("Twój znak zodiaku to:",astro_sign)
