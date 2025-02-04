class Celle:
    # Konstruktør
    def __init__(self):                         # etablerer en instans celle av rutenett som brukes i abstraksjonsnivået over i rutenett.py
        self._status = "doed"                   # default, en celle settes som status: doed
        self._naboer = []
        self._ant_levende_naboer = 0 

    def sett_doed(self):                        # gir en celle status doed
        self._status = "doed"

    def sett_levende(self):                     # gir en celle status levende
        self._status = "levende"

    def er_levende(self):                       # returner True hvis en celle er levende og False hvis den er død
        if self._status == "levende":
            return True
        else:
            return False

    def hent_status_tegn(self):                 # returnerer O hvis en celle er levende
        if self._status == "levende":           # returnerer . hvis en celle er doed
            return "O"
        elif self._status == "doed":
            return "."

    def legg_til_nabo(self, nabo):              # legger til data fra parameteret til listen self._naboer
        self._naboer.append(nabo)

    def tell_levende_naboer(self):              # itererer gjennom listen self._naboer og oppdaterer self._ant_levende_naboer med antall levende celler
        levende_naboer = 0
        for nabo in self._naboer:
            if nabo.er_levende():
                levende_naboer += 1
        self._ant_levende_naboer = levende_naboer

    def oppdater_status(self):                  # regler for om en celle skal doe, kommer til live eller kan fortsette å leve
        if self._status == "levende":           # cellen blir oppdatert til doed eller levende basert på om den treffer kriteriene
            if self._ant_levende_naboer < 2:
                self._status = "doed"
            elif 2 <= self._ant_levende_naboer <= 3:
                self._status = "levende"
            elif self._ant_levende_naboer > 3:
                self._status = "doed"
        elif self._status == "doed":
            if self._ant_levende_naboer == 3:
                self._status = "levende"
