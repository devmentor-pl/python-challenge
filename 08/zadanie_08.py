class Uzytkownik:


def znajdz_uzytkownika(imie, lista_uzytkownikow):


uzytkownicy = [Uzytkownik("Anna", 25), Uzytkownik("Piotr", 30)]
znaleziony = znajdz_uzytkownika("Piotr", uzytkownicy)
print(znaleziony.imie if znaleziony else "Nie znaleziono użytkownika")