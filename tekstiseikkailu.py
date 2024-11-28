import time
import random

def hirsipuu():
    # lista sanoista
    listasanoja = ['näkinkenkä', 'kalmari', 'purjevene','pääkallo', 'hiekka']

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
            print("Salasana hirviön linnakkeeseen on makkaravoileipä. Muista se!")
        
        valitse = input("Haluatko arvata sanan? k/e: ")
        # jos valitsee k arvataan sana
        if valitse =="k":
            sananarvaus = input("Arvaa sana: ")
            # jos sana on oikein onnitellaan
            if sananarvaus == valittusana:
                print(f"Onnittelut! Vastaus {sananarvaus} on oikein")
                print("Salasana hirviön linnakkeeseen on makkaravoileipä. Muista se!")
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
            
        pelaa = input(f"Valitse pelaatko vai jänistätkö: p/j ? (kierros {laskuri}) ")

        if pelaa == "p":  
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
                print("BÄNG!")
                valinta()
                break
            # Muuten pelaaja voitti tämän kierroksen
            else:  
                onnittelu = "Onneksi olkoon, voitit kierroksen"
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
                    salasana = "makkaravoileipä"
                    print(f"Selvisit ruletista! Salasana hirviön linnaan on {salasana}. Lisäksi voitit {voitot} kolikkoa!")
                    return salasana, voitot
    
                else: 
                    palkinto = summa * 2

            voitot += palkinto  # lisää voitot kokonaisvoittoihin
            print(f"{onnittelu} {palkinto}")
            print(f"Kokonaisvoitot: {voitot}")

            # kierrosten lisääminen        
            laskuri += 1
        
        # Jos valitaan j poistutaan pelistä 
        elif pelaa == "j": 
            print("Et tainnut uskaltaa...")
            valinta()
            break

def valinta():
    print("Edessäsi on tienhaara. Oikealla siintää tumman vihreä metsä, polun kaartuessa pois näkyviltä.")
    time.sleep(2)
    print("Vasemmalla kohisee meri, ja näet rannikon hiekkaa.")
    time.sleep(2)
    
    while True:
        valinta = input("Lähdetkö metsään, vai siirrytkö rannikolle? Vastaa joko metsä tai rannikko: ")

        # jos valinta m eli metsä pelataan rulettia
        if valinta == "metsä":
            print("Päätät suunnata metsään.")
            time.sleep(2)
            print("Kuljet tiheässä metsässä taistellen eteenpäin aluskasvillisuuden läpi.")
            time.sleep(2)
            print("Näet edessäsi jotain, joka kiinnittää huomiosi.")
            time.sleep(2)
            print("Pöytä, jossa on revolveri ja kuusi luotia.")
            time.sleep(2)
            print("Puun takaa kuulet äänen, joka sanoo: 'Uskallatko haastaa pelkosi?'")
            time.sleep(2)
            print("'Jos voitat, annan sinulle salasanan hirviön linnakkeeseen.'")
            time.sleep(2)
            print("Eteesi astuu punasilmäinen viikatemies.")
            # tulos = 
            ruletti()
            break
            
    #  jos tulee voitto saadaan salasana sekä voitot
    #         if tulos:
    #             print(f"Voitit pelin: {tulos}") 
    #             break
    #         else:
    #             print("Hävisit pelin")
    #             break
                
     
            #jos valinta r eli rannikko mennään rannikolle ja hirsipuu peli alkaa    
        elif valinta == "rannikko":
            print("Käännyt vasemmalle ja suuntaat rannikolle.")
            time.sleep(2)
            print("Kävelet pitkin hiekkarantaa rauhalliseen tahtiin. Melkein unohdat hirviön ja huolesi, kuunnellessasi vain meren kohinaa ja lokkien huutoja.")
            time.sleep(2)
            print("Heräät ajatuksistasi, kun huomaat edessä siintävän hirsipuun.")
            time.sleep(2)
            print("Kävelet rakennelman luokse. Se on vanha ja lahonnut.")
            time.sleep(2)
            print("'Tervetuloa hirsipuuhun', kuulet äänen sanovan.")
            time.sleep(2)
            print("'Tässä pelissä sinun tulee arvata sana. Jos arvaat oikein, annan sinulle salasanan hirviön linnakkeeseen.'")
            time.sleep(2)
            print("'Jos arvaat väärin', ääni hihittää saaden mielipuolisen vivahteen ääneensä, 'hirtän sinut.'")
            hirsipuu()
            break
        else:
            print("Valitse joko rannikko tai metsä")

# Hahmoluokka
class Character: 
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

# Funktio: pelin intro
def intro():
    print("Olet tämän seikkailun päähenkilö.")
    time.sleep(2)
    name = input("Kerro minulle nimesi: ")
    time.sleep(2)
    print(f"Tervehdys {name}. Olillesi lankeaa raskas paino.")
    time.sleep(2)
    print(f"{name}, tehtäväsi on päihittää kylääsi uhkaava hirviö.")
    time.sleep(2)
    print("Hirviö on sulkenut itsensä vuoren päälliseen linnakkeeseen, josta sen vaikutusvalta ja myrkyllinen aura vaikuttaa maailmaan ympärilläsi.")
    time.sleep(2)
    print(f"{name}. Tehtäväsi tulee olemaan yksinäinen ja vaikea.")
    time.sleep(2)
    print(f"Matkastasi tulee pitkä. Kantamustesi lisäksi voit ottaa vain yhden aseen.")
    time.sleep(2)
    print(f"Olet molemmilla yhtä taitava, mutta ne antavat sinulle eri lähestymistavan matkaasi. Jousi ja nuolikotelo, vai miekka ja kilpi?")
    time.sleep(2)
    return name

