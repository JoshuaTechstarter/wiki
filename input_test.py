def add():
    zahl1 = input("Gib die erste Zahl ein: ")
    if not zahl1.isdigit():
        return "Ungültige Eingabe"

    zahl2 = input("Gib die zweite Zahl ein: ")
    if not zahl2.isdigit():
        return "Ungültige Eingabe"

    return int(zahl1) + int(zahl2)


print(add())
