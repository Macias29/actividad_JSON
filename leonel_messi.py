import json

# Crear objeto JSON a partir de un diccionario de Python
jugador2 = {"nombres": "Leonel", "apellidos": "Messi",
"fecha_nacimiento": "24-06-1987", "edad": 35, "pais_nacimiento": "Argentina", "ciudad": "Rosario",
"posición": "Delantero", "grupo_sanguíneo": "O+", "nacionalidad": "Argentina"}

# Guardar objeto JSON en un archivo
with open("leonel_messi.json", "w") as file:
    json.dump(jugador2, file)

# Cargar objeto JSON desde un archivo
with open("leonel_messi.json", "r") as file:
    jugador2 = json.load(file)

# Acceder a los valores
print("Nombres:", jugador2["nombres"])
print("Apellidos:", jugador2["apellidos"])
print("Fecha de nacimiento:", jugador2["fecha_nacimiento"])
print("Edad:", jugador2["edad"])
print("País de nacimiento:", jugador2["pais_nacimiento"])
print("Ciudad:", jugador2["ciudad"])
print("Posición:", jugador2["posición"])
print("Grupo sanguíneo:", jugador2["grupo_sanguíneo"])
print("Nacionalidad:", jugador2["nacionalidad"])




