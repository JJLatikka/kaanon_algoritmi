"""
intervalli :
    Tämän moduulin [ Intervalli ] luokassa määritellään kahden samanaikaisesti
    soivan sävelen muodostamaa sävelparia, eli intervallia kuvaava olio.
    Intervallin on tärkeää tietää alkuhetkensä, jotta voidaan keskittää
    tarkastelu erityisesti vahvalla tahtiosalla soiviin intervalleihin.
    Intervallin on myös tiedettävä kokonsa, jotta tiedetään onko kyseessä
    konsonanssi vai dissonanssi. Intervallin koko on sen sävelparin sävelten
    kokojen erotuksen itseisarvo.
kaanon:
    Tämän moduulin [ Kaanon ] luokassa määritellään kahden
    samanaikaisesti soivan melodian muodostamaa
    melodia-vastamelodia-paria, eli kaanonia kuvaava olio. Kaanonin on
    tärkeää tietää, mitkä sen melodioiden sävelistä osuvat yhtäaikaisesti
    iskulle. Tästä syystä luodaan [ self.dict_yksikko ] oliomuuttuja, jonka
    tyyppi on sanakirja. Tämän sanakirjan avaimina ovat tahtilajin mukaisen
    [ Fraction ] tyyppisen yksikön esim. '1/4' kerrannaiset, ja arvoina taasen
    tuolle tietylle iskulle osuvat kaksi eri säveltä. Näistä arvoina olevista
    sävelpareista sitten muodostetaan kaanonin intervallit. Kaanon myös
    tietää, onko se kaanon, sen jälkeen kun [ self.is_kaanon ]
    oliomuuttujaan asetetaan totuusarvo, joka määritellään käymällä läpi
    kaanonin vahvalle tahtiosalle osuvia intervalleja, joiden kaikkien
    tulee siis olla konsonansseja!
melodia:
    Tämän moduulin [ Melodia ] luokka aloittaa ohjelman syötteeksi luetun
    tiettyä melodiaa kuvaavan merkkijonon käsittelyn. Merkkijono
    pilkotaan osiin ensin tahtiviivojen '|' ja myöhemmin välilyöntien
    kohdalta, ja näin syntyneitä osamerkkijonoja analysoidaan vielä lisää
    säännöllisten lausekkeiden avulla, jotta saadaan luotua [ self.savelet ]
    oliomuuttujan arvoksi asetettava lista [ Savel ] olioita. Melodiaa
    kuvaavan merkkijonon analysoinnin perusteella asetetaan myös
    muutamia melodian ominaisuuksia kuvaavia globaalin tason muuttujia.
    Funktio [ pitkat_savelet ] pilkkoo melodian yksikköä pidemmät sävelet
    lyhyemmiksi. Tämä on tärkeää siksi, että joka iskulle voidaan määritellä
    intervalli, ja toisaalta siksi, että lopullinen .pdf-tuloste sisältäisi vain
    halutun kaltaista nuottikuvaa. Nämä pidempien nuottien lyhyemmät
    osat myös sidotaan toisiinsa Lilypond-syntaksin mukaisella kaarella '~',
    jotta melodian alkuperäinen hahmo ei kuitenkaan muutu. Tästä syystä
    sävelille voidaan asettaa totuusarvo [ self.sidottu ], joka oletusarvoisesti
    on [ False ].
savel:
    Tämän moduulin [ Savel ] luokka määrittelee yhtä säveltä kuvaavan
    olion. Pyrin tekemään tästä mahdollisimman kevyen, koska näitä olioita
    ohjelmassa luodaan kaikkein eniten. Sävel tietää nuottinimensä,
    lukuarvonsa, kestonsa, sen onko se sidottu toiseen nuottiin vai ei, sekä
    alkuhetkensä. Alkuhetki tosin asetetaan vasta siinä vaiheessa, kun
    kahta eri vaiheista melodiaa aletaan tarkastella yhdessä. Sävelen
    lukuarvo saadaan hakemalla [ globals ] moduulin [ Globals ] luokan
    sanakirja-tyyppisestä luokkamuuttujasta [ dict_nuotit ] sävelen
    nuottinimeä vastaava lukuarvo.
"""
