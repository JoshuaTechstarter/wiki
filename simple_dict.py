ger_en = {
    "eins": "one",
    "zwei": "two",
    "drei": "three",
    "katze": "cat",
    "haus": "house",
    "kindergarten": "kindergarten",
    "telefon": "telephone",
    "kamera": "camera",
    "bildschirmschoner": "screensaver",
    "rückwärts": "backwards",
}


def expand():
    while True:
        new_word = input(
            "Gib ein deutsches Wort ein, das du hinzufügen möchtest (oder 'exit' zum Beenden): "
        ).lower()
        if new_word == "exit":
            break
        if new_word in ger_en:
            print(f"Das Wort '{new_word}' ist bereits im Wörterbuch enthalten.")
        else:
            translation = input(
                f"Gib die englische Übersetzung für '{new_word}' ein: "
            ).lower()
            ger_en[new_word] = translation
            print(
                f"Das Wort '{new_word}' mit der Übersetzung '{translation}' wurde hinzugefügt."
            )


expand()
word = input("Welches deutsche Wort möchtest du übersetzen? ").strip().lower()

if word in ger_en:
    print(f"Die englische Übersetzung von '{word}' ist '{ger_en[word]}'.")
else:
    print(f"Das Wort '{word}' ist nicht im Wörterbuch enthalten.")
