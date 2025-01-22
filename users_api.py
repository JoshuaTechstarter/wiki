from flask import Flask, request

app = Flask(__name__)

users = [
    {
        "id": 1,
        "usename": "maexchen",
        "password": "letsGo",
        "firstName": "Max",
        "familyName": "Mustermann",
    },
    {
        "id": 2,
        "usename": "annachen",
        "password": "letsGo1",
        "firstName": "Anna",
        "familyName": "Muster",
    },
    {
        "id": 3,
        "usename": "bobby",
        "password": "letsGo2",
        "firstName": "Bob",
        "familyName": "M.",
    },
]


@app.route("/users", methods=["GET"])
def home():
    return "Welcome to our users api"


# route 1
@app.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    for user in users:
        if user["id"] == id:
            return f"ID: {user['id']}, name: {user['name']}, email: {user['email']}"
    return "User not found", 404


# route 2
# 1. Postman installieren
# 2. url eingeben, POST Befehl aushwählen --> siehe Screenshot
# 3. Ausführen und veschiedene Parameter im  body angeben
# 4. Zusatz: Versuchen den richtigen Benutzer zu bekommen
# 5. Zusatz Zusatz: Versucht eine weitere post anfrage mit signup zu erstellen,
# welche Route einen neuen Nutzer in die Liste einfügt
@app.route("/users/login", methods=["POST"])
def login():
    credentials = request.get_json()
    username = credentials["username"]
    password = credentials["password"]
    if username in users and users["username"] == password:
        return f"Hallo {username}, Login erfolgreich!"
    else:
        return "Ungültige Anmeldedaten"


# @app.route("/users/signup", methods=["POST"])
# def signup():
#     credentials = request.get_json()
#     username = credentials["username"]
#     password = credentials["password"]
#     if username in users:
#         return f"Benutzername {username} ist bereits vergeben."
#     users[username] = password
#     return f"Benutzer {username} wurde erfolgreich registriert!"


# route 3
@app.route("/search", methods=["GET"])
def search():
    name = request.args.get("name")
    if not name:
        return "Error: 'name' query parameter is required.", 400

    for user in users:
        if user["name"].lower() == name.lower():
            return f"Found user: {user['name']}"
    return f"No user found with name: {name}", 404


if __name__ == "__main__":
    app.run(port=6060)
