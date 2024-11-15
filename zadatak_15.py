def brojsamsu(tekst):
    samoglasnici = ("aeiouAEIOU")
    
    broj_samoglasnika = 0
    broj_suglasnika = 0

    for znak in tekst:
        if znak.isalpha():
            if znak in samoglasnici:
                broj_samoglasnika += 1
            else:
                broj_suglasnika += 1

    return {'samoglasnika': broj_samoglasnika, 'suglasnika': broj_suglasnika}

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan i odličan programski jezik."
print(brojsamsu(tekst))