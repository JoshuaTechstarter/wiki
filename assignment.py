

def durchschnittsalter(person1, person2):
    person1 = input("Gib Alter 1 an:")
    person2 = input("Gib Alter 2 an:")
    print(f"Der Datentyp von person1 ist:{type(person1)}")
    print(f"Der Datentyp von person2 ist:{type(person2)}")
    person1int = int(person1)
    person2int = int(person2)
    print(f"Die Addition der beiden strings ist: {person1 + person2}")
    print(f"Die Addition der beiden Zahlen ist: {person1int + person2int}")

durchschnittsalter(10, 20)