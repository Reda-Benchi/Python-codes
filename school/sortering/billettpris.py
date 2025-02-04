# Dette programmet beregner billettprisen basert på alder.

# Input for brukerens alder
alder = int(input("Skriv inn alderen: "))

# Initial billettpris
billettpris = 0

# Funksjon som beregner billettprisen basert på alder
def bilett():
    global alder
    global billettpris
    
    # Beslutning for billettpris basert på alder
    if alder <= 17:
        billettpris = 30      # Billettpris for personer 17 år eller yngre
    elif alder >= 63:
        billettpris = 35      # Billettpris for personer 63 år eller eldre
    else:
        billettpris = 50      # Billettpris for personer mellom 18 og 62 år

    # Skriver ut billettprisen
    print("Billettprisen din er: ", billettpris, ",-kr")

# Kaller på funksjonen for å beregne billettprisen
bilett()
