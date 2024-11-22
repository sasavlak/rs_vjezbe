godina = int(input("Unesite godinu: "))

if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
    print(f"Godina {godina}. je prijestupna godina.")
else:
    print(f"Godina {godina}. nije prijestupna godina.")
    