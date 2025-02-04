# Funksjon som legger sammen to tall og returnerer resultatet
def addisjon(tall1, tall2):
    return int(tall1) + int(tall2)  # Legger sammen tallene og returnerer resultatet

# Tester addisjon-funksjonen med to tall
print(f"resultatet er: {addisjon(5, 4)}")  # Kaller funksjonen med 5 og 4 som argumenter og skriver ut resultatet

# Funksjon som subtraherer tall2 fra tall1 og returnerer resultatet
def subtraksjon(tall1, tall2):
    return int(tall1) - int(tall2)  # Subtraherer tall2 fra tall1 og returnerer resultatet

# Tester subtraksjon-funksjonen med forskjellige tall og validerer med asserts
assert subtraksjon(10, 5) == 5  # Sjekker at resultatet er 5
assert subtraksjon(-10, -5) == -5  # Sjekker at resultatet er -5
assert subtraksjon(-10, 5) == -15  # Sjekker at resultatet er -15

# Funksjon som deler tall1 med tall2 og returnerer resultatet
def divisjon(tall1, tall2):
    return int(tall1) / int(tall2)  # Deler tall1 med tall2 og returnerer resultatet

# Tester divisjon-funksjonen med forskjellige tall og validerer med asserts
assert divisjon(100, 2) == 50  # Sjekker at resultatet er 50
assert divisjon(-10, -2) == 5  # Sjekker at resultatet er 5
assert divisjon(-10, 2) == -5  # Sjekker at resultatet er -5

# Funksjon som konverterer tommer til centimeter
def tommer_til_cm(antall_tommer):
    assert float(antall_tommer) > float(0)  # Sjekker at antall tommer er større enn 0
    return antall_tommer * 2.54  # Konverterer tommer til centimeter og returnerer resultatet

# Tester konvertering fra tommer til centimeter
print(tommer_til_cm(1))  # Kaller funksjonen med 1 tomme og skriver ut resultatet i cm

# Funksjon som gjør beregninger basert på brukerens input
def skriv_beregninger():
    # Brukerinput for to tall
    bruker1 = float(input("skriv inn ditt første tall:"))
    bruker2 = float(input("skriv inn ditt andre tall:"))
    
    # Beregner og skriver ut addisjon, subtraksjon og divisjon
    print("addisjon av tallene: ", addisjon(bruker1, bruker2))
    print("subtraksjon av tallene: ", subtraksjon(bruker1, bruker2))
    print("divisjon av tallene: ", divisjon(bruker1, bruker2))
    
    # Brukerinput for tommer
    bruker3 = float(input("skriv inn ditt tredje tall i tommer:"))
    
    # Beregner og skriver ut resultatet i centimeter
    print("tommer til cm:", tommer_til_cm(bruker3))

# Kaller funksjonen som gjør beregningene basert på brukerens input
skriv_beregninger()
