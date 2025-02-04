class Film: 
    def __init__(self, tittel: str, aar: int):  # Konstruktør som initialiserer en film med tittel og årstall
        self._tittel = tittel  # Lagrer filmens tittel
        self._aar = aar  # Lagrer filmens utgivelsesår
        self._skuespiller = {}  # Oppretter en tom ordbok for skuespillere og deres roller
    
    def hent_tittel(self):  # Returnerer filmens tittel
        return str(self._tittel)
    
    def ny_skuespiller(self, navn: str, rolle: str):  # Legger til en skuespiller med tilhørende rolle hvis ikke allerede registrert
        if navn not in self._skuespiller:
            self._skuespiller[navn] = rolle  # Legger til skuespilleren i ordboken
        else:
            print("Feilmelding: denne skuespilleren er allerede lagt til filmen")  # Feilmelding hvis skuespilleren finnes fra før
    
    def hent_alle_skuespiller_navn(self):  # Returnerer en liste over navnene til skuespillerne i filmen
        return list(self._skuespiller.keys())  # Henter nøklene (skuespillernes navn) fra ordboken
    
    def skriv_ut_film(self):  # Skriver ut filmens informasjon inkludert skuespillere
        print(f"Film: {self._tittel}\nÅr: {self._aar}\nMedvirkende:")
        for navn in self._skuespiller:  # Itererer gjennom ordboken og skriver ut navn og rolle
            print(f"{navn} som {self._skuespiller[navn]}")
    
    def sjekk_periode(self, aar_1: int, aar_2: int):  # Sjekker om filmen ble laget mellom to gitte år
        return aar_1 < self._aar < aar_2  # Returnerer True hvis årstallet er innenfor perioden
    
    def sjekk_tittel(self, tittel_start: str):  # Sjekker om filmens tittel starter med en gitt tekst
        if self._tittel.split(" ")[0] == tittel_start.split(" ")[0]:  # Sammenligner første ord i tittelen
            return True
        elif tittel_start == "":  # Hvis tittel_start er tom, returner True
            return True
        elif len(tittel_start) > len(self._tittel):  # Hvis tittel_start er lengre enn hele tittelen, returner False
            return False
        else:
            return False  # Sikrer at funksjonen alltid returnerer en verdi
    
    def __str__(self):  # Returnerer en strengrepresentasjon av filmobjektet
        pen_string = f"Film: {self._tittel}\nÅr: {self._aar}\nMedvirkende:\n"
        for navn in self._skuespiller:  # Legger til alle skuespillere og deres roller
            pen_string += f"{navn} som {self._skuespiller[navn]}\n"
        return pen_string
    
    def __eq__(self, annen: "Film"):  # Sjekker om to filmer er like basert på tittel og år
        return (self._tittel.strip().lower() == annen._tittel.strip().lower() and int(self._aar) == int(annen._aar))
    
    def hent_aar(self):  # Returnerer filmens utgivelsesår
        return self._aar
