from TemperturaMora import TemperaturaMora
from datetime import datetime, timedelta
import asyncio
import random

grad = "Zadar"
temperatura = 16.5
datum_rodjenja = datetime(1985, 6, 25)

temperatura_mora = TemperaturaMora(grad, temperatura, datum_rodjenja)

temperatura_mora.ispis()

import asyncio
import random
import time

async def simuliraj_temperaturu(broj_dana: int, isSummer: bool):
    rezultat = []
    for dan in range(1, broj_dana + 1):
        temperatura = 0

        if isSummer:
            temperatura = random.randint(20, 30)
        else:
            temperatura = random.randint(10, 20)
        rezultat.append((dan, temperatura))
        print(f"Dan {dan}: {temperatura}C")
        await asyncio.sleep(0.1)
    return rezultat

async def simuliraj_ljetovanje(ljetni_dani, instanca):
    print("\n--- Simulacija ljetovanja u kolovozu 2025. ---")
    novi_datum = instanca.datum

    for dan, nova_temperatura in ljetni_dani:
        novi_datum += timedelta(days=1)
        instanca.dnevna_promjena(nova_temperatura, novi_datum) 
        await asyncio.sleep(0.1)

async def main():

    broj_dana = 10
    print("--- Simulacija za 30 ljetnih dana ---")
    ljetni_dani = await simuliraj_temperaturu(30, True)
    print("\nLjetni dani (dan, temperatura):", ljetni_dani)

    grad = "Dubrovnik"
    pocetna_temperatura = 25.0
    datum_pocetak = datetime(2025, 8, 1)

    more = TemperaturaMora(grad, pocetna_temperatura, datum_pocetak)
    more.ispis()

    await simuliraj_ljetovanje(ljetni_dani, more)
    
    print("\n--- Sekvencijalno izvršavanje ---")
    start_time = time.perf_counter()

    rezultat_ljeto = await simuliraj_temperaturu(broj_dana, True)
    rezultat_zima = await simuliraj_temperaturu(broj_dana, False)

    end_time = time.perf_counter()
    sekvencijalno_vrijeme = round(end_time - start_time, 1)

    print("\nLjeto (sekvencijalno):", rezultat_ljeto)
    print("Zima (sekvencijalno):", rezultat_zima)
    print(f"Vrijeme sekvencijalnog izvršavanja: {sekvencijalno_vrijeme} s")

    print("\n--- Konkurentno izvršavanje ---")
    start_time = time.perf_counter()
    
    task1 = asyncio.create_task(simuliraj_temperaturu(broj_dana, True))
    task2 = asyncio.create_task(simuliraj_temperaturu(broj_dana, False))

    rezultat_ljeto, rezultat_zima = await asyncio.gather(task1, task2)

    end_time = time.perf_counter()
    konkurentno_vrijeme = round(end_time - start_time, 1)

    print("\nLjeto (konkurentno):", rezultat_ljeto)
    print("Zima (konkurentno):", rezultat_zima)
    print(f"Vrijeme konkurentnog izvršavanja: {konkurentno_vrijeme} s")

    if sekvencijalno_vrijeme > konkurentno_vrijeme:
        print("\nKonkurentno izvršavanje je brže.")
    else:
        print("\nSekvencijalno izvršavanje je brže.")

if __name__ == "__main__":
    asyncio.run(main())