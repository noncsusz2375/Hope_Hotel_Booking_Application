import datetime

print("Üdvözlöm a nevem Hope!")

print("Én vagyok a virtuális asszisztense az ügyintézéshez a Hope Hotelben.")

print("Kérem válasszon az alábbi opciók közül.")

print("Segítségül egy kis instrukcióval tudok szolgálni, hogy gördülékenyen menjen az ügyintézés. Az alábbiakban kiválaszthatja az ön számára megfelelő opciót. Ehhez be kell írnia az ön általad válaszott opció számát pont nélkül. Az opció véglehesítéséhez kérem nyomjon entert és válaszoljon a további kérdésekre.")

# Absztrakt Szoba osztály
class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

# EgyagyasSzoba osztály
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)

# KetagyasSzoba osztály
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)

# Szalloda osztály
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)


    def foglalas_hozzaad(self, szobaszam, datum):

        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if not any(foglalas.szobaszam == szobaszam and foglalas.datum == datum for foglalas in self.foglalasok):
                    self.foglalasok.append(Foglalas(szobaszam, datum))
                    return szoba.ar
        return None  # Ha a szoba nem létezik, None visszaadása
    
    def foglalas_lemond(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def foglalasok_listazasa(self):
        return self.foglalasok

    def szobak_listazasa(self):
        return self.szobak

# Foglalás osztály
class Foglalas:
    def __init__(self, szobaszam, datum):
        self.szobaszam = szobaszam
        self.datum = datum

    def __str__(self):
        return f"Foglalás: Szobaszám: {self.szobaszam}, Dátum: {self.datum}"

def felhasznalo_interfesz(szalloda):
 while True:
    print("Válasszon az alábbi opciók közül:")
    print("1. Szoba foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások megtekintése")
    print("4. Kilépés")
    valasz = input("Kérem válasszon egy opciót: ")
    if valasz == '1':
        print("Hotelünkben az alábbi szobák állnak rendelkezésre: 101, 102, 103.")
        szobaszam = input("Kérem adja meg a szobaszámot: ")
        szoba_elerheto = False
        for szoba in szalloda.szobak_listazasa():
            if szoba.szobaszam == szobaszam:
                szoba_elerheto = True

        while not szoba_elerheto:
            print("A megadott szoba nem elérhető, alábbi szobák állnak rendelkezésre: 101, 102, 103.")
            szobaszam = input("Kérem adja meg a szobaszámot: ")
            for szoba in szalloda.szobak_listazasa():
                if szoba.szobaszam == szobaszam:
                    szoba_elerheto = True

        while True:
            datum = input("Kérem adja meg a dátumot (YYYY-MM-DD): ")
            try:
                datum = datetime.datetime.strptime(datum, "%Y-%m-%d").date()
                if datum >= datetime.date.today():
                    break
                else:
                    print("A foglalás dátuma nem lehet a múltban.")
            except ValueError:
                print("Érvénytelen dátumformátum. Kérem, próbálja újra.")

        ar = szalloda.foglalas_hozzaad(szobaszam, datum)
        if ar is None:
            print("Az ön által kiválasztott szoba nem létezik, kérem módosítsa a szoba számot.")
        elif ar:
            print(f"Köszönjük, hogy a Hope Hotelt választotta. Foglalását rögzítettük. A választott szoba ára: {ar} Ft")
        else:
            print("Sajnáljuk, a szoba nem elérhető ezen a napon.")

    elif valasz == '2':
        szobaszam = input("Kérem adja meg a szobaszámot: ")
        datum = input("Kérem adja meg a dátumot (YYYY-MM-DD): ")
        try:
            datum = datetime.datetime.strptime(datum, "%Y-%m-%d").date()
            if szalloda.foglalas_lemond(szobaszam, datum):
                print("Foglalás sikeresen lemondva.")
            else:
                print("Sajnáljuk, nincs ilyen foglalás.")
        except ValueError:
            print("Érvénytelen dátumformátum!")

    elif valasz == '3':
        foglalasok = szalloda.foglalasok_listazasa()
        if foglalasok:
            for foglalas in foglalasok:
                print(foglalas)  # Itt fog szépen kiíródni minden foglalás
        else:
            print("Nincsenek jelenlegi foglalások.")

    elif valasz == '4':
        break

    else:
        print("Érvénytelen opció.")


# Adatok inicializálása és futtatás
szalloda = Szalloda("Best Hotel")
szalloda.szoba_hozzaad(EgyagyasSzoba("101", 15000))
szalloda.szoba_hozzaad(KetagyasSzoba("102", 20000))
szalloda.szoba_hozzaad(EgyagyasSzoba("103", 18000))

# Teszt foglalások
szalloda.foglalas_hozzaad("101", datetime.date.today() + datetime.timedelta(days=10))
szalloda.foglalas_hozzaad("102", datetime.date.today() + datetime.timedelta(days=20))
szalloda.foglalas_hozzaad("103", datetime.date.today() + datetime.timedelta(days=30))
szalloda.foglalas_hozzaad("101", datetime.date.today() + datetime.timedelta(days=40))
szalloda.foglalas_hozzaad("102", datetime.date.today() + datetime.timedelta(days=50))

felhasznalo_interfesz(szalloda)
