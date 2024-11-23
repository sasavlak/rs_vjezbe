class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}.")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}.")

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"Povećana plaća radnika {radnik.ime} na {radnik.placa}.")

radnik = Radnik("Nikola", "Inženjer", 5000)
manager = Manager("Lucia", "Manager", 10000, "Razvoj")

radnik.work()
manager.work()
manager.give_raise(radnik, 1000)