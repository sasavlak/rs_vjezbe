from datetime import datetime
import math

class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena} eur, Količina: {self.kolicina}")

# Lista 
proizvodi = [
    Proizvod("Televizor", 4000, 5),
    Proizvod("Hladnjak", 3000, 2)
]

def dodaj_proizvod(naziv, cijena, kolicina):
    proizvod = Proizvod(naziv, cijena, kolicina)
    proizvodi.append(proizvod)

class Narudzba:
    def __init__(self, proizvodi):
        self.proizvodi = proizvodi
        self.ukupna_cijena = sum(p['cijena'] * p['kolicina'] for p in proizvodi)

    def ispis_narudzbe(self):
        narudzba_info = ", ".join(
            [f"{p['naziv']} x {p['kolicina']}" for p in self.proizvodi]
        )
        print(f"Naručeni proizvodi: {narudzba_info}, Ukupna cijena: {self.ukupna_cijena} eur")

def napravi_narudzbu(lista_proizvoda):
    if not isinstance(lista_proizvoda, list):
        print("Greška: Argument mora biti lista!")
        return None
    if not lista_proizvoda:
        print("Greška: Lista proizvoda ne smije biti prazna!")
        return None
    for proizvod in lista_proizvoda:
        if not isinstance(proizvod, dict):
            print("Greška: Svi elementi u listi moraju biti rječnici!")
            return None
        if not all(key in proizvod for key in ["naziv", "cijena", "kolicina"]):
            print(f"Greška: Proizvod {proizvod} nema sve potrebne ključeve!")
            return None
        if proizvod["kolicina"] <= 0:
            print(f"Proizvod {proizvod['naziv']} nije dostupan!")
            return None

    return Narudzba(lista_proizvoda)

novi_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

for p in novi_proizvodi:
    dodaj_proizvod(p["naziv"], p["cijena"], p["kolicina"])

print("Popis svih proizvoda:")
for proizvod in proizvodi:
    proizvod.ispis()

print("\nKreiranje narudžbe:")
narudzba_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 1}
]

narudzba = napravi_narudzbu(narudzba_proizvodi)
if narudzba:
    narudzba.ispis_narudzbe()