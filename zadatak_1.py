broj1 = float(input("Unesite prvi broj: "))
broj2 = float(input("Unesite drugi broj: "))
operator = input("Unesite operator (+, -, *, /): ")

if operator == "+":
    rezultat = broj1 + broj2
    print(f"Rezultat operacije {broj1} + {broj2} je {rezultat}")
elif operator == "-":
    rezultat = broj1 - broj2
    print(f"Rezultat operacije {broj1} - {broj2} je {rezultat}")
elif operator == "*":
    rezultat = broj1 * broj2
    print(f"Rezultat operacije {broj1} * {broj2} je {rezultat}")
elif operator == "/":
    if broj2 != 0:
        rezultat = broj1 / broj2
        print(f"Rezultat operacije {broj1} / {broj2} je {rezultat}")
    else:
        print("Dijeljenje s nulom nije dozvoljeno!")
else:
    print("Nepodržani operator!")