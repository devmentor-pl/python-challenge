class Uzytkownik:

def wyszukaj_uzytkownikow(fraza, lista_uzytkownikow):


uzytkownicy = [Uzytkownik("Anna", 25), Uzytkownik("Piotr", 30), Uzytkownik("Aneta", 28)]
wynik = wyszukaj_uzytkownikow("an", uzytkownicy)

for u in wynik:
    print(u.imie)