# Funktio: aseen valinta
def weapon_choice(name):
    weapon = ""
    while weapon not in ["jousi", "miekka"]:
        weapon = input("Valitse aseesi kirjoittamalla 'jousi' tai 'miekka': ")

    if weapon == "jousi":
        player = Character(name, health=6, damage=6)
        print("Valitsit jousen. Se antaa sinulle vahvan etäedun!")
    elif weapon == "miekka":
        player = Character(name, health=10, damage=4)
        print("Valitsit miekan. Se antaa sinulle kestävyyttä lähitaisteluun!")
    time.sleep(2)
    return player, weapon

def linnakkeen_salasanatarinankerronta(name):
    print("Koettelemuksesi ovat tuoneet sinut ylös vuoren rinnettä, jossa hirviön linnake sijaitsee.")
    time.sleep(2)
    print("Väsymys koettelee raajojasi, mutta et anna sen hidastaa sinua.")
    time.sleep(2)
    print("Saavut linnakkeen portille. Se on lukittu ja vaatii salasanan.")
    time.sleep(2)

def linnake_salasana():
    salasana = ""
    yritys = 0
    
    while salasana != "makkaravoileipä":
        salasana = input("Anna löytämäsi salasana: ")
        yritys += 1
        if yritys >= 3:
            print("Olet ylittänyt yritysten määrän. Portti ei aukea.")
            time.sleep(2)
            print("Päätät palata takaisin.")
            time.sleep(2)
            yritys = 0
            valinta()
    else:
        print("Salasana on oikein. Portti aukeaa.")

def linnakkeen_tarinankerronta(name):
    print(f"Astut portista linnakkeeseen. Näet ympärilläsi vain tyhjyyttä ja kylmyyttä. Linnakkeen piha-alue on hiljainen ja kolkko.")
    time.sleep(2)
    print(f"Kuulet hirviön karjunnan. Se tuijottaa sinua ikkunasta, ennenkuin hyppää eteesi piha-alueella, valtavaa taistelukirvestä heilutellen.")
    time.sleep(2)
    print("Hirviö: 'Tunnen sinut, ihminen. Olet tullut lopettamaan minut. Mutta minä en aio antaa sinun tehdä sitä. Mikä on nimesi, jonka voin kirjoittaa hautakiveesi?'")
    time.sleep(2)
    print(f"{name}: 'Minun nimeni on {name}. Olen tullut vapauttamaan meidät vallastasi, hirviö.'")
    time.sleep(2)
    print(f"Hirviö: 'Sinä olet rohkea, {name}. Mutta rohkeus ei riitä. Näytä minulle, mitä sinulla on mielessäsi.'")
    time.sleep(2)
    print("Hirviö hyökkää!")

# Funktio: pelin pääsilmukka
def battle(player, monster, weapon, monster_distance):
    while monster.health > 0 and player.health > 0:
        monster_distance = combat_round(player, monster, weapon, monster_distance)
    
    # Tarkista voittaja
    if player.health <= 0:
        print(f"\n{player.name} on kaatunut taistelussa. Hirviö voitti.")
        sana = "YRITÄ UUDELLEEN"
        print(30* "*")
        print("*"+ sana.center(28, " ")+"*")
        print(30* "*")
    else:
        print(f"\nHirviö on kaadettu! {player.name} on sankari!")
        sana = "LOPPU"
        print(30* "*")
        print("*"+ sana.center(28, " ")+"*")
        print(30* "*")
        
# Funktio: yhden taistelukierroksen suorittaminen
def combat_round(player, monster, weapon, monster_distance):
    print(f"\nHirviön etäisyys: {monster_distance} | Hirviön HP: {monster.health}")
    print(f"{player.name} HP: {player.health}")
    time.sleep(2)
    
    input("Paina enteriä jatkaaksesi seuraavaa vuoroa...")
    
    if weapon == "jousi":
        print("Ammut nuolen!")
        time.sleep(2)
        monster.health -= player.damage
        monster_distance -= 2
        if monster_distance <= 5:
            print("Hirviö hyökkää!")
            time.sleep(2)
            player.health -= monster.damage
    elif weapon == "miekka":
        if monster_distance > 5:
            print("Olet liian kaukana! Lähestyt hirviötä.")
            time.sleep(2)
            monster_distance -= 2
        else:
            print("Hyökkäät miekkasi kanssa!")
            time.sleep(2)
            monster.health -= player.damage
            print("Hirviö hyökkää!")
            time.sleep(2)
            player.health -= monster.damage

    return monster_distance

# Pääohjelman rakentaminen funktioista
def main():
    name = intro()  # Pelaajan nimi
    player, weapon = weapon_choice(name)  # Pelaajan hahmo ja ase
    monster = Character("Hirviö", health=20, damage=2)  # Hirviön luonti
    monster_distance = random.randint(5, 15)  # Hirviön etäisyys
    valinta() # metsä vai rannikko
    linnakkeen_salasanatarinankerronta(name)  # Linnakkeen salasanan tarinankerronta
    linnake_salasana()  # Linnakkeen salasana
    linnakkeen_tarinankerronta(name)  # Linnakkeen tarinankerronta
    battle(player, monster, weapon, monster_distance)  # Aloita taistelu

# Suoritetaan pääohjelma
if __name__ == "__main__":
    main()



