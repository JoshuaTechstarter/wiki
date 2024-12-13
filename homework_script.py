
#1. Namensabfrage mit Input
firstname = input("Gib deinen Vornamen ein:")
lastname = input("Gib deinen Nachnamen ein:")

name_full = firstname +" "+ lastname

print(f"Der vollständige Name lautet: {name_full}" )

#2. Addition von Zahlen
a = float(input("Zahl 1:"))
b= float(input("Zahl 2:"))

c = (a + b)

print(f"Ergebnis: {c}")

#3. Zusatzaufgabe: Einfache If-Bedingung

zahl = (input("Gib eine Zahl zum prüfen an:"))
zahl1 = float(zahl)

if zahl1 > 0:
    print("Die Zahl ist positiv")
elif zahl1 == 0:
    print("Die Zahl ist null")
else :
    print("Die Zahl ist negativ")

 istgerade = (zahl1 == 2 and zahl1 != -1) or (zahl1 % 2 == 0)

 if not istgerade:
     print("Die Zahl ist ungerade.")
 else:
     print("Die Zahl ist gerade.")





