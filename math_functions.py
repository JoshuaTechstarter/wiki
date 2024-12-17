# Mathematische Funktionen zum import in calculator.py
# Additions-Funktion
def add(zahl1, zahl2):
    return zahl1 + zahl2


# Substraktions-Funktion
def subtract(zahl1, zahl2):
    return zahl1 - zahl2


# multiplikation-Funktion
def mult(zahl1, zahl2):
    return zahl1 * zahl2


# Division-Funktion
def div(zahl1, zahl2):
    return zahl1 / zahl2


# km to miles
def km_to_miles(km):
    zahl1 = float(km)
    return zahl1 * float(0.621371)


# miles to km
def miles_to_km(m):
    zahl1 = float(m)
    return zahl1 / float(0.621371)


# print (a, "Kilometer entsprechen: ", km_to_miles(a), "Meilen")
