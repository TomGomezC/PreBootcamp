costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for i in diccionario:
        print(len(diccionario[i]), i)
        for n in diccionario[i]:
            print(n)

imprimirInformacion(costa_rica)