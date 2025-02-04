# Skriver ut en hilsen til brukeren
print("\nHei Student \n")

# Lar brukeren oppgi sitt navn og skriver det ut
navn = input("Hei, hva heter du?: ")
print("\nHei", navn)

# Definerer to heltallsvariabler og skriver ut deres verdier
a = 2
b = 1
print()
print(a)
print(b)

# Beregner differansen mellom variablene a og b
c = a - b 
print(c)

# Ber brukeren om å oppgi et nytt navn og kombinerer de to navnene
navn2 = input("\nHar du muligheten til å skrive inn ett nytt navn: ")
sammen = navn + navn2
print("\nDu har skrevet inn navne:", sammen)

# Kombinerer navnene med "og" for å skape et naturlig mellomrom
sammen = navn + " og " + navn2 
print("\nDu har skrevet inn navne:", sammen)
print()
