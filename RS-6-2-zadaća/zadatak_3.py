from pydantic import BaseModel, Field
from typing import List, TypedDict

# Definicija rječnika za stol 
class StolInfo(TypedDict):
    broj: int
    lokacija: str

# Definicija modela za Jelo
class Jelo(BaseModel):
    id: int
    naziv: str
    cijena: float

# Definicija modela za narudžbu
class RestaurantOrder(BaseModel):
    id: int
    ime_kupca: str
    stol_info: StolInfo
    jela: List[Jelo]
    ukupna_cijena: float = Field(default=0.0)

    # Metoda za automatski izračun ukupne cijene
    def izracunaj_ukupnu_cijenu(self):
        self.ukupna_cijena = sum(jelo.cijena for jelo in self.jela)

# Primjer korištenja
if __name__ == "__main__":
    # Kreiranje rječnika za stol_stol
    stol_podaci = {
        "broj": 5,
        "lokacija": "terasa"
    }

    # Kreiranje liste jela
    jela_podaci = [
        {"id": 1, "naziv": "Pizza Margherita", "cijena": 8.5},
        {"id": 2, "naziv": "Spaghetti Carbonara", "cijena": 10.0},
        {"id": 3, "naziv": "Tiramisu", "cijena": 4.5}
    ]

    # Validacija jela
    jela = [Jelo(**jelo_podaci) for jelo_podaci in jela_podaci]

    # Kreiranje narudžbe
    narudzba_podaci = {
        "id": 101,
        "ime_kupca": "Ivan Horvat",
        "stol_info": stol_podaci,
        "jela": jela
    }

    narudzba = RestaurantOrder(**narudzba_podaci)

    # Izračun ukupne cijene narudžbe
    narudzba.izracunaj_ukupnu_cijenu()

    # Ispis narudžbe
    print("Narudžba validirana:", narudzba)
