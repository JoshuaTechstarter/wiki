# Funktion die User nach Alter fragt und auf Konsole ausgibt


def altersabfrage():
    age = input("Gib dein Alter ein: ")
    print(f"Dein Alter ist", (age))


altersabfrage()


def namensabfrage():
    name = input("Was ist dein Name? ")
    print(f"Hallo", (name))


def namensabfrage2():
    name = input("Was ist dein Name? ")
    return f"Du bist also {name}"


namensabfrage()
namensabfrage2()
