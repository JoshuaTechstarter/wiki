student = {"name": "Lisa", "alter": 20, "kurs": "Informatik"}

for key, value in student.items():
    print(f"{key}: {value}")

print(student["name"])

student["stadt"] = "Berlin"
print(student)
