import math_functions

# Taschenrechner


def calculator():
    print("Wähle deine Rechenoperation.")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")
    print("5. Fläche berechnen")
    print("6. Meilen in Kilometer")
    print("7. Kilometer in Meilen")
    print("8. Celsius in Fahrenheit")
    print("9. Fahrenheit in Celsius")
    choice = input("Wähle Option(1/2/3/4/5/6/7/8/9): ")

    if choice in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        try:
            zahl1 = float(input("Gib deine erste Zahl ein: "))
            zahl2 = float(input("Gib deine zweite Zahl ein: "))
        except ValueError:
            print("Ungültige Eingabe, bitte gib eine Zahl ein.")
        if choice == "1":
            print(math_functions.add(zahl1, zahl2))
        elif choice == "2":
            print(math_functions.subtract(zahl1, zahl2))
        elif choice == "3" or "5":
            print(math_functions.mult(zahl1, zahl2))
        elif choice == "4":
            print(math_functions.div(zahl1, zahl2))
        elif choice == "6":
            print(math_functions.miles_to_km(km))
    else:
        print("Ungültige Eingabe")


calculator()
