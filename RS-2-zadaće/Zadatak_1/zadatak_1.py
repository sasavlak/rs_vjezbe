def kvadriraj(x):
    return x ** 2

broj = 5
print("Kvadrat broja", broj, "je:", kvadriraj(broj))

kvadriraj_lambda = lambda x: x ** 2

print("Kvadrat broja", broj, "je (lambda):", kvadriraj_lambda(broj))
