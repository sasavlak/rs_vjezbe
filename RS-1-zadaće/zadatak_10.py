def brojanje_riječi(tekst):
    riječi = tekst.split()
    
    brojač = {}
    
    for riječ in riječi:
        if riječ in brojač:
            brojač[riječ] += 1
        else:
            brojač[riječ] = 1
    
    return brojač

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan i odličan je programski jezik"
print(brojanje_riječi(tekst))
