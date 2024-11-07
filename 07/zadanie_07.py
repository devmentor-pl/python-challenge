class Uzytkownik:


class PremiumUzytkownik(Uzytkownik):


class Administrator(Uzytkownik):



admin = Administrator("Ewa", 40)
premium_user = PremiumUzytkownik("Piotr", 30, "Gold")
przywitaj_uzytkownika(admin)
przywitaj_uzytkownika(premium_user)