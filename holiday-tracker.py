# Hausaufgabe 2024.12.13 Ferientracker



date = input("Enter a date to determine if its holiday or not (YYYY.MM.DD):")

is_winter = date >= "2024.12.24" and date <= "2025.01.01"
is_spring = date >= "2025.04.18" and date <= "2025.04.21" 
is_summer = date >= "2025.08.11" and date <= "2025.08.19"
is_winter2 = date >= "2025.12.24" and date <= "2025.01.01"
feiertag = date == "2024.10.03" + "2024.10.31" + "2024.12.25" + "2024.12.26" + "2025.01.01" + "2025.04.18" + "2025.04.21" + "2025.05.01" + "2025.05.29" + "2025.06.09" + "2025.10.03" + "2025.10.31" + "2025.12.25" + "2025.12.26" + "2026.01.01"


         
if is_winter:
    print("Es sind Winterferien 2024.")
elif is_spring:
    print("Es sind Osterferien.")
elif is_summer:
    print("Es sind Sommerferien.")
elif is_winter2:
    print("Es sind Winterferien 2025.")
elif feiertag:
    print("Es ist Feiertag.")
else :
    print("Es sind keine Ferien oder Feiertag.")

