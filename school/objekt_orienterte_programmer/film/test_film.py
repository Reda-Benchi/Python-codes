from film import Film # importerer klassen film fra filen film.py

def test_film():
    # __init__
    # Oppretter to film-objekter med tittel og produksjonsår
    batman = Film("The dark knight", 2008)
    superman = Film("Man of steel", 2013)
    print("Oppretter to filmer")
    print()
    
    # hent_tittel
    # Skriv ut tittel på de to filmene
    print("Skriver ut titler på to filmer")
    print(batman.hent_tittel(),"og", superman.hent_tittel())
    print()

    # ny_skuespiller
    # Legg til to skuespillere og deres roller for en av filmene, skriv ut alt om filmen
    print("Legger til to skuespillere")
    batman.ny_skuespiller("Christian Bale", "Batman")
    batman.ny_skuespiller("Heath Ledger", "Joker")
    superman.ny_skuespiller("Henry Cavhill", "Superman")
    print()

    # Prøv å legge inn en av skuespillerne igjen, med en ny rolle, og sjekk at rollen ikke blir endret
    print("Tester ulovlig innlegging av skuespiller")
    batman.ny_skuespiller("Christian Bale", "Batwoman")
    superman.ny_skuespiller("Henry Cavhill", "Superwoman")
    print()

    # skriv_ut_film
    # Skriv ut all informasjon om begge filmer du har lagt inn
    print("Skriver ut all info om to filmer:")
    batman.skriv_ut_film()
    superman.skriv_ut_film()
    print()

    # hent_alle_skuespiller_navn
    # Skriv ut skuespillernes navn for den filmen som har to
    print("Henter og skriver ut alle skuespillernavn for en film:")
    print(batman.hent_alle_skuespiller_navn())
    print()

    # sjekk_periode
    # Sjekk om en film du har lagt inn er i en periode du velger
    # (velg periode som skal gi True og sjekk at dette blir resultatet)
    print ("Sjekker at en film er i oppgitt periode")
    print(batman.sjekk_periode(2005,2020))
    print()

    # Sjekk om en film er i en periode som skal gi False
    # (velg samme årstall til begge argumenter og sjekk resultat er False)
    print ("Sjekker at en film ikke kan være produsert før og etter samme år")
    print(batman.sjekk_periode(2005,2005))
    print(batman.sjekk_periode(2020,2020))
    print()

    # sjekk_tittel
    # Sjekk om en film har en tittel som starter på en streng som du selv velger
    print ("Sjekker om starten på en films tittel kjennes igjen")
    print(superman.sjekk_tittel("Man of steel"))
    print()
    
    # __str__
    # Skriv ut film-objekt med print
    print("Skriver ut en film med print (test av __str__)")
    print(batman.__str__())
    print()
    
    # test __eq__ (frivillig)
    print ("tester __eq__ med to ulike filmer:")
    print(superman.__eq__(batman))
    print("\nTester __eq__ med to like filmer:")
    print(superman.__eq__(superman))
    print()

test_film()
