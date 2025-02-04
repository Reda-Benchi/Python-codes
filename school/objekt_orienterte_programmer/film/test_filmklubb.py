from film import Film
from filmklubb import Filmklubb

def testprogram():

    # __init__
    # Opprett Filmklubb-objekt
    oslo = Filmklubb()
    print("oppretter Filmklubb-objekt")
    print()

    # les_filmer_fra_fil
    # Les inn filmer fra filen filmer.txt
    print("Leser filmer fra fil")
    oslo.les_filmer_fra_fil("filmer.txt")
    print()

    # skriv_ut_alle_filmer
    # Skriv ut all info om alle filmer, sjekk at alt er lest fra fil
    print("Skriver ut alle filmer")
    oslo.skriv_ut_alle_filmer()
    print()

    # registrer_film
    print("Registrerer ny film")
    # Legg inn en ny film med tittel og produksjonsår som leses fra terminal
    oslo.registrer_film()
    print()
    # Skriv ut all info om alle filmer og sjekk at ny film ble registrert
    oslo.skriv_ut_alle_filmer()
    print()
    
    # Hvis _eq_ er implementert i Film og testes i registrer_film:
    print("Prøv å registrere film som allerede finnes")
    oslo.registrer_film() # som bruker må du fylle ut king kong i første input og 1933 i andre input for å fremprovosere feilmeldingen
    print()    


    # finn_film_tittel
    print("Leter etter film med (start på) usannsynlig tittel")
    # Kall på metoden med et argument som ingen titler starter med
    letting = oslo.finn_film_tittel("The") # MERKNAD: Klarer ikke å skrive ut The matrix fordi The imitation game kommer først. Fant ikke ut hvordan jeg skulle løse det
    # Bruk print eller assert for å sjekke at resultatet er som forventet
    print(letting)
    print()

    print("Leter etter film med (start på) tittel 'Hidden '")
    # Kall på metoden med argument "Hidden "
    hidden = oslo.finn_film_tittel("Hidden")
    # Bruk print eller assert for å sjekke at resultatet er som forventet
    print(hidden)
    print()

    # legg_til_skuespillere
    print("Legg til skuespillere for en film" )
    # kall metoden på film-objektet du fikk returnert fra finn_film_tittel
    # (navn og rolle for to skuespillere du velger selv leses fra terminal)
    oslo.legg_til_skuespiller(hidden)
    print()
    # SKriv ut all info om alle filmer og sjekk at resultatet er som forventet
    oslo.skriv_ut_alle_filmer()
    print()

    # finn_film_periode
    # Kall på metoden med argumentene etter=2000 og før=2024
    print("Leter filmer produsert etter 2000 og før 2024:")
    ny_film_liste = oslo.finn_filmer_periode(2000,2024)
    # Skriver ut titlene på filmer som returneres (bruk hent_tittel).
    for film in ny_film_liste:
        print(Film.hent_tittel(film))
    # Kontroller at resultatene er som forventet
    joker_film = oslo.finn_film_tittel("Joker")
    assert joker_film is not None
    assert joker_film.hent_aar() == 2019
    print("Testen er bestått, Joker filmen har dato 2019")
    print()

    # Kall på finn_film_periode med argumentene etter=2020 og før=2020
    liste2 = oslo.finn_filmer_periode(2020, 2020)
    print("Leter etter filmer produsert etter 2020 og før 2020:")
    # Kontroller at resultatet er som forventet (tom liste) med assert (evt skriv ut)
    assert liste2 == []
    print("Liste2 er tom og testen er bestått")
    print()
    # SKriv ut all info om alle filmer og sjekk at resultatet er som forventet
    print("Utskrift alle filmer")
    oslo.skriv_ut_alle_filmer()

testprogram()
