class Auto:
    def __init__(self, name, motor, reichweite, kilometer):
        self.name = name
        self.motor = motor
        self.restreichweite = float(reichweite)
        self.kilometerzahl = float(kilometer)

    def fahren(self, km):
        if self.restreichweite >= km:
            self.kilometerzahl += km
            self.restreichweite -= km
        else:
            print("Reichweite nicht mehr ausreichend!")

    def tanken(self, km):
        self.restreichweite += km
