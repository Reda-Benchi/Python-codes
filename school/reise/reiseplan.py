# Reiseplanlegger program gjennom nøstete lister

# Tom liste for reisemål
steder = [] 
# Tom liste for klær
klessplagg = []
# Tom liste for avreisedato
avreisedato = []

# Brukeren fyller inn reiseinformasjon for 5 reisemål
for i in range(5):  # Løkke som går 5 ganger
    reise = input("Skriv inn ditt reisemål: ")  # Brukeren skriver inn reisemål
    steder.append(reise)  # Legger til reisemålet i listen 'steder'
    klær = input("Skriv inn dine klær: ")  # Brukeren skriver inn klær
    klessplagg.append(klær)  # Legger til klærne i listen 'klessplagg'
    dato = input("Skriv inn din reisedato: ")  # Brukeren skriver inn dato
    avreisedato.append(dato)  # Legger til datoen i listen 'avreisedato'

# Lager en liste som inneholder de tre andre listene (steder, klessplagg og avreisedato)
reiseplan = []
reiseplan.append(steder)  # Legger til reisemålene
reiseplan.append(klessplagg)  # Legger til klærne
reiseplan.append(avreisedato)  # Legger til avreisedatoene

# Skriver ut hele reiseplanen
for n in reiseplan:
    print(n)

# Brukeren velger en indeks for å vise spesifikk informasjon fra reiseplanen
liste_indeks1 = int(input("Velg en indeks mellom 0 og 2: "))  # Velg kategori (steder, klær eller dato)
liste_indeks2 = int(input("Velg en indeks mellom 0 og 4: "))  # Velg spesifikk reise

# Hvis begge indeksene er gyldige, vises den valgte informasjonen
if 0 <= liste_indeks1 <= 2 and 0 <= liste_indeks2 <= 4:
    print(f"Du har valgt: {reiseplan[liste_indeks1][liste_indeks2]}")
else:
    print("Ugyldig verdi")  # Hvis indeksene er utenfor gyldige områder

