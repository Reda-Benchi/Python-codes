# Dette programmet holder oversikt over hva beboerne på et sykehjem spiser til hvert måltid.
# Programmet lar brukeren finne ut hva en spesifikk beboer spiser til frokost, lunsj og middag.

# Ordbok med 5 forskjellige beboere og hva de spiser
sykehjem = {
    "mats": [{"frokost": ["havregryn"]}, {"lunsj": ["smørbrød"]}, {"middag": ["laks"]}],
    "ina": [{"frokost": ["yoghurt"]}, {"lunsj": ["suppe"]}, {"middag": ["burger"]}],
    "jon": [{"frokost": ["egg"]}, {"lunsj": ["taco"]}, {"middag": ["pizza"]}],
    "ingrid": [{"frokost": ["brød"]}, {"lunsj": ["salat"]}, {"middag": ["pasta"]}],
    "abdi": [{"frokost": ["frukt"]}, {"lunsj": ["sushi"]}, {"middag": ["ørret"]}]
}

# Funksjon for å finne hva en beboer spiser
def beboere():
    global sykehjem
    # Printer ut nøklene til ordboken sykehjem (beboernes navn)
    print(sykehjem.keys())
    
    # Input som lar brukeren finne hva en spesifikk beboer spiser
    navn = input("Skriv inn navn på beboer: ")
    
    # Beslutning som gir verdiene til ordboken eller gir feilmelding hvis beboeren ikke er på sykehjemmet
    if navn in sykehjem:
        print(sykehjem[navn])  
    else: 
        print("Beboeren er ikke registrert på sykehjemmet.")

# iverksetter prosedyren
beboere()
