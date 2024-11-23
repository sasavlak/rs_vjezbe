from datetime import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Godina proizvodnje: {self.godina_proizvodnje}, Kilometraža: {self.kilometraza} km")

    def starost(self):
        trenutna_godina = datetime.now().year
        print(f"Automobil je star {trenutna_godina - self.godina_proizvodnje} godina.")

auto = Automobil("Audi", "a4", 2013, 175000)
auto.ispis()
auto.starost()