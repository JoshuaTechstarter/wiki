meals = []


for _ in range(3):
    meal = input("Gib ein Gericht ein: ")
    meals.append(meal)

print(meals)

for x in meals:
    print(f"Dein genanntes Gericht ist: {x}")


weekdays = ["Montag", "Dienstag", "Mittwoch"]
food = []
for w in weekdays:
    for _ in range(2):
        food_input = input(f"Was möchtest du am {w} essen?")
        food.append(food_input)
print(f"Der Essensplan für die gesamte Woche sieht wie folgt aus: {food}")
