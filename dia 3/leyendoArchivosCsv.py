import csv
ciudades = {}
with open("dia 3/datosNormales.csv", newline="") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        if fila["ciudad"] in ciudades:
            ciudades[fila["ciudad"]] += 1
        else:
            ciudades[fila["ciudad"]] = 1
#ciudades[ciudad] = ciudades.get(ciudad, 0) + 1

maxActual = 0
print(ciudades)
for i, gente in ciudades.items():
    if gente > maxActual:
        maxActual = gente
        ciudad = i
        
print(f"La ciudad con más personas es: {ciudad}")
    

with open("dia 3/datosNormales.csv", newline="") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila['nombre'])

#Parseo para poder comparar con numeros
with open("dia 3/datosNormales.csv", newline="") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        edad = int(fila['edad'])
        if edad > 21:
            print(f"{fila["nombre"]} - {edad}")
contador = 0
edad = 0
with open("dia 3/datosNormales.csv", newline="") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        contador +=1
        edad += int(fila['edad'])
    
    print(f"Edad promedio: {edad/contador}")