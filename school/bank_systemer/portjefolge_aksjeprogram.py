# Start med å sette inn aksjebeholdninger og kontantbeholdning til 0
bitcoin = 0
apple = 0
nvida = 0
cash = 0

# Velkomstmelding til brukeren
print("\nHei og velkommen til IFI investering!")

# Funksjon for å vise portefølje og tilby brukerens manøvrering
def minside():
    global bitcoin, nvida, apple, cash
    print(f"\nDin portjefølge ser slik ut:\nBTC:{bitcoin},-kr\nNVIDA:{nvida},-kr\nApple:{apple},-kr\nCash:{cash},-kr")
    manøvrering = input("\nSkriv inn ett av alternativene (selge/ kjøpe/ innskudd eller uttak): ")
    if manøvrering.lower() == "selge":
        selge()
    elif manøvrering.lower() == "kjøpe":
        kjøpe()
    elif manøvrering.lower() == "innskudd eller uttak":
        innskudd_uttak()
    else:
        print("\nDu tastet inn feil verdi, prøv på nytt\n")
        minside()

# Funksjon for å gjøre innskudd eller uttak av cash
def innskudd_uttak():
    global bitcoin, nvida, apple, cash
    penger = input("\nSkriv inn ett av alternativene (innskudd eller uttak): ")
    if penger.lower() == "innskudd":
        innskudd = float(input("\nSkriv kroner sum i innskudd:"))
        cash = cash + innskudd 
    elif penger.lower() == "uttak":
        uttak = float(input("\nSkriv kroner sum du ønsker å ta ut:"))
        cash = cash - uttak
    else: 
        print("Du har tastet feil verdier, prøv igjen")
    minside()

# Funksjon for å kjøpe aksjer i Bitcoin, Nvidia og Apple
def kjøpe():
    global bitcoin, nvida, apple, cash
    invest = float(input("\nSkriv inn totalsummen du ønsker å investere for: "))
    b = float(input("\nTast inn din prosent(0-100) du ønsker å eksponere innskuddet ditt for i BTC: "))
    n = float(input("\nTast inn din prosent(0-100) du ønsker å eksponere innskuddet ditt for i nvida: "))
    a = float(input("\nTast inn din prosent(0-100) du ønsker å eksponere innskuddet ditt for i apple: "))
    bitcoin = bitcoin + (invest) * (b / 100)
    nvida = nvida + (invest) * (n / 100)
    apple = nvida + (invest) * (a / 100)
    cash = cash - bitcoin - nvida - apple
    minside()

# Funksjon for å selge investeringene sine og ta ut penger til cash
def selge():
    global bitcoin, nvida, apple, cash
    salg = input("\nHvilken investering ønsker du å selge?: ")
    andel = float(input("\nHvor mye ønsker du å selge for, i kroner?:"))
    if salg.lower() == "bitcoin":
        bitcoin -= andel
        cash += andel
    elif salg.lower() == "nvida":
        nvida -= andel
        cash += andel
    elif salg.lower() == "apple":
        apple -= andel
        cash += andel
    else: 
        print("Du har brukt ugyldige verdier, verdiene er bitcoin, nvida og apple")
    minside()

# Starter programmet og viser brukerens side
minside()
