from verden import Verden

def hovedprogram():
    rader = input("Tast inn antall rader du ønsker i spillbrettet: ")       # bruker fører inn input: antall rader
    kolonner = input("Tast inn antall kolonner du ønsker i spillbrettet: ") # bruker fører inn input: antall kolonner
    verden = Verden(int(rader),int(kolonner))                               # opprettelse av objekt
    verden.tegn()                                                           # tegner objektet

    inp = ""
    
    while inp != "q":                                                       # løkke: brukeren taster inn q for å avslutte og space for fortsette
        inp = input('Tast inn bokstaven "q" for å avslutte og mellomrom (" ") for å gå videre: ').lower()
        if inp == " ":
            verden.oppdatering()                                            # oppdaterer objektet
            verden.tegn()                                                   # tegner det oppdaterte objektet
        
# starte hovedprogrammet
hovedprogram()
