import pandas as pd

df = pd.read_csv("dia 3/datosNormales.csv")
print(df)
print(df.head())   # primeras filas
print(df.info())   # tipos de datos
print(df.describe())  # estadísticas
print(df["nombre"]) #columna nombre
print(df["edad"]) #columna Edad
mayores = df[df["edad"] > 21]
print(mayores) 
print(df["edad"].mean())
print(df["ciudad"].value_counts())
print(df["ciudad"].value_counts().idxmax())

print(f"Total de personas: {len(df)}")
print(f"Edad promedio: {df["edad"].mean()}")
print(f"Ciudad mas comun: {df["ciudad"].value_counts().idxmax()}")
mayores = df[df["edad"] > 21]
print(f"Mayores de 21")
for fila in mayores.itertuples():
    print(f"{fila.nombre} - {fila.edad}")
ordenado = df.sort_values(by="edad", ascending=False)
print(ordenado)