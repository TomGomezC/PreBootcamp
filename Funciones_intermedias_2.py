
def iterarDiccionario(cantantes):
    for n in cantantes:
        print("nombre - " ,n["nombre"], "," , "pais - ",n["pais"])

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)