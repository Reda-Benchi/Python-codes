# Funksjon som tar to tall som input og returnerer summen deres
def addere(tall1, tall2): 
    return int(tall1) + int(tall2)  # Legger sammen tallene og returnerer resultatet

# Tester addere-funksjonen med to sett av tall
print("Kall 1: ", addere(5, 4))  # Kaller funksjonen med tallene 5 og 4, resultatet vises
print("Kall 2: ", addere(10, 12))  # Kaller funksjonen med tallene 10 og 12, resultatet vises

# Tar inn tekst og bokstav fra brukeren
tekst = input("Skriv inn en tekststreng: ") 
bokstav = input("Skriv inn en bokstav: ") 

# Funksjon som teller hvor mange ganger en bokstav forekommer i en tekst
def tell_forekomst(min_tekst, min_bokstav):
    teller = 0  # Initialiserer telleren til 0
    for bokstaver in tekst:  # Går gjennom hver bokstav i teksten
        if bokstaver == bokstav:
