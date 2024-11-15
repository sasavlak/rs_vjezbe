def filtriraj_parne(lista):
    parni_brojevi = []
    for broj in lista:
        if broj % 2 == 0:
            parni_brojevi.append(broj)
    return parni_brojevi

originalna_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista = filtriraj_parne(originalna_lista)
print(nova_lista)

#rezultat [2, 4, 6, 8, 10]