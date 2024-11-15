def obrni_rjecnik(rjecnik):
    obrnuti_rjecnik = {}
    for kljuc, vrijednost in rjecnik.items():
        obrnuti_rjecnik[vrijednost] = kljuc
    return obrnuti_rjecnik

rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))