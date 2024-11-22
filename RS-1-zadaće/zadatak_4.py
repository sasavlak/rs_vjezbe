broj = 0
while broj < 5:
    broj +=2
    print(broj)

#Svaki put kad se uđe u petlju broj se povećava za 2, zatim se ispisuje trenutna vrijednost, 
#kada broj postane 6, uvjet broj < 5 više nije zadovoljen i petlja se završava.


broj = 0
while broj < 5:
    broj += 1
    print(broj)
    broj -= 1

#Svaki put kada povećamo vrijednost broj broj += 1, nakon toga vraćamo vrijednost na početnu broj -= 1, 
#što znači da uvjet broj < 5 nikada neće postati False i petlja se nikada ne zaustavlja.


broj = 10
while broj > 0:
    broj -= 1
    print(broj)
#    if broj < 5 and broj > 0:
    broj += 2

#Kada broj dosegne vrijednost 4 izvršava se broj += 2 i broj se vraća na 5. 
#Ovo uzrokuje beskonačnu petlju jer se broj, ne može smanjiti do 0 zbog uvjeta broj < 5 i dodavanja broja 2.