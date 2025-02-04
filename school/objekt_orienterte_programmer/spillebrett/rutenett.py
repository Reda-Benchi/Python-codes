from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader  # Antall rader i rutenettet
        self._ant_kolonner = kolonner  # Antall kolonner i rutenettet
        # Initialiserer rutenettet som en 2D-liste med None-verdier
        self._rutenett = [[None for _ in range(kolonner)] for _ in range(rader)]

    def fyll_med_tilfeldige_celler(self):
        # Fyller rutenettet med tilfeldige celler, noen levende og noen døde
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self._rutenett[rad][kol] = self.lag_celle()

    def lag_celle(self):
        celle = Celle()  # Oppretter en ny celle
        if randint(0, 2) == 1:
            celle.sett_levende()  # Setter cellen til å være levende med 50% sjanse
        return celle

    def hent_celle(self, rad, kol):
        # Henter cellen på spesifisert rad og kolonne, hvis den er innenfor rutenettets grenser
        if 0 <= rad < self._ant_rader and 0 <= kol < self._ant_kolonner:
            return self._rutenett[rad][kol]
        return None

    def tegn_rutenett(self):
        # Skriver ut rutenettet i konsollen, viser levende celler som "O" og døde celler som "."
        for rad in self._rutenett:
            print("".join(celle.hent_status_tegn() for celle in rad))

    def _sett_naboer(self, rad, kol):
        celle = self.hent_celle(rad, kol)
    

