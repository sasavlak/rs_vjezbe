def grupiraj_po_paritetu(lista):
    rezultat = {
        'parni': [broj for broj in lista if broj % 2 == 0],
        'neparni': [broj for broj in lista if broj % 2 != 0]
    }
    return rezultat

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(grupiraj_po_paritetu(lista))