# Hausaufgabe 2024.12.13 Ferientracker
import datetime

date = datetime.date.today()
print(date.strftime("Heute ist der %d.,%Y"))
is_winter = date >= datetime.datetime(2024, 12, 24) and date <= datetime.datetime(
    2025, 1, 1
)
is_spring = date >= datetime.datetime(2025, 4, 18) and date <= datetime.datetime(
    2025, 4, 21
)
is_summer = date >= datetime.datetime(2025, 8, 11) and date <= datetime.datetime(
    2025, 8, 19
)
is_winter2 = date >= datetime.datetime(2025, 12, 24) and date <= datetime.datetime(
    2025, 1, 1
)
feiertag = [
    datetime.datetime(
        (2024, 10, 3),
        (2024, 10, 31),
        (2024, 12, 25),
        (2024, 12, 26),
        (2025, 1, 1),
        (2025, 4, 18),
        (2025, 4, 21),
        (2025, 5, 1),
        (2025, 5, 29),
        (2025, 6, 9),
        (2025, 10, 3),
        (2025, 10, 31),
        (2025, 12, 25),
        (2025, 12, 26),
        (2026, 1, 1),
    )
]

if is_winter:
    print("Es sind Winterferien 2024.")
elif is_spring:
    print("Es sind Osterferien.")
elif is_summer:
    print("Es sind Sommerferien.")
elif is_winter2:
    print("Es sind Winterferien 2025.")
elif date in feiertag:
    print("Es ist ein Feiertag.")
else:
    print("Es sind keine Ferien oder Feiertag.")
