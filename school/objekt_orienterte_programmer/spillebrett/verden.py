from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):                            # objketet verden brukes i abstraksjonsnivået over i hovedprogram.py
        self._rader = rader
        self._kolonner = kolonner 
        self._rutenett = Rutenett(self._rader, self._kolonner)      # fyller inn parametre fra verden og etablerer instansen Rutenett
        self._generasjonsnummer = 0                                 # holder styr generasjon, oppdatering gir +1 generasjon
        self._rutenett.fyll_med_tilfeldige_celler()                 # etablerer tilfeldige instanser i instansen self._rutenett
        self._rutenett.koble_celler()                               # i instansen rutenett etableres det referanser for hver celle (instans) til naboene rundt

    def tegn(self):                                                 # Tegner rutenettet
        self._rutenett.tegn_rutenett()
        print(f"Generasjonsnummer: {self._generasjonsnummer}\nAntall levende celler: {self._rutenett.antall_levende()}")
        print()

    def oppdatering(self):                                          # teller antall naboer(referanser) per celle(instans) i rutenett og gir cellen status levende eller doed
        alle_celler = self._rutenett.hent_alle_celler()
        for celle in alle_celler:
            celle.tell_levende_naboer()
        
        for celle in alle_celler:   
            celle.oppdater_status()
        self._generasjonsnummer += 1
