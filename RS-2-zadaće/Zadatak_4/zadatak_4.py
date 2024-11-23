import math

class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return 2 * math.pi * self.r

    def povrsina(self):
        return math.pi * self.r ** 2

krug = Krug(10)
print(f"Opseg kruga: {krug.opseg():.2f}")
print(f"Površina kruga: {krug.povrsina():.2f}")