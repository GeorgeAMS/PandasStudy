import pandas as pd 
df = pd.read_csv("dia 6/ventasSucio.csv")

print(df)
#Identificamos que tenemos una fila en donde no sabemos la cantidad de mouse vendidos en bogota
#Identificamos que no sabemos el precio de la mesa, no podemos guiarnos de un precio de mesa similar, no sabemos.
#Quiero identficar si hay filas similares, podria simular datos teniendo en cuenta similitudes.
print(df[(df["producto"] == "Mouse") & (df["ciudad"] == "Bogota")])
#Vemos que en bogota se ha vendido 2 veces mouse, una no sabemos la cantidad, otra se vendieron 5, si no se la cantidad, pensaria que lo mejor es borrar esa fila que no me da informacion.
print(df.duplicated())
#Con esto verifico que no haya mas valores repetidos, considero que la fila que tiene cantidad en nulos es mejor borrarla
df_ordenado = df.sort_values("cantidad")
print(df_ordenado)
df_sinDuplicado = df_ordenado.drop_duplicates(subset=["producto","categoria","precio"])
print(df_sinDuplicado)
#Ahora vemos que no tenemos el precio de la mesa, y solo se ha vendido en cali, podria buscar el precio en el mercado y asignarlo, pero eso podria dañar o crear valores atipicos.
#Creo que como no se vende mesa en ninguna parte podemos asignarle un valor despreciable o "normal"
df_sinDuplicado.loc[(df_sinDuplicado["producto"] == "Mesa") & (df_sinDuplicado["precio"].isna()), "precio"] = 500
print(df_sinDuplicado)
#Ahora vemos que en venta de un celular no tenemos la ciudad y es el unico lugar domde se ha vendido, yo siento que lo mejor es eliminar.
dfLimpio = df_sinDuplicado.dropna(subset=["ciudad"]).reset_index(drop=True)
print(dfLimpio)
dfLimpio["ingreso_total"] = dfLimpio["precio"] * dfLimpio["cantidad"]
print(dfLimpio)
### comenzamos analisis 
ventas_totales = dfLimpio.groupby('producto')['cantidad'].sum()
ingresos_totales = dfLimpio.groupby('ciudad')['ingreso_total'].sum()
categoriaPorVenta = dfLimpio.groupby('categoria')['ingreso_total'].sum()
topProductos = dfLimpio.groupby('producto')['ingreso_total'].sum()

print("RESUMEN")
print("")

# ingreso total
print("Ingreso total:", ingresos_totales.sum())

# producto más vendido
print("Producto más vendido:", ventas_totales.idxmax())

# ciudad con más ingresos
print("Ciudad con más ingresos:", ingresos_totales.idxmax())

# ventas por categoría
print("\nVentas por categoría:")
print(categoriaPorVenta)

# top productos
print("\nTop productos:")
print(topProductos.sort_values(ascending=False).head(3))