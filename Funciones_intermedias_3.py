cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario2(n,cantantes):
    for i in cantantes:
        print(i[n])

iterarDiccionario2("nombre",cantantes)
iterarDiccionario2("pais",cantantes)