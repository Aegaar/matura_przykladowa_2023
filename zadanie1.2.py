# nazwa_pliku = "dane/szachy_przyklad.txt"
nazwa_pliku = "dane/szachy.txt"

with open(nazwa_pliku, 'r', encoding="utf-8") as plik:
    wiersze = [wiersz.strip() for wiersz in plik.readlines()]

plansze = []

for i in range(0, len(wiersze), 9):
    plansza = []
    for j in range(8):
        plansza.append(wiersze[i + j])
    plansze.append(plansza)

licznik = 0
min_liczba_birek_w_stanie_rownowagi = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

for plansza in plansze:
    użyte_pionki_małe = []
    użyte_pionki_duze = []
    for kolumna in range(8):
        for wiersz in range(8):
            if plansza[wiersz][kolumna] != ".":
                if plansza[wiersz][kolumna].islower():
                    pionki_wielka_litera = plansza[wiersz][kolumna].upper()
                    użyte_pionki_małe.append(pionki_wielka_litera)
                else:
                    użyte_pionki_duze.append(plansza[wiersz][kolumna])

    użyte_pionki_duze.sort()
    użyte_pionki_małe.sort()
    if użyte_pionki_duze == użyte_pionki_małe:
        licznik += 1
        liczba_birek_w_stanie_rownowagi = len(użyte_pionki_duze) + len(użyte_pionki_małe)
        if liczba_birek_w_stanie_rownowagi < min_liczba_birek_w_stanie_rownowagi:
            min_liczba_birek_w_stanie_rownowagi = liczba_birek_w_stanie_rownowagi
        # licznik += 1

print(licznik, min_liczba_birek_w_stanie_rownowagi)
