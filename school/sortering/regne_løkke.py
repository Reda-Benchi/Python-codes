# Program som lar brukeren legge inn tall, og utfører ulike beregninger med disse tallene

# Starter løkken med verdi 1, slik at den kjører minst én gang
verdi = 1 
liste = []  # Tom liste for å lagre tallene som brukeren legger inn
while verdi != 0:  # Løkke som avsluttes når bruker skriver inn 0
    verdi = int(input("Skriv inn ett tall: "))  # Brukerens input
    if verdi != 0:  # Legger bare til tallene i listen hvis de ikke er 0
        liste.append(verdi)

# Skriver ut alle elementene i listen
for element in liste:
    print(element)

# Summerer alle verdiene i listen
min_sum = 0 
for i in liste:
    min_sum += i  # Legger sammen alle verdiene
print(f"Summen er: {min_sum}")

# Finner største verdi
størst = liste[0]  # Setter den første verdien som størst
for e in liste:
    if e > størst:  # Hvis et element er større enn nåværende største
        størst = e  # Oppdaterer størst verdi

# Finner minste verdi
minst = liste[0]  # Setter den første verdien som minst
for r in liste:
    if r < minst:  # Hvis et element er mindre enn nåværende minste
        minst = r  # Oppdaterer minst verdi

print(f"Største verdi: {størst}")
print(f"Minste verdi: {minst}")
