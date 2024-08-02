# nazwa_pliku = "dane/szachy_przyklad.txt"
# nazwa_pliku = "dane/szachy_test.txt"
nazwa_pliku = "dane/szachy.txt"

with open(nazwa_pliku, 'r', encoding="utf-8") as plik:
    wiersze = [wiersz.strip() for wiersz in plik.readlines()]

plansze = []

for i in range(0, len(wiersze), 9):
    plansza = []
    for j in range(8):
        plansza.append(wiersze[i + j])
    plansze.append(plansza)

def czy_szach(krol, wieza):
    szach = 0
    for plansza in plansze:
        flag = True
        while flag:
            for kolumna in range(8):
                for wiersz in range(8):
                    if plansza[wiersz][kolumna] == krol:
                        for prawo in range(kolumna + 1, 8):
                            if plansza[wiersz][prawo] == wieza:
                                szach += 1
                                flag = False
                            if plansza[wiersz][prawo] != "." and plansza[wiersz][prawo] != wieza:
                                break
                        for lewo in range(kolumna)[::- 1]:
                            if plansza[wiersz][lewo] == wieza:
                                szach += 1
                                flag = False
                            if plansza[wiersz][lewo] != "." and plansza[wiersz][lewo] != wieza:
                                break
                        for gora in range(wiersz)[::-1]:
                            if plansza[gora][kolumna] == wieza:
                                szach += 1
                                flag = False
                            if plansza[gora][kolumna] != "." and plansza[gora][kolumna] != wieza:
                                break
                        for dol in range(wiersz + 1, 8):
                            if plansza[dol][kolumna] == wieza:
                                szach += 1
                                flag = False
                            if plansza[dol][kolumna] != "." and plansza[dol][kolumna] != wieza:
                                break
                        if flag:
                            flag = False
    return szach

print(czy_szach("k", "W"))
print(czy_szach("K", "w"))

# szach_biały = 0
# szach_czarny = 0
#
# for plansza in plansze:
#     flag = True
#     while flag:
#         for kolumna in range(8):
#             for wiersz in range(8):
#                 if plansza[wiersz][kolumna] == "k":
#                     for prawo in range(kolumna + 1, 8):
#                         if plansza[wiersz][prawo] == "W":
#                             szach_biały += 1
#                             flag = False
#                         if plansza[wiersz][prawo] != "." and plansza[wiersz][prawo] != "W":
#                             break
#                     for lewo in range(kolumna)[::- 1]:
#                         if plansza[wiersz][lewo] == "W":
#                             szach_biały += 1
#                             flag = False
#                         if plansza[wiersz][lewo] != "." and plansza[wiersz][lewo] != "W":
#                             break
#                     for gora in range(wiersz)[::-1]:
#                         if plansza[gora][kolumna] == "W":
#                             szach_biały += 1
#                             flag = False
#                         if plansza[gora][kolumna] != "." and plansza[gora][kolumna] != "W":
#                             break
#                     for dol in range(wiersz + 1, 8):
#                         if plansza[dol][kolumna] == "W":
#                             szach_biały += 1
#                             flag = False
#                         if plansza[dol][kolumna] != "." and plansza[dol][kolumna] != "W":
#                             break
#                 if plansza[wiersz][kolumna] == "K":
#                     for prawo in range(kolumna + 1, 8):
#                         if plansza[wiersz][prawo] == "w":
#                             szach_czarny += 1
#                             flag = False
#                         if plansza[wiersz][prawo] != "." and plansza[wiersz][prawo] != "w":
#                             break
#                     for lewo in range(kolumna)[::- 1]:
#                         if plansza[wiersz][lewo] == "w":
#                             szach_czarny += 1
#                             flag = False
#                         if plansza[wiersz][lewo] != "." and plansza[wiersz][lewo] != "w":
#                             break
#                     for gora in range(wiersz)[::-1]:
#                         if plansza[gora][kolumna] == "w":
#                             szach_czarny += 1
#                             flag = False
#                         if plansza[gora][kolumna] != "." and plansza[gora][kolumna] != "w":
#                             break
#                     for dol in range(wiersz + 1, 8):
#                         if plansza[dol][kolumna] == "w":
#                             szach_czarny += 1
#                             flag = False
#                         if plansza[dol][kolumna] != "." and plansza[dol][kolumna] != "w":
#                             break
#                     if flag:
#                         flag = False
# print(szach_biały, szach_czarny)
