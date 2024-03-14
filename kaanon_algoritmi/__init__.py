"""
Kaanon_algoritmi.sh :
    Aluksi tässä skriptissä lisätään [ PYTHONPATH ] ympäristömuuttujaan
    tarvittavat itse määritellyt Python-paketit, jotta skriptiin voidaan viitata
    esimerkiksi pikakuvaketta painettaessa. Sitten tallennetaan käytössä
    olevan Lilypond-version tuloste [ version_ly ] muuttujan arvoksi. Tämän
    jälkeen aloitetaan algoritmin suoritus, ja suorituskäskyn
    komentoriviparametrina annetaan [ version_ly ] muuttujan arvo.
    Ohjelman suorituksen jälkeen tallennetaan [ status ] muuttujan arvoksi
    prosessin suorituksen palauttama lukuarvo. Mikäli tuo lukuarvo on 0, eli
    ohjelma suoritettiin läpi onnistuneesti, tulostetaan algoritmin
    tallentamasta [ kaanon_temp.txt ] väliaikaistiedostosta uuden
    kaanontiedoston nimi, ja tallennetaan se [ kaanon ] muuttujan arvoksi.
    Sitten voidaan ensin kutsua Lilypond:ia, joka muuntaa ohjelman
    tallentaman uuden .ly-tiedoston sisällön .pdf-muotoon, sekä tämän
    jälkeen Atril:ia, jolla uusi .pdf-tiedosto voidaan näyttää käyttäjälle.
    Lopuksi poistetaan [ kaanon_temp.txt ] väliaikaistiedosto. - Tämä skripti
    sijaitsee [ kaanon_algoritmi ] paketin yläkansiossa, koska sieltä voidaan
    ohjelman suoritusta kutsua [ python3 -m kaanon_algoritmi ]
    komennolla, jossa [ -m ] viittaa [ __main__ ] moduuliin, joka
    oletettavasti löytyy [ kaanon_algoritmi ] paketista.
__main__ :
    Tässä moduulissa on [ Main ] pääluokka, joka käynnistää sovelluksen.
    Luokalla on vain yksi oliomuuttuja, joka on kaanoneita etsivä [ Etsija ]
    olio. Tuo olio saa konstruktorinsa parametrina melodian nuotteja
    kuvaavan merkkijonon. Merkkijonon lukemiseen käytetään [ in_out ]
    paketin [ luku_ja_kirjoitus ] moduulin [ LukuJaKirjoitus] luokan [ lue_in ]
    funktiota. Oliomuuttujan [ self.etsija ] arvo on aluksi [ None ], koska ei
    ole varmaa, pystytäänkö tiedostoa lukea ensinkään! - Jos tiedosto
    pystytään lukemaan, ja melodian nuotteja kuvaava merkkijono on
    olemassa, voidaan [ Etsija ] olio luoda. Tällöin [ Etsija ] olion [ etsi ]
    funktiota voidaan kutsua, ja mahdolliset löydetyt kaanonit voidaan
    antaa [ in_out ] paketin [ muotoilu ] moduulin [ Muotoilu ] luokan
    funktion [ get_output ] käsiteltäväksi. Tuo funktio muuntaa löydetyt
    kaanonit Lilypond:in syntaksin mukaiseksi merkkijonoksi, jonka paketin
    [ in_out ] moduulin [ luku_ja_kirjoitus] luokan [ LukuJaKirjoitus ] funktio
    [ kirjoita_out ] tallentaa .ly-tiedostoksi, joka voidaan muuntaa
    Lilypond:ia hyödyntämällä .pdf-formaatissa olevaksi nuottikuvaksi.
    Koska ohjelman suoritus käynnistetään skriptillä, saa se aina
    komentoriviparametrina käytössä olevan Lilypond-version numeron.
    Tämä versionumero on hyvä olla liitettynä lopulliseen .ly-tiedostoon,
    koska muuten Lilypond huomautaa versionumeron puuttumisesta,
    vaikka yleensä toimiikin silti normaalisti. - Mikäli ohjelman
    suorituksessa taphtuu virhe, käyttäjälle näytetään virheestä kertova viesti,
    tallennettaan virheilmoitus [ in_out ] paketin [ luku_ja_kirjoitus ] moduulin
    [ LukuJaKirjoitus ] luokan [ kirjoita ] funktiolla virheloki-
    tiedostoon ja lopetetaan sovelluksen suoritus pienen tauon jälkeen.
    Pääluokan [ Main ] funktio [ get_nuottitiedoston_nimi ] kutsuu itseään
    niin kauan, että käyttäjä joko sulkee sovelluksen tai syöttää jonkin
    tiedostonimen, joka tallennetaan [ kaanon_algoritmi ] paketin [ globals ]
    moduulin [ Globals ] luokan [ nuottitiedoston_nimi ] luokkamuuttujan
    arvoksi.
globals :
    Tämän moduulin [ Globals ] luokka sisältää nimensä mukaisesti
    sovelluksen globaalin tason muuttujia, joihin voidaan viitata eri puolilta
    ohjelman lähdekoodia tarpeen mukaan. Muutujaan [ version_ly ]
    tallennetaan käytössä olevan Lilypond-version versionumero.
    Muuttujaan [ nuottitiedoston_nimi ] tallennetaan käyttäjän syöttämä
    prosessoitavan nuottitiedoston nimi. Sanakirja [ dict_nuotit ] sisältää
    avaimina diatonisen asteikon sävelet (sama kuin pianon valkoiset
    koskettimet) sekä taukonuotin, joka Lilypond-syntaksin mukaan on 'r',
    eli 'rest'. Näitä avaimina olevia arvoja vastaavia lukuarvoja tarvitaan
    kuvaamaan mahdollisia kahden eri sävelen muodostamia intervalleja, ja
    ne etenevät 'c' sävelestä (arvo 1) puolisävelaskelittain aina asteikon
    viimeiseen säveleen 'b' asti (arvo 12). Tauko 'r' saa arvon 0, koska
    sen kanssa ei voi muodostaa intervallia, eikä sen lukuarvolla siksi
    ole merkitystä kahden eri sävelen välistä etäisyyttä mitattaessa.
    Melodian eri transponointien muodostamiseen tarvittava muuttuja [ nuotit ]
    sisältää kuusi oktaavia eri oktaavialoissa sijaitsevia asteikon nuotteja
    alkaen tauosta (r indeksi = 0) ja matalimmasta sävelestä (kontra c = c,,
    indeksi = 1) korkeimpaan säveleen (kolmiviivainen b = b''' indeksi = 42).
    Sävelten merkintätapa noudattaa jälleen Lilypond-syntaksia. Muuttujiin
    [ tahtiosoitus, kaksijakoinen, tahtimaara, soivia_distinct ] tallennetaan
    prosessoitavan melodian ominaisuuksia. Murtoluku, eli [ Fraction ]
    -tyyppinen muuttuja [ yksikko ] kuvaa sitä, lasketaanko melodiassa
    esim. neljäs- vai kahdeksasosia. Muuttujan [ jaollisuus ], jonka tyyppi on
    myös [ Fraction ], tallentama tieto on tärkeä siksi, koska se, onko
    melodia kaksi- vai kolmijakoinen vaikuttaa oleellisesti siihen, mitkä ovat
    ne kriteerit, joiden perusteella voidaan sanoa mikä on kaanon ja mikä
    ei. Esimerkiksi tahtilajissa '4/4' painollisia säveliä ovat ensimmäinen ja
    kolmas sävel, kun taas kolmijakoisessa tahtilajissa kuten vaikkapa '3/4'
    painollinen sävel on vain tahdin ensimmäinen. Kaanonin määritelmän
    mukaan painollisella iskulla olevan intervallin on oltava konsonanssi.
    Siksi onkin vielä muuttuja [ dissonanssit ] jossa luetellaan ne kahden eri
    sävelen väliset etäisyydet, jotka muodostavat dissonanssin, joka on
    konsonanssin vastakohta.
"""
