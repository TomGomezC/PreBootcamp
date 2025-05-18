matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

#Actualizar valores en diccionarios y listas

#print(matriz)
matriz[1][0]=6
#print(matriz)

cantantes[0]["nombre"]="Enrique Martin Morales"
#print(cantantes)

ciudades["México"][2]="Monterrey"
#print(ciudades)

coordenadas[0]["latitud"]=9.9355431
print(coordenadas)