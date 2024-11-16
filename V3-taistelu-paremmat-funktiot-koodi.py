import time

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
    print(f"Saavut linnakkeeseen. Näet ympärilläsi vain tyhjyyttä ja kylmyyttä. Linnake on hiljainen ja kolkko.")
    time.sleep(1)
    print(f"Kuulet hirviön karjunnan. Se on lähellä.")
    time.sleep(1)
    print("Hirviö: 'Tunnen sinut, ihminen. Olet tullut lopettamaan minut. Mutta minä en aio antaa sinun tehdä sitä. Mikä on nimesi, jonka voin kirjoittaa hautakiveesi?'")
    time.sleep(1)
    print(f"{name}: 'Minun nimeni on {name}. Olen tullut vapauttamaan meidät vallastasi, hirviö.'")
    time.sleep(1)
    print(f"Hirviö: 'Sinä olet rohkea, {name}. Mutta rohkeus ei riitä. Näytä minulle, mitä sinulla on mielessäsi.'")
    time.sleep(1)
    print("Hirviö hyökkää!")

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

# Pääohjelman suoritus
def main():
    name = intro()  # Pelaajan nimi
    player, weapon = weapon_choice(name)  # Pelaajan hahmo ja ase
    monster = Character("Hirviö", health=20, damage=2)  # Hirviön luonti
    linnakkeen_tarinankerronta(name)  # Linnakkeen tarinankerronta
    battle(player, monster, weapon)  # Aloita taistelu (lisätty weapon)

# Suoritetaan pääohjelma
if __name__ == "__main__":
    main()