"""
luku_ja_kirjoitus :
    Tämän moduulin [ LukuJaKirjoitus ] luokassa määritellään eri polut
    prosessoitavan nuottitiedoston, tallennettavan .ly-tiedoston ja
    virhelokitiedoston sijainteihin. [ LukuJaKirjoitus ] luokan funktio [ lue_in ] lukee
    prosessoitavan nuottitiedoston sisällön ja palauttaa sen merkkijonona, jos
    mitään virhettä ei tapahdu. Funktio [ kirjoita_out ] tallentaa [ output/ly ]
    hakemistoon sekä uuden .ly-tiedoston  että uuden .ly-tiedoston nimen
    väliaikaistiedostoon [ kaanon_temp.txt ]. Molemmat funktiot sekä [ kirjoita_out ]
    että [ lue_in ] hyödyntävät [ LukuJaKirjoitus ] luokan apufunktiota [ get_polku ] ja
    [ kirjoita ].
muotoilu:
    Tämän moduulin [ Muotoilu ] luokan funktio [ savelet_str ] on sellaisien
    luokkien apufunktio, joiden [ __str__ ] funktion tulostessa on [ Savel ]
    tyyppisiä oliota. [ Muotoilu ] luokan funktio [ matriisi_str ] taas on
    apufunktio [ Matriisi ] luokan [ __str__ ] funktiolle. [ Muotoilu ] luokan
    funktio [ get_output ] on vastuussa siitä, että [ Etsija ] tyyppisen olion
    löytämät kaanonit muunnetaan Lilypond-syntaksin mukaisiksi
    merkkijonoiksi. [ Muotoilu ] luokan funktio [ get_stemmat ] on
    apufunktio [ get_output ] funktiolle ja sisältää ikään kuin muotin
    yhdelle Lilypond-syntaksin mukaiselle pianostemmalle, jossa luetaan
    yhtä aikaa kahta nuottiviivastoa. Alemmalla viivastolla on aina annettu
    melodia ja ylemmällä sille mahdollisesti löytynyt vastamelodia. Lisäksi
    on vielä [ get_err_msg ] funktio, jota käytetään virhelokin tulosteen
    muotoiluun, joka sisältää myös aikaleiman. Funktion [ get_output ]
    sisäfunktio [ get_treble ] laskee keskiarvon siitä, kuinka moni erilaisista
    soivista nuoteista on yksiviivaisia tai sitä korkeampia. Jos enemmän
    kuin puolet viivaston nuoteista on yksiviivaisia tai sitä korkeampia, niin
    viivaston nuottiavaimeksi valitaan 'g-avain' (Lilypondissa 'treble')
    muutoin 'f-avain' (Lilypondissa 'bass'). Tämä valinta tapahtuu
    varsinaisesti [ get_treble ] funktion palauttaman totuusarvon
    perusteella  [ get_stemmat ] funktion sisäfunktion [ get_clef ] avulla.
"""
