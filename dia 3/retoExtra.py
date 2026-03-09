import csv

ciudades = {}
c = 0
suma_edades = 0

print("Mayores de 21:")

with open("dia 3/datosNormales.csv", newline="") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        c += 1

        edad = int(fila['edad'])
        suma_edades += edad

        ciudad = fila["ciudad"]
        ciudades[ciudad] = ciudades.get(ciudad, 0) + 1

        if edad > 21:
            print(f"{fila['nombre']} - {edad}")

#  cálculo fuera del loop
maxActual = 0
ciudad_max = ""

for ciudad, cantidad in ciudades.items():
    if cantidad > maxActual:
        maxActual = cantidad
        ciudad_max = ciudad

print("\nResumen:")
print(f"- Total personas: {c}")
print(f"- Edad promedio: {suma_edades / c}")
print(f"- Ciudad más común: {ciudad_max}")