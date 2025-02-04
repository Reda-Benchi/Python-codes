# Funksjon for å hente brukerens navn og bosted og skrive ut en hilsen
def utskriftsprosedyre():
    hilsen = input("Hei, velkommen til IFI maskinen\nHva heter du?: ")
    bosted = input("Hva er ditt bosted?: ")
    print(f"Hei {hilsen}. Det er hyggelig å møte deg. Du er fra {bosted}.\n")

# Kaller på funksjonen flere ganger for å skrive ut hilsen til brukeren
utskriftsprosedyre()
utskriftsprosedyre()
utskriftsprosedyre()
