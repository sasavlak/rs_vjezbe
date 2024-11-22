def pomnozi_i_potenciraj(x, y):
    return (y * 5) ** x

vrijednost = 2
eksponent = 3
print("Rezultat množenja vrijednosti", vrijednost, "s 5 i potenciranja na", eksponent, "je:", pomnozi_i_potenciraj(eksponent, vrijednost))

pomnozi_i_potenciraj_lambda = lambda x, y: (y * 5) ** x

print("Rezultat množenja vrijednosti", vrijednost, "s 5 i potenciranja na", eksponent, "je (lambda):", pomnozi_i_potenciraj_lambda(eksponent, vrijednost))