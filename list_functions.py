# Erstelle ein Python-Skript, das eine Liste von Zahlen als Eingabe erhält und: #
# 1. die Summe aller Zahlen berechnet#
# 2. Nur die ungeraden Zahlen ausgibt#
# 3. Die größte Zahl der Liste findet#


zahlenliste = [22, 3, 5, 19, 4, 20, 8, 14]
summe = sum(zahlenliste)
biggest = max(zahlenliste)
print(f"Die Summe aller Zahlen ist", summe)


def ungerade_zahlen(zahlenliste):
    uneven = []
    for num in zahlenliste:
        if num % 2 != 0:

            uneven.append(num)
    return uneven


print(ungerade_zahlen(zahlenliste))


print(f"Die größte Zahl ist", biggest)

largest = 0

for i in zahlenliste:
    if i > largest:
        largest = i

print(largest)
