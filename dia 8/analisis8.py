#Hoy detectaremos errores en el merge, tenedremos que analizar y tomar decisiones con respecto a lo que tengamos
#Nos tomaremos el tiempo para analizar que tenemos y vizualizar que errores puede haber.

#Primordial ante todo
#Siempre ver si hay valores nulos por columnas
#Ver si hay informacion que no tiene relacion entre las tablas
#Visualizar los tipos de datos
#Observar la cardinalidad 
#Si al hacer un inner join, hay menos filas, observar porque se pierde informacion
#Ver que los datos sean correcto tiendo en cuenta la logica de negocio, Auriculares no van muebles 
# APLICAR OJO DE AGUILA O CREAR VECTOR PARA CADA CATEGORIA
#error_muebles = df_final[(df_final['categoria'] == 'Muebles') & 
                    #     (df_final['nombre'].str.contains('Auriculares|Mouse|Laptop', case=False))]
import pandas as pd

df_ventas = pd.read_csv("dia 8/ventas.csv")
df_productos = pd.read_csv("dia 8/producto.csv")

print(df_productos)
print()
print(df_ventas)
print()
print(df_ventas.isnull().sum())
print()
print(df_productos.isnull().sum())

#Puedo tomar dos decisiones limpiar cada tabla primero y despues hacer merge o hacer merge y limpiar la tabla
#Obtare por limpiar cada una primero 

#Primero buscare en la tabla venta cuales son los id donde aparece nulo, en este caso cantidad.
#Despues buscare cuantas veces el id aparece en la tabla.
ids_con_nulos = df_ventas[df_ventas['cantidad'].isnull()]['id_producto'].unique()
frecuencia_productos = df_ventas[df_ventas['id_producto'].isin(ids_con_nulos)]['id_producto'].value_counts()

print("IDs con cantidades nulas y su frecuencia total en el dataset:")
print(frecuencia_productos)
#Nos damos cuenta que id 107 no se ha vendido mas de una vez, ahora lo filtrare en productos para saber cual es ese producto.
producto_info = df_productos[df_productos['id_producto'] == 107]
print()
print(producto_info)
#Empty DataFrame
#Columns: [id_producto, nombre, categoria, precio]
#Index: []
#Ahi vemos que en la tabla productos ni si quiera existe el producto, entonces borremos en venta eso.
df_ventas = df_ventas[df_ventas['id_producto'] != 107] #Eliminado de ventas 107 
print(df_ventas.isnull().sum()) #Ya no hay valores nulos o nan

#Revisamos productos 
ids_con_nulos = df_productos[df_productos['precio'].isnull()]['nombre'].unique()
print(ids_con_nulos) #Obersvamos el nombre del producto que no tiene precio, lo eliminamos pero con la condicon de preguntar que pasa con ese producto.
df_productos = df_productos[df_productos['id_producto'] != 104]
print(df_productos.isnull().sum()) #Tabla limpia

#Haremos merge
df_final = pd.merge(df_ventas,df_productos, on='id_producto', how = "left")
print(df_final) #El resultado de este df sera con respecto a los id si los ai no estan en los dos no nos sirve. 
#Nos da exactamente lo que necesitamos
if df_final["precio"].isnull().any():
    print(" Hay productos sin información en el catálogo, no serán considerados en el análisis de ingresos.")
    print()
    # Eliminamos las filas con NaN para que no afecten los cálculos posteriores
    df_final = df_final.dropna(subset=["precio"])

df_final["ingreso_total"] = df_final["cantidad"] * df_final["precio"]
print(df_final)

ingresosCategoria = df_final.groupby('categoria')['ingreso_total'].sum()

ingresosProducto = df_final.groupby('nombre')['ingreso_total'].sum()

ingresosCiudad = df_final.groupby('ciudad')['ingreso_total'].sum()

print(f"¿Cual es el ingreso total por categoria?: {ingresosCategoria}")
print(f"¿Cual es el producto que más dinero genera?: {ingresosProducto.idxmax()}")
print(f"¿Cual es la ciudad con más ingresos?: {ingresosCiudad.idxmax()}")


filas_iniciales =  len(pd.read_csv("dia 8/ventas.csv")) 
filas_finales = len(df_final)
filas_eliminadas = filas_iniciales - filas_finales
porcentaje_eliminado = (filas_eliminadas / filas_iniciales) * 100

print(f"📊 Análisis de limpieza:")
print(f"- Filas originales: {filas_iniciales}")
print(f"- Filas tras limpieza y merge: {filas_finales}")
print(f"- Filas descartadas: {filas_eliminadas}")
print(f"- % de información descartada: {porcentaje_eliminado:.2f}%")

filas_iniciales =  len(pd.read_csv("dia 8/producto.csv")) 
filas_finales = len(df_final)
filas_eliminadas = filas_iniciales - filas_finales
porcentaje_eliminado = (filas_eliminadas / filas_iniciales) * 100

print(f"📊 Análisis de limpieza:")
print(f"- Filas originales: {filas_iniciales}")
print(f"- Filas tras limpieza y merge: {filas_finales}")
print(f"- Filas descartadas: {filas_eliminadas}")
print(f"- % de información descartada: {porcentaje_eliminado:.2f}%")