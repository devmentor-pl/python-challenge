pracownicy = ["Anna - Manager", "Piotr - Programista", "Ewa - Asystent"]
slownik_pracownikow = {p.split(" - ")[0]: p.split(" - ")[1] for p in pracownicy}

print(slownik_pracownikow)
