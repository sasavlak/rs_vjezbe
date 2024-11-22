def paran_broj(x):
    if x % 2 == 0:
        return True
    else:
        return None
broj = 4
print("Broj", broj, "je paran:", paran_broj(broj))

paran_broj_lambda = lambda x: True if x % 2 == 0 else None

print("Broj", broj, "je paran (lambda):", paran_broj_lambda(broj))