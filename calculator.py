# Taschenrechner


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


def calculator():
    choice = input("Wähle Option(1/2/3/4): ")

    if choice in ("1", "2", "3", "4"):
        try:
            zahl1 = float(input("Gib deine erste Zahl ein: "))
            zahl2 = float(input("Gib deine zweite Zahl ein: "))
        except ValueError:
            print("Ungültige Eingabe, bitte gib eine Zahl ein.")
        if choice == "1":
            print(add(zahl1, zahl2))

        elif choice == "2":
            print(subtract(zahl1, zahl2))

        elif choice == "3":
            print(mult(zahl1, zahl2))

        elif choice == "4":
            print(div(zahl1, zahl2))
    else:
        print("Ungültige Eingabe")


print("Wähle deine Rechenoperation.")
print("1.Addition")
print("2.Subtraktion")
print("3.Multiplikation")
print("4.Division")
calculator()
