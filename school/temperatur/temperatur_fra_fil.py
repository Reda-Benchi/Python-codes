# Funksjon for å lese en CSV-fil og returnere en ordbok med måneder som nøkler og temperaturer som verdier
def dokument(csv_fil): 
    min_fil = open(csv_fil)  # Åpner filen i lesemodus
    ordbok = {}  # Initialiserer en tom ordbok
    
    for linje in min_fil:  # Itererer gjennom hver linje i filen
        linje = linje.strip().split(",")  # Fjerner mellomrom og deler linjen på komma
        måned = linje[0]  # Første verdi er måneden
        temp = float(linje[1])  # Andre verdi er temperaturen, konverteres til float
        ordbok[måned] = temp  # Legger til måned som nøkkel og temperatur som verdi i ordboken
    
    min_fil.close()  # Lukker filen
    return ordbok  # Returnerer ordboken

print(dokument("max_temperatures_per_month.csv"))  # Skriver ut resultatet av funksjonskallet

# Funksjon for å finne den varmeste dagen i et gitt år ved å sammenligne daglige temperaturer med månedens maks
def varmeste_dag(daglig_temp, måndelig_temp): 
    daglig_fil = open(daglig_temp)  # Åpner filen for daglige temperaturer i lesemodus
    ordbok_måned = måndelig_temp  # Bruker ordboken fra dokument-funksjonen
    ordbok_max = {}  # Initialiserer en tom ordbok for maks-temperaturene

    for linje in daglig_fil:  # Itererer gjennom hver linje i filen
        linje = linje.strip().split(",")  # Fjerner mellomrom og deler linjen på komma
        måned = linje[0]  # Første verdi er måneden
        dag = linje[1]  # Andre verdi er dagen
        temp = float(linje[2])  # Tredje verdi er temperaturen, konverteres til float

        if måned not in ordbok_max:  # Hvis måneden ikke finnes i ordboken, legg den til
            ordbok_max[måned] = (dag, temp)
        if temp > ordbok_måned[måned]:  # Hvis den nåværende temperaturen er høyere enn månedens maks
            ordbok_max[måned] = dag, temp  # Oppdaterer rekordene for den varmeste dagen
            print(f"Ny varmerekord den {dag} {måned} ga: {temp} grader (gammel varmerekord var {ordbok_måned[måned]} grader)") 
            # Skriver ut ny rekord og gammel rekord

    daglig_fil.close()  # Lukker filen
    return ordbok_max  # Returnerer den oppdaterte ordboken med maks-temperaturene

oppdater_ordbok = varmeste_dag("max_daily_temperature_2018.csv", dokument("max_temperatures_per_month.csv"))

# Bonusfunksjon for å skrive den oppdaterte ordboken til en ny fil
def bonus1(oppdater_temp, ny_fil):
    ny_fil = open(ny_fil, "w")  # Åpner filen i skribemodus
    ordbok = oppdater_temp  # Bruker ordboken fra forrige funksjon

    for i in ordbok:  # Itererer gjennom ordboken
        ny_fil.write(f"{i},{ordbok[i][0]},{ordbok[i][1]}\n")  # Skriver måneden, dagen og temperaturen til filen
    ny_fil.close()  # Lukker filen

bonus1(oppdater_ordbok, "ny_fil")  # Kaller funksjonen for å lage den nye filen

# Bonusfunksjon for å identifisere en hetebølge basert på sammenhengende dager med temperaturer over 25 grader
def varmeboelge(daglig_temp): 
    daglig_temp = open(daglig_temp)  # Åpner filen med daglige temperaturer
    teller = 0  # Initialiserer telleren
    varmebølge = []  # Initialiserer en tom liste for hetebølgen

    for linje in daglig_temp:  # Itererer gjennom hver linje i filen
        linje = linje.strip().split(",")  # Fjerner mellomrom og deler linjen på komma
        måned = linje[0]  # Første verdi er måneden
        dag = linje[1]  # Andre verdi er dagen
        temp = float(linje[2])  # Tredje verdi er temperaturen, konverteres til float

        if teller == 5:  # Hvis 5 sammenhengende hete dager er nådd, skriv ut hetebølgen
            print(f"Starten av varmebølgen var {varmebølge[0]} og slutten var {varmebølge[4]}")
            teller = 0  # Nullstiller telleren
            varmebølge = []  # Nullstiller listen

        if temp > 25:  # Hvis temperaturen er over 25 grader
            varmebølge.append((måned, dag))  # Legger måneden og dagen til i listen for hetebølgen
            teller += 1  # Øker telleren
        else: 
            teller = 0  # Nullstiller telleren hvis temperaturen er under 25 grader
            varmebølge = []  # Nullstiller listen

varmeboelge("max_daily_temperature_2018.csv")  # Kaller funksjonen for å identifisere hetebølgen

