def provjera_lozinke(lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova.")
        return
    
    ima_veliko_slovo = any(char.isupper() for char in lozinka)
    ima_broj = any(char.isdigit() for char in lozinka)
    if not ima_veliko_slovo or not ima_broj:
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj.")
        return

    if "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'.")
        return

    print("Lozinka je jaka!")

unos_lozinke = input("Unesite lozinku: ")
provjera_lozinke(unos_lozinke)