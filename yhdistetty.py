import time
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


def ruletti():

    print("Tervetuloa pelaamaan venäläistä rulettia!")

    # luodaan satunnainen luku luodille
    luoti = random.randint(1, 6) 
    # luoti = 1

    # alustetaan laskuri
    laskuri = 1 
    # alustetaan voitot
    voitot = 0

    # While loopin sisällä valitaan pelataanko vai ei
    while True:    
        valinta = input(f"Valitse pelaatko vai jänistätkö: p/j ? (kierros {laskuri}) ")

        if valinta == "p":  
            while True:
                
                try:
                    summa = int(input("Valitse panostettava summa väliltä 1-10: "))
                    if summa in range(1,11): break
                   
                # Jos panostettava summa ei ole numeroita annetaan virheilmoitus ja palataan kyselyyn    
                except ValueError:
                    print("Väärä muoto, syötä vain numeroita") 
    
            # arvotaan luku pelaajalla
            arvonta = random.randint(1, 6)
         
            # Jos luoti ja luku täsmäävät pelaaja häviää ja poistutaan loopista
            if luoti == arvonta:
                print("BÄNG!, hävisit pelin")
                break

            # Muuten pelaaja voitti tämän kierroksen
            else:  
                onnittelu = "Onneksi olkoon voitit"
                print("Click")
                palkinto = 0         

                # Katsotaan monennenko kierroksen pelaaja voitti, palkintosumma määräytyy sen mukaan
                if laskuri == 2:   
                    palkinto = summa * 4                                                   
                elif laskuri == 3:
                    palkinto = summa * 6                
                elif laskuri == 4: 
                    palkinto = summa * 10       # jos kierros on 4 eli viimeinen pelaaja voittaa pelin ja poistutaan funktiosta palauttaen salasanan
                    voitot += palkinto
                    print(f"Selvisit ruletista! Kokonaisvoitot {voitot}")
                    return "makkaravoileipä", voitot
                else: 
                    palkinto = summa * 2

            voitot += palkinto  # lisää voitot kokonaisvoittoihin
            print(f"{onnittelu} {palkinto}")
            print(f"Kokonaisvoitot: {voitot}")



            # kierrosten lisääminen        
            laskuri += 1
        
        # Jos valitaan j poistutaan pelistä 
        elif valinta == "j": 
            print("Et tainnut uskaltaa...")
            break

def valinta():

    while True:
        valinta = input("Edessä siintää metsä, menetkö sinne vai siirryt rannikolle? Vastaa joko m tai r ")
        # jos valinta m eli metsä pelataan rulettia
        if valinta == "m":
            print("Menet metsään")
            time.sleep(3)
            print("Näet metsän laidalla heinikon...")
            time.sleep(2)
            print("Heinikossa näkyy jotain, muttet tiedä tarkalleen mitä..")
            print("Mutta aiot ottaa selvää..")
            print("Näet viikatemiehen punaisine silmineen")
            time.sleep(3)
            tulos = ruletti()
            
    # jos tulee voitto saadaan salasana sekä voitot
            if tulos:
                print(f"Voitit pelin, tässä salasanasi sekä voitot: {tulos}") 
                break
            else:
                print("Hävisit pelin")
                break
                
     
            #jos valinta r eli rannikko mennään rannikolle ja hirsipuu peli alkaa    
        elif valinta == "r":
            print("Siirryt rannikolle")
            print("Näet kaukana hirsipuun..")
            time.sleep(2)
            print("Kävelet hirsipuun luokse")
            time.sleep(1)
            hirsipuu()
            break
        else:
            print("Valitse joko r(rannikko) tai m(metsä)")

# Hahmoluokka
class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

# Funktio: pelin intro
def intro():
    print("Olet tämän seikkailun päähenkilö.")
    time.sleep(1)
    name = input("Kerro minulle nimesi: ")
    time.sleep(1)
    print(f"Tervehdys {name}. Olillesi lankeaa raskas paino.")
    time.sleep(1)
    print(f"{name}, tehtäväsi on päihittää kylääsi uhkaava hirviö.")
    time.sleep(1)
    print("Hirviö on sulkenut itsensä vuoren päälliseen linnakkeeseen, josta sen vaikutusvalta ja myrkyllinen aura vaikuttaa maailmaan ympärilläsi.")
    time.sleep(1)
    print(f"{name}. Tehtäväsi tulee olemaan yksinäinen ja vaikea.")
    time.sleep(1)
    print(f"Matkastasi tulee pitkä. Kantamustesi lisäksi voit ottaa vain yhden aseen.")
    time.sleep(1)
    print(f"Olet molemmilla yhtä taitava, mutta ne antavat sinulle eri lähestymistavan matkaasi. Jousi ja nuolikotelo, vai miekka ja kilpi?")
    return name

