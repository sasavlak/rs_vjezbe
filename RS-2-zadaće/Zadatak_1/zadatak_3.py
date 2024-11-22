def kvadriraj_duljinu(niz):
    return len(niz) ** 2

niz = "Raspodijeljeni_sustavi"
print("Kvadrat duljine niza", niz, "je:", kvadriraj_duljinu(niz))

kvadriraj_duljinu_lambda = lambda niz: len(niz) ** 2

print("Kvadrat duljine niza", niz, "je (lambda):", kvadriraj_duljinu_lambda(niz))