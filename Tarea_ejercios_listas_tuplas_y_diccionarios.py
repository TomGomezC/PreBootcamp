ventas = [
    {"fecha": "2025-05-01", "producto": "polera", "cantidad": 3, "precio": 10000},
    {"fecha": "2025-05-01", "producto": "short", "cantidad": 2, "precio": 15000},
    {"fecha": "2025-05-02", "producto": "balon", "cantidad": 5, "precio": 25000},
    {"fecha": "2025-05-03", "producto": "zapato", "cantidad": 1, "precio": 40000},
    {"fecha": "2025-05-03", "producto": "zapato", "cantidad": 1, "precio": 40000},
    {"fecha": "2025-05-04", "producto": "short", "cantidad": 5, "precio": 15000},
    {"fecha": "2025-05-08", "producto": "balon", "cantidad": 1, "precio": 25000},
    {"fecha": "2025-05-09", "producto": "polera", "cantidad": 15, "precio": 10000}
]

#2. Cálculo de Ingresos Totales

total_ventas=0
for i in ventas:
    #print(i["precio"]*i["cantidad"])
    total_ventas+=i["precio"]*i["cantidad"]

print("La venta total es ", total_ventas)

#3. Análisis del Producto Más Vendido

ventas_por_producto={
    "polera":0,
    "short":0,
    "zapato":0,
    "balon":0
}

for i in ventas_por_producto:
    for j in ventas:
        if i == j["producto"]:
            #print(i)
            ventas_por_producto[i]+=j["cantidad"]*j["precio"]

max_venta = max(ventas_por_producto.values())

keys = [key for key, val in ventas_por_producto.items() if val == max_venta]
print("El producto mas vendido fue ",keys, " con ", max_venta)

#4. Promedio de Precio por Producto

precios_por_producto={
    "polera":(180000,18),
    "short":(105000,7),
    "zapato":(80000,2),
    "balon":(150000,6)
}

for producto in precios_por_producto:
    print("El precio por ", producto, " es ", precios_por_producto[producto][0]/precios_por_producto[producto][1])

#5. Ventas por Día

ingresos_por_dia={}

for venta in ventas:
    for venta in ventas:
        ingresos_por_dia[venta["fecha"]] = venta["precio"]

print(ingresos_por_dia)

#6. Representación de Datos

resumen_ventas={
    "polera":{"cantidad_total":0,"ingresos_totales":0,"precio_promedio":0},
    "short":{"cantidad_total":0,"ingresos_totales":0,"precio_promedio":0},
    "zapato":{"cantidad_total":0,"ingresos_totales":0,"precio_promedio":0},
    "balon":{"cantidad_total":0,"ingresos_totales":0,"precio_promedio":0},
}

for i in resumen_ventas:
    for j in ventas:
        if i==j["producto"]:
            resumen_ventas[i]["cantidad_total"]+=j["cantidad"]
            resumen_ventas[i]["ingresos_totales"]+=j["cantidad"]*j["precio"]
    resumen_ventas[i]["precio_promedio"]=resumen_ventas[i]["ingresos_totales"]/resumen_ventas[i]["cantidad_total"]

print(resumen_ventas)