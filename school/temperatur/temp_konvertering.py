# Spør brukeren om temperaturen i fahrenheit
temp_fahrenheit = float(input("Skriv in temperaturen i fahrenheit: "))

# Skriver ut temperaturen i fahrenheit
print(f"{"Temperatur i fahrenheit: ": >10} {temp_fahrenheit:.2f}")

# Konverterer fahrenheit til celsius
celsius = (((temp_fahrenheit) - 32) * (5/9))

# Skriver ut temperaturen i celsius
print(f"{"Temperatur i celsius: ": >10} {celsius:.2f}")
