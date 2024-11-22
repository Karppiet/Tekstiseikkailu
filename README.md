# Tekstiseikkailu 

## Miten käynnistän tekstiseikkailun?

Tekstiseikkailu käynnistyy ajamalla tiedosto **yhdistetty.py** sen komentorivillä.

## Mistä tekstiseikkailussa on kysymys 

Tekstiseikkailussamme on tarkoitus voittaa hirviö. Matkalla on reittivaihtoehtoja, joiden läpäiseminen auttaa pelin läpäisyssä.

* [Flowchart ensisuunnitelma](flow-ekaversio.png)
* [Draw.iolla tehty ajantasainen Flowchart](tekstiseikkailu-flowchart.png)

## Pelin suunnittelu

Lähdimme liikkeelle siitä, että halusimme peliin jonkin verran pelaaja interaktiota. Tämä toteutettaisiin sillä, että pelaaja antaa oman nimensä, ja pystyy valitsemaan aseen, jolla lähteä tappelemaan maailmaa kiusaavaa hirviötä vastaan.

Pelaajalle ei kerrota suurempaa taustatarinaa, mutta tehdään selväksi että hirviö on maailmalle paha.

Halusimme pelin sisään pienpelejä, joita läpäisemällä pelaaja saa jotain hyötyä matkaansa. Suunnittelimme alunperin, että hyöty voisi olla jokin pelaajan statseja parantava trinket. 

Päädyimme peleistä saatavaan salasanaan, jolla hirviön linnakkeen portti aukeaa. 

## Pelin toteutus

Mietimme, miten peli olisi paras toteuttaa. Jaoimme pelin osia kahden kesken, jotta molemmille tulisi suurinpiirtein yhtä paljon koodia kehitettäväksi. Lopulta koodia olikin jo yli 300 riviä.

Olimme kahden vaiheilla, toteuttaako peli erillisillä tiedostoilla, vai funktioilla. Flowchartin suunnittelu näytti, että pelistä tulisi melko laaja, joten jonkinlainen koodin hallinta olisi tärkeää. Myös mahdollista jatkokehitystä varten funktioilla rakennettu koodi kuulosti helpommalta alkuun, kun tiesimme että peli ei venyisi ihan mahdottomuuksiin.

