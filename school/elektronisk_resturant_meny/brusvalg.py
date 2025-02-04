# Spør brukeren om de ønsker brus
brus = input("\nGod dag. Har du lyst på brus?\nSkriv svar her: ")

# Programmet håndterer svarene med if, elif og else
if brus == "ja":
    print("\nHer har du en brus\n")
elif brus == "nei": 
    print("\nDen er grei.\n")
else: 
    print("\nDet forsto jeg ikke helt\n")