# Funktio: aseen valinta
def weapon_choice(name):
    weapon = ""
    while weapon not in ["jousi", "miekka"]:
        weapon = input("Valitse aseesi kirjoittamalla 'jousi' tai 'miekka': ").lower()

    if weapon == "jousi":
        player = Character(name, health=6, damage=6)
        print("Valitsit jousen. Se antaa sinulle vahvan etäedun!")
    elif weapon == "miekka":
        player = Character(name, health=8, damage=4)
        print("Valitsit miekan. Se antaa sinulle kestävyyttä lähitaisteluun!")
    time.sleep(2)
    return player, weapon

def linnakkeen_tarinankerronta(name):
    print(f"Astut portista linnakkeeseen. Näet ympärilläsi vain tyhjyyttä ja kylmyyttä. Linnakkeen piha-alue on hiljainen ja kolkko.")
    time.sleep(1)
    print(f"Kuulet hirviön karjunnan. Se tuijottaa sinua ikkunasta, ennenkuin hyppää eteesi piha-alueella, valtavaa taistelukirvestä heilutellen.")
    time.sleep(1)
    print("Hirviö: 'Tunnen sinut, ihminen. Olet tullut lopettamaan minut. Mutta minä en aio antaa sinun tehdä sitä. Mikä on nimesi, jonka voin kirjoittaa hautakiveesi?'")
    time.sleep(1)
    print(f"{name}: 'Minun nimeni on {name}. Olen tullut vapauttamaan meidät vallastasi, hirviö.'")
    time.sleep(1)
    print(f"Hirviö: 'Sinä olet rohkea, {name}. Mutta rohkeus ei riitä. Näytä minulle, mitä sinulla on mielessäsi.'")
    time.sleep(1)
    print("Hirviö hyökkää!")

def linnake_salasana():
    print("Saavut linnakkeen portille. Se on lukittu ja vaatii salasanan.")
    time.sleep(1)
    salasana = input("Anna löytämäsi salanasana: ")

    if salasana == "makkaravoileipä":
        print("Salasana on oikein. Portti aukeaa.")

# Funktio: yhden taistelukierroksen suorittaminen
def combat_round(player, monster, weapon, monster_distance):
    print(f"\nHirviön etäisyys: {monster_distance} | Hirviön HP: {monster.health}")
    print(f"{player.name} HP: {player.health}")
    time.sleep(1)
    
    input("Paina enteriä jatkaaksesi seuraavaa vuoroa...")
    
    if weapon == "jousi":
        print("Ammut nuolen!")
        time.sleep(1)
        monster.health -= player.damage
        monster_distance -= 2
        if monster_distance <= 5:
            print("Hirviö hyökkää!")
            time.sleep(1)
            player.health -= monster.damage
    elif weapon == "miekka":
        if monster_distance > 5:
            print("Olet liian kaukana! Lähestyt hirviötä.")
            time.sleep(1)
            monster_distance -= 2
        else:
            print("Hyökkäät miekkasi kanssa!")
            time.sleep(1)
            monster.health -= player.damage
            print("Hirviö hyökkää!")
            time.sleep(1)
            player.health -= monster.damage

    return monster_distance

# Funktio: pelin pääsilmukka
def battle(player, monster, weapon):
    monster_distance = 10
    while monster.health > 0 and player.health > 0:
        monster_distance = combat_round(player, monster, weapon, monster_distance)
    
    # Tarkista voittaja
    if player.health <= 0:
        print(f"\n{player.name} on kaatunut taistelussa. Hirviö voitti.")
    else:
        print(f"\nHirviö on kaadettu! {player.name} on sankari!")
        sana = "LOPPU"
        print(30* "*")
        print("*"+ sana.center(28, " ")+"*")
        print(30* "*")
        

# Pääohjelman suoritus
def main():
    name = intro()  # Pelaajan nimi
    player, weapon = weapon_choice(name)  # Pelaajan hahmo ja ase
    monster = Character("Hirviö", health=20, damage=2)  # Hirviön luonti
    valinta()
    linnake_salasana():
    linnakkeen_tarinankerronta(name)  # Linnakkeen tarinankerronta
    battle(player, monster, weapon)  # Aloita taistelu (lisätty weapon)

# Suoritetaan pääohjelma
if __name__ == "__main__":
    main()
