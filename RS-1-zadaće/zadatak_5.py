# for petlja
broj = int(input("Unesite broj za izračun faktorijela: "))

faktorijel = 1

for i in range(1, broj + 1):
    faktorijel *= i

print(f"Faktorijel broja {broj} je {faktorijel}.")

# while petlja
broj = int(input("Unesite broj za izračun faktorijela: "))

faktorijel = 1
trenutni = 1

while trenutni <= broj:
    faktorijel *= trenutni
    trenutni += 1

print(f"Faktorijel broja {broj} je {faktorijel}.")