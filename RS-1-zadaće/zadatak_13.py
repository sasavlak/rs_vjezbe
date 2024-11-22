def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(lista))  

# rezultat (1, 10)


def maks_i_min(lista):
    maksimum = lista[0]
    minimum = lista[0]

    for broj in lista:
        if broj > maksimum:
            maksimum = broj
        if broj < minimum:
            minimum = broj

    return (maksimum, minimum)

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista))  

# rezultat (250, 5)

def presjek(skup_1, skup_2):
    rezultat = {element for element in skup_1 if element in skup_2}
    return rezultat

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2))  

# rezultat {4, 5}
