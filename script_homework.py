
print("Aufgabe 1: Einfache Mathematik")
# Variablen
zahl1 = 34
zahl2 = 67

# Berechnung
print("Zahl 1 + Zahl 2:", zahl1 + zahl2)
print("Zahl 1 - Zahl 2:", zahl1 - zahl2)
print("Zahl 1 * Zahl 2:", zahl1 * zahl2)
print("Zahl 1 / Zahl 2:", zahl2 / zahl1)


#Aufgabe 2
print("Aufgabe 2: Durchschnitt berechnen")

# Variablen
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))
zahl3 = float(input("Gib die dritte Zahl ein: "))

# Berechnung Durchschnitt
durchschnitt = (zahl1 + zahl2 + zahl3) / 3

# Ergebnis 
print(f"Der Durchschnitt der drei Zahlen ist: {durchschnitt}")


#Aufgabe 3
print("Aufgabe 3. Kilometer in Meilen umrechnen")

a = input("Wie viele Kilometer sollen in Meilen umgerechnet werden?")
b="10"
def km_to_miles(km):
    x = float(km)
    c = float(0.621371)
    d=x*c
    return d

print (a, "Kilometer entsprechen: ", km_to_miles(a), "Meilen")
print (b, "Kilometer entsprechen: ", km_to_miles(b), "Meilen")