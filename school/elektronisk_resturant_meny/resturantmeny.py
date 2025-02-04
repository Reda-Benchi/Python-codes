# Skriver ut restaurantens meny
print("\nMISELINGRESTAURANTEN MENY")

# Definerer hovedretter og tilbehør som variabler
meny1 = "Biff"
meny2 = "Salat"
meny3 = "Kyllinglår" 
tilbehør1 = "Bearnaisesaus"
tilbehør2 = "Gulrøtter"

# Vist meny med hovedretter og tilbehør
print("\nHovedretter:\n", meny1, "\n", meny2, "\n", meny3)
print("\nTilbehør:\n", tilbehør1, "\n", tilbehør2)

# Brukeren velger sin hovedrett og tilbehør
hovedrett = input("\nSkriv inn din ønskelige hovedrett her: ")
tilbehør = input("Skriv inn ditt ønskelige tilbehør her: ")

# Programmet gir et svar basert på brukerens valg
if hovedrett == meny2 and tilbehør == tilbehør1:
    print("Du har valgt Salat med bearnaisesaus")
elif (hovedrett == meny1 or hovedrett == meny3) and tilbehør != tilbehør2:
    print("Du spiser ikke nok grønnsaker!")
elif hovedrett == meny2 and tilbehør == tilbehør2:
    print("Du har valgt et vegetarmåltid")
elif hovedrett == meny1 and tilbehør == tilbehør2:
    print("Du har valgt Biff med gulrøtter")
elif hovedrett == meny3 and tilbehør == tilbehør2:
    print("Du har valgt Kyllinglår med gulrøtter")
