# file_name = "dane/szachy_przyklad.txt"
file_name = "dane/szachy.txt"

with open(file_name, "r", encoding='utf-8') as file:
    wiersze = [letter.strip() for letter in file.readlines()]

plansze = []

for i in range(0, len(wiersze), 9):
    plansza = []
    for j in range(8):
        plansza.append(wiersze[i + j])
    plansze.append(plansza)

# print(plansze)

ile_plansz_z_co_najmniej_jedną_pustą_kolumną = 0
ile_max_pustych_kolumn_na_jednej_planszy = 0

for plansza in plansze:
    ile_pustych_na_danej_planszy = 0
    for kolumna in range(0,8):
        ma_pusta_kolumne = True
        for wiersz in range(0, 8):
            if plansza[wiersz][kolumna] != ".":
                ma_pusta_kolumne = False
                break
        if ma_pusta_kolumne:
           ile_pustych_na_danej_planszy += 1
    if ile_pustych_na_danej_planszy > 0:
        ile_plansz_z_co_najmniej_jedną_pustą_kolumną += 1
        if ile_pustych_na_danej_planszy > ile_max_pustych_kolumn_na_jednej_planszy:
            ile_max_pustych_kolumn_na_jednej_planszy = ile_pustych_na_danej_planszy


print(ile_plansz_z_co_najmniej_jedną_pustą_kolumną, ile_max_pustych_kolumn_na_jednej_planszy)