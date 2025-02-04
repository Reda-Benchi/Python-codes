from film import Film 

class Filmklubb: 
    def __init__(self): # konstruktør  
        self._filmer = [] # Instansvariabel med en tom liste 
    
    def les_filmer_fra_fil(self, filnavn): # leser fil og gjør om til str
        self._fil = open(filnavn, "r") # åpner filen
        for linje in self._fil: # iterer igjennom hver linje i filen
            linje = linje.strip().split(";") # fjerner hvit tekst og slpitter på ;
            film = Film(linje[0], int(linje[1])) # kaller på klassen Film og lager nytt objekt med tittel som [0] og år som [1]
            self._filmer.append(film) # legger til objektet til tomme listen
        self._fil.close() # lukker filen

    def skriv_ut_alle_filmer(self): # Utskrift av alle filmer
        for objekt in self._filmer: # itererer gjennom listen med objekter
#(siden klassen Film er brukt til å opprette objekt og legge til listen i linje 6, så har vi tilgang til denne klassen ved bruk av denne listen)
            objekt.skriv_ut_film() # kaller på utskrift fra klassen Film og metode skriv_ut_film() for hvert objekt
        
    def registrer_film(self): # henter ny tittel og årstall fra terminal og lagrer dette i et nytt objekt
        objekt = Film(input("Skriv inn en film-tittel: "), int(input("skriv inn filmens årstall: ")))
        for film in self._filmer: # itererer gjennom listen med lagrede titler og årstall (linje 6)
            if film == objekt: # gir bolsk verdi gjennom sammenligning ved bruk av __eq__ fra klassen Film 
                print("\nFeilmelding: denne filmen og dette årstallet er registrert") # hvis filmen er i listen så skrives feilmelding ut
                return 
        self._filmer.append(objekt) # når iterasjonen er ferdig så legges film og årstall til listen hvis de ikke finnes der

    def finn_film_tittel(self, tittel: str): # returnerer filmen fra listen hvis paramteret er likt
        film_objekt = Film(tittel, None) # opretter nytt objekt i klassen Film
        for film in self._filmer: # iterer gjennom listen
            if film.sjekk_tittel(film_objekt.hent_tittel()): # hvis de første tegnene er like som ett filmene i listen
                return film
        return None # hvis ingen film ikke er i listen så returnes None
    
    def legg_til_skuespiller(self, film:"Film"): # legger til skuespillernavn og rolle til klassen Film
# tilordner paramater film objekt for klassen Film
        navn = input("Hva er navnet på skuespilleren?: ") # skuespillernavn -> input fra terminal
        rolle = input("Hva er rollen til skuespilleren?: ") # rolle -> input fra terminal
        film.ny_skuespiller(navn, rolle) # tilordner objektet film ny skuespiller (navn,rolle) gjennom metoden ny_skuespiller i klassen Film

    def finn_filmer_periode(self, år_1: int, år_2: int): # legger til filmene som er imellom parameterne
        liste = [] # tom liste
        for film in self._filmer: # itererer gjennom listen i instansvariablen 
            årstall = int(Film.hent_aar(film)) # for hver iterasjon henter vi instansvariabel self._aar fra klassen Film og endrer formen til int()
            if årstall > år_1 and årstall < år_2: # sjekker årstall i instansvariabel møter kriteriene (imellem år 1 og år 2)
                liste.append(film) # hvis True, legges filmen til en ny liste
        return liste # returnerer listen
    
