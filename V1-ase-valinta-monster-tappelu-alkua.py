print("Olet tämän seikkailun päähenkilö.")
nimi = input("Kerro minulle nimesi: ")

print(f"Tervehdys {nimi}. Olillesi lankeaa raskas paino.")
print(f"{nimi}, tehtäväsi on päihittää kylääsi ja läheisiäsi uhkaava hirviö.")
print("Hirviö on sulkenut itsensä vuoren päälliseen linnakkeeseen, josta sen vaikutusvalta ja myrkyllinen aura vaikuttaa maailmaan ympärilläsi.")
print(f"{nimi}. Tehtäväsi tulee olemaan yksinäinen ja vaikea.")
print(f"Matkastasi tulee pitkä. Kantamustesi lisäksi voit ottaa vain yhden aseen.")
print(f"Olet molemmilla yhtä taitava, mutta ne antavat sinulle eri lähestymistavan matkaasi. Jousi ja nuolikotelo, vai miekka ja kilpi?")
dmg = 2
hp = 6
ase = ""
ase = input("Valitse aseesi kirjoittamalla jousi tai miekka: ")

if ase == "jousi":
	dmg += 4
	
if ase == "miekka":
	dmg += 2
	hp += 2
	
monsterdistance = 10
playerdistance = 10
monsterhp = 20
distance = monsterdistance + playerdistance

while monsterhp >= 0:
	if ase == "jousi":
		monsterhp -= dmg
		monsterdistance -= 2
		if monsterdistance <= 5:
			print(f"Hirviön etäisyys: {monsterdistance}")
			print(f"Hirviön hp: {monsterhp}")
			print("Hirviö hyökkää!")
			hp -= 2
			print(f"Sinun hp: {hp}")
			if hp <= 0:
				print("Olet kuollut.")
				break

	if ase == "miekka":
		monsterhp -= dmg
		if monsterhp <= 0:
			print("Hirviö on kuollut.")
			break
		elif distance > 5:
			print("Olet liian kaukana.")
			playerdistance -= 2
			monsterdistance -= 2
			print("Hirviö siirtyy lähemmäs!")
		else:
			print(f"Hirviön etäisyys: {monsterdistance}")
			print(f"Hirviön hp: {monsterhp}")
			print("Hirviö hyökkää!")
			hp -= 2
			print(f"Sinun hp: {hp}")
			if hp == 0:
				print("Olet kuollut.")
				break
print("Hirviö on kuollut.")