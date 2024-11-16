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
    time.sleep(2)
    print(f"{name}, tehtäväsi on päihittää kylääsi uhkaava hirviö.")
    time.sleep(2)
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
def battle(player, monster):
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
    battle(player, monster)  # Aloita taistelu

# Suoritetaan pääohjelma
if __name__ == "__main__":
    main()