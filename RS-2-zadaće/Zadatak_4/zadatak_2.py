class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    def dijeljenje(self):
        return self.a / self.b if self.b != 0 else "Dijeljenje s nulom nije moguće!"

    def potenciranje(self):
        return self.a ** self.b

    def korijen(self):
        return self.a ** 0.5, self.b ** 0.5

kalkulator = Kalkulator(9, 3)
print(kalkulator.zbroj())
print(kalkulator.oduzimanje())
print(kalkulator.mnozenje())
print(kalkulator.dijeljenje())
print(kalkulator.potenciranje())
print(kalkulator.korijen())