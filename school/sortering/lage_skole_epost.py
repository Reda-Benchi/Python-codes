# Funksjon for å lage brukernavn basert på fornavn og første bokstav av etternavn
def lag_brukernavn(navn):
    delt_navn = navn.lower().strip().split()  # Gjør navnet små bokstaver og deler på mellomrom
    return delt_navn[0] + delt_navn[1][0]  # Kombinerer fornavn og første bokstav i etternavn

# Funksjon for å lage epostadresse med prefix og suffix
def lag_epost(prefix, sufix):
    return prefix.lower() + "@" + sufix.lower()  # Kobler sammen prefix og suffix, og gjør små bokstaver

# Funksjon for å skrive ut eposter fra ordboken
def skriv_ut_eposter(ordboken):
    for i in ordboken:  # Itererer gjennom ordboken
        print(f"eposten til {i}: {lag_epost(i, ordboken[i])}")  # Skriver ut eposten til hver bruker

# Eksempel på en ordbok med navn og tilhørende domene
ordbok = {"olan": "ifi.uio.no", "karin": "student.matnat.uio.no"}
skriv_ut_eposter(ordbok)  # Kaller funksjonen for å skrive ut eposter

# Løkke som gir brukeren mulighet til å legge til nye brukere eller vise eposter
nyordbok = {} 
bruker = input("Velkommen, ønsker du å starte? svar ja/nei: ").lower()  # Spør om brukeren vil starte
while bruker == "ja":
    svar = input("tast bokstaven i, p eller s: ")  # Spør om ønsket handling

    if svar == "i":  # Hvis bruker ønsker å legge til en ny bruker
        navn = input("skriv inn ett navn: ") 
        suffix = input("skriv inn en epost suffix: ")
        epost = lag_epost(navn, suffix)  # Lag epostadresse
        nyordbok[navn] = epost  # Legg til brukeren i ordboken
    if svar == "p":  # Hvis bruker ønsker å printe ut alle eposter
        skriv_ut_eposter(nyordbok)  # Kall på funksjon for å skrive ut alle eposter
    if svar == "s":  # Hvis bruker ønsker å avslutte programmet
        break  # Bryt ut av løkken
