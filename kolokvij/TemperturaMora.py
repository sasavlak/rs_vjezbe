from datetime import datetime

class TemperaturaMora:
    def __init__(self, grad, temperatura_mora, datum):
        self.grad = grad
        self.temperatura_mora = temperatura_mora
        self.datum = datum

    def dnevna_promjena(self, nova_temperatura, novi_datum):
        self.temperatura_mora = nova_temperatura
        self.datum = novi_datum
#print(f"{self.datum.strftime('%d-%m-%Y')} - {self.grad}: {self.temperatura_mora}C")

   #def ispis(self)
   #print(f"{self.datum.strftime('%d-%m-%Y')} - {self.grad}: {self.temperatura_mora}C")


    def ispis(self):
        datum = self.datum.strftime ("%d-%m-%Y ")
        print(f"{datum}- {self.grad}: {self.temperatura_mora}C")

from datetime import datetime