def zbroji_pa_kvadriraj(a, b):
    return (a + b) ** 2
broj1 = 3
broj2 = 4
print("Rezultat zbrajanja i kvadriranja brojeva", broj1, "i", broj2, "je:", zbroji_pa_kvadriraj(broj1, broj2))

zbroji_pa_kvadriraj_lambda = lambda a, b: (a + b) ** 2

print("Rezultat zbrajanja i kvadriranja brojeva", broj1, "i", broj2, "je (lambda):", zbroji_pa_kvadriraj_lambda(broj1, broj2))