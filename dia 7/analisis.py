#Ventas.csv
# - id_pruducto - ciudad - cantidad
# - id_pruducto - nombre - categoria - precio

#Aqui buscamos practicar el analisis de dos tablas diferentes, responder ¿Como podemos trabajar con ellas?
#¿Que tienen en común? 
# ------------------------ Responder las siguientes preguntas -------------------
#¿Cual es el ingreso total por categoria?
#¿Cual es el producto que más dinero genera?
#¿Cual es la ciudad con más ingresos?

#Vizualicamos Dataframes 

import pandas as pd


df_ventas = pd.read_csv("dia 7/ventas.csv")
df_productos = pd.read_csv("dia 7/producto.csv")

print(df_productos)
print()
print(df_ventas)
print()
#Observamos que podemos unir con merge, podemos guardas los productos que no tienen venta con cantidad de venta en 0, en este caso todos los producto se venden.
#O si queremos podemos olvidar los productos que no se vendieron con inner.

df_final = pd.merge(df_ventas,df_productos, on='id_producto', how = "left") #Recomendable ver con left pq asi vemos mas inconsistencias
print("Df final")
print()
if df_final["precio"].isnull().any():
    print(" Hay productos sin información en el catálogo, no serán considerados en el análisis de ingresos.")
    print()
    # Eliminamos las filas con NaN para que no afecten los cálculos posteriores
    df_final = df_final.dropna(subset=["precio"])

df_final["ingreso_total"] = df_final["cantidad"] * df_final["precio"]
print(df_final)

ingresosCategoria = df_final.groupby('categoria')['ingreso_total'].sum()
#Aqui podemos asimilar que aunque el mouse inalambrico se venda mucho, el precio del producto es quien ayuda a tener mas ganancias.
ingresosProducto = df_final.groupby('nombre')['ingreso_total'].sum()
#Si la pregunta fuera, ¿Que ciudad vende mas productos seria ciudad y cantidad, pero como hablamos de ingresos, entonces es con cash
ingresosCiudad = df_final.groupby('ciudad')['ingreso_total'].sum()

print(f"¿Cual es el ingreso total por categoria?: {ingresosCategoria}")
print(f"¿Cual es el producto que más dinero genera?: {ingresosProducto.idxmax()}")
print(f"¿Cual es la ciudad con más ingresos?: {ingresosCiudad.idxmax()}")


#Recuerda no solo es pensar, es validar, ver que falta, tomar decisiones.