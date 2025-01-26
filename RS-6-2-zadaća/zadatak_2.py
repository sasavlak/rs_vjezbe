from pydantic import BaseModel, EmailStr
from typing import List, Literal

# Definicija Pydantic modela za Admina
class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: EmailStr
    ovlasti: List[Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"]] = []

# Primjer validacije
if __name__ == "__main__":
    # Kreiranje podataka za admina
    admin_podaci = {
        "ime": "Ana",
        "prezime": "Anić",
        "korisnicko_ime": "admin_ana",
        "email": "ana.admin@example.com",
        "ovlasti": ["dodavanje", "čitanje"]
    }

    # Validacija podataka o administratoru
    admin = Admin(**admin_podaci)
    print("Administrator validiran:", admin)

    # Primjer bez navedenih ovlasti
    admin_podaci_bez_ovlasti = {
        "ime": "Marko",
        "prezime": "Marković",
        "korisnicko_ime": "admin_marko",
        "email": "marko.admin@example.com"
    }

    # Validacija podataka o administratoru bez ovlasti
    admin_bez_ovlasti = Admin(**admin_podaci_bez_ovlasti)
    print("Administrator bez ovlasti validiran:", admin_bez_ovlasti)
