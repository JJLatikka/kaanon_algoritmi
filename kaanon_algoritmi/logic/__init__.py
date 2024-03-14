"""
etsija:
    Tämän moduulin [ Etsija ] luokka on se, joka suorittaa varsinaisen eri
    kaanonvaihtoehtojen etsimisen. Tämän luokan konstruktori saa
    parametrinaan käyttäjän tallentamasta tekstimuotoisesta
    nuottitiedostosta luetun tiettyä melodiaa kuvaavan merkkijonon.
    Tuosta merkkijonsta luodaan [ Melodia ] tyyppinen [ self.melodia ]
    oliomuuttujan  arvoksi asetettava olio. Oliomuuttujan [ self.melodia.savelet ]
    sisältämä sävellista taas annetaan [ Matriisi ] tyyppisen
    oliomuuttujan [ self.matriisi ] konstruktorin parametrina. Tämä
    oliomuuttuja muodostaa ne eri vastamelodia vaihtoehdot, joita eri
    vaiheisina yritetään sovittaa yhteen alkuperäisen melodian
    perusmuodon kanssa. Oliomuuttujan [ self.vaihe ] arvo on aluksi 1, ja
    varsinainen melodioiden vaihe-ero saadaan kertomalla tämä
    oliomuuttujan [ self.vaihe ] arvo yksikön arvolla, joka esim. '1/4'
    tahtilajissa on [ Fraction ] tyyppinen murtoluku '1/4'. Suurin
    mahdollinen vaihe-ero asetetaan funktiolla [ set_vaihe_max ], joka
    tässä versiossa on noin puolet alkuperäisen melodian tahtimäärästä.
    Onhan selvää, että jos melodioiden vaihe-ero on lähes koko
    alkuperäisen melodian pituinen, ei ole enää mielekästä yrittää
    tarkastella melodiaa ja sen vastamelodiaa kaanonina, koska kaanonissa
    melodiat soivat yhtäaikaisesti, eli ainakin osittain 'päällekkäin', eivätkä
    perättäisesti. Funktio [ etsi ] kloonaa ja vaiheistaa aina uuden vaiheen
    alkaessa ensin alkuperäisen melodian sävellistan uudeksi omaksi
    listakseen, ja sitten vaiheistaa vuorollaan jokaisen matriisin
    melodiavaihtoehdon, ja luo kaanonehdoḱkaan kustakin
    samanvaiheisesta alkuperäisestä melodiasta ja vastamelodia-
    vaihtoehdosta. Löydetyt kaanonit tallennetaan [ self.loydetyt ]
    oliomuuttujaan siten, että syntyy lista [ Tuple ] tyyppisiä
    tietorakenteita. Jokainen tällainen [ Tuple ] koostuu kahdesta
    sävellistasta, melodiasta ja vastamelodiasta, joista molemmat ovat
    samanvaiheisia. Luokan [ Etsija ] funktio [ vaiheista ] toimii käytännössä
    siten, että se lisää vastamelodian alkuun ja melodian loppuun saman
    määrän yksikön pituisia taukoja. Funktiota [ set_savelten_alkuhetket ]
    kutsutaan [ vaiheista ] funktion palautusarvona olevalle listalle. Tämä
    on tarpeellista siksi, että tiedetään mitkä tarkasteltavien melodioiden
    sävelet milloinkin soivat samaan aikaan, ja että niistä tällöin voidaan
    muodostaa [ Kaanon ] tyyppisen olion tarvitsemat intervallit.
matriisi:
    Tämän moduulin [ Matriisi ] luokka hyödyntää [ globals ] moduulin
    luokan [ Globals ] luokkamuuttujana olevaa merkkijonolistaa [ nuotit ].
    Tästä listasta luodaan avain-arvo-parit [ Matriisi ] tyyppisen olion
    sanakirja-tyyppiseen [ self.dict_tr ] oliomuuttujaan siten, että avaimeksi
    tulee nuottinimi ja arvoksi nuottinimen listaindeksi. Tätä sanakirjaa
    tarvitaan transponoitaessa melodian nuotteja eri korkeuksille, ja
    toisaalta käännettäessä melodian intervalleja 'peilikuvikseen'. Funktiota
    [ kloonaa ] tarvitaan sekä [ Matriisi ] luokassa että myöskin [ etsija ]
    moduulin [ Etsija ] luokan [ etsi ] funktiossa. [ Matriisi ] luokalla on
    oliomuuttujinaan neljä erilaista versiota alkuperäisestä melodiasta.
    Näitä ovat [ self.perus ] melodian perusmuoto ja [ self.krapu ] melodian
    krapuliike versio, jossa sävelet ovat käänteisessä järjestyksessä, ensin
    viimeinen ja viimeisenä ensimmäinen. Sitten ovat vielä [ self.inver ]
    melodian inversio, jossa melodian sävelten väliset intervallit ovat
    käännettyinä peilikuvikseen, ylös suuntatuva liike alas suuntautuvaksi ja
    alas suuntautuva ylös suuntautuvaksi, sekä [ self.krapuinver ] inversion
    krapuliike versio, eli inversion sävelet käänteisessä järjestyksessä. Aina
    melodian sävelten käänteistä järjestystä asetettaessa tehdään tarkistus
    [ kaanteinen_jarjestys ] funktiossa, onko melodiassa toisiinsa sidottuja
    kaarellisia nuotteja, ja jos on, niin kaaren suuntaa vaihdetaan, koska jos
    on 'a~ b', niin ilman kaaren suunnan vaihtoa käänteisessä järjestyksessä
    on 'b a~', vaikka pitäisi olla 'b~ a'. Jos kaarellisia nuotteja havaitaan, niin
    [ kaanteinen_jarjestys ] funktion sisäfunktio [ vaihda_kaarien_suunnat ]
    suoritetaan. Funktiolla [ set_inversio ] käännetään melodian intervallien
    suunnat ensimmäisen soivan nuotin suhteen. Tämä funktio kutsuu ensin
    funktiota [ get_tuplet_tr ], joka palauttaa listan [ Tuple ] tyyppisiä
    tietorakenteita. Jokainen [ Tuple ] koostuu indeksistä, joka haetaan
    sävelen nimen perusteella [ self.dict_tr ] oliomuuttujasta, ja [ Savel ]
    oliosta itsestään. Melodian intervallin suuntaa vaihdettaessa katsotaan
    mikä on säveleen liittyvän indeksin ja ensimmäiseen soivaan säveleen
    liittyvän ns. symmetriaindeksin erotus ja lisätään tämä erotus tuohon
    symmetria indeksiin, jotta saadaan uusi indeksi, jolla [ self.dict_tr ]
    sanakirjasta voidaan hakea uusi transponoitu sävelnimi [ Savel ] oliolle.
    Uusi sävelnimi asetetaan funktiolla [ get_savel_tr ]. Asetettaessa
    oliomuuttujan [ self.matriisi ] arvoa, kootaan yhdeksi ja samaksi listaksi
    kaikki neljä alkuperäisen melodian eri versiota transponointeineen,
    siten, että muodostetaan ensin seitsemän eri korkeudelle sijoittuvaa
    transponoitua versiota kustakin melodian versiosta, minkä jälkeen
    yhdistetään kaikki yhdeksi ja samaksi listaksi [ numpy.concatenate ]
    funktiota hyödyntämällä. Ennen [ numpy.concatenate ] funktion
    käyttöä on hetkellisesti tilanne, jolloin on olemassa komiulotteinen
    lista, jolla on neljä listaa, joista jokainen sisältää seitsemän [ Savel ]
    tyyppisiä olioita sisältävää listaa.
"""
