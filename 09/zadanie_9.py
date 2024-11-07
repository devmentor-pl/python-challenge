class Uzytkownik:


uzytkownicy = [Uzytkownik("Anna", 25), Uzytkownik("Piotr", 30), Uzytkownik("Ewa", 22)]
uzytkownicy.sort()

for uzytkownik in uzytkownicy:
    print(f"{uzytkownik.imie}: {uzytkownik.wiek} lat")