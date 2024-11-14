import random

def hirsipuu():
    # lista sanoista
    listasanoja = ['auto', 'kalmari', 'polkupyörä','substantiivi', 'arkeologinen']

    # arvotaan yksi sana listasta
    valittusana = random.choice(listasanoja)

    # lisätään listalle * jokaisen kirjaimen kohdalle
    lista = ['*'] * len(valittusana)   

    # printataan valitun sanan pituus
    print(f"Sanassa on {len(valittusana)} kirjainta")

    while True:

        arvaa = input("Arvaa kirjain: ")
        # päivitetään arvattu kirjain listaan
        for index, kirjain in enumerate(valittusana):           
                if arvaa == kirjain:
                    lista[index] = arvaa # korvataan * kirjaimella

        print("".join(lista)) # printataan lista ilman välimerkkejä

        if '*' not in lista: # tsekataan kun lista ei sisällä enää * merkkejä
            print("Onnittelut! Olet arvannut oikein!")
        
        valitse = input("Haluatko arvata sanan? k/e: ")
        # jos valitsee k arvataan sana
        if valitse =="k":
            sananarvaus = input("Arvaa sana: ")
            # jos sana on oikein onnitellaan
            if sananarvaus == valittusana:
                print(f"Onnittelut! Vastaus {sananarvaus} on oikein")
                break
            else: # jos väärin palataan arvaamaan kirjainta
                print(f"Valitettavasti vastaus {sananarvaus} on väärä")

hirsipuu()
