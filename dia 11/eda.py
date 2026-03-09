import pandas as pd

df = pd.read_csv("dia 11/ventas_eda.csv")


#EDA = EXPLORATORY DATA ANALYSIS

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.describe())
print(df["ciudad"].value_counts())
print(df["precio"].quantile([0.25,0.5,0.75]))


#Tenemos un dataSet donde tiene 7 columnas y 35 filas que eso se traduce en 35 ventas.
#Observamos que los tipos de columnas estan correctos, no hay string en clumnas de numeros o al contrario.
#Tenemos dos valores nulos en la columna ciudad y en la columna producto, si no tenemos ciudad, no podemos registrar esa venta
#Vere el precio de ese producto, puede que pueda asociarlo a un producto ya existente
filaProductoNulo = df.loc[df['producto'].isnull(),'precio']
#Su precio es 45 buscare que productos tienen ese precio
producto45 = df.loc[df["precio"] == 45, 'producto']
#Observamos que es un teclado, entonces asignare ese nombre al producto que vale 45 y no tiene nombre
df.loc[(df['producto'].isnull()) & (df['precio'] == 45),'producto'] = 'Teclado'
filaCiudadNula = df.loc[df['ciudad'].isnull(),'producto']
#Al producto sin ciudad, vemos que el producto es un mouse, dos opciones o le coloco sinciudad, que no me gusta o con la moda, donde mas se venda el mouse
ciudad = df[df['producto'] == 'Mouse']['ciudad'].mode()[0]
#La ciudad que mas vende el mouse es bogota, le asignare ese valor
df.loc[(df['ciudad'].isnull()) & (df['producto'] == 'Mouse'),'ciudad'] = 'Bogota'

#La ciudad que mas registra ventas es bogota, con un indice de 13 ventas en total
#Se obeserva que el valor minimo y el valor max tienen una gran diferencia entre si 24 - 10000, por eso en las distribuciones
#Se ven valores raros, es normal por su precio
#Se podria decir que hay un valor atipico en ventas, por lo general se vende de 1 a 3 unidades pero de repente alguien compro 10 cosas de una venta
#Podriamos sacar ingresos para ver cuanto se ha ganado por producto.
df['ingreso_total'] = df['precio'] * df['cantidad']

grupoProducto = df.groupby('producto')['ingreso_total'].sum()
print(grupoProducto) 
print(df.loc[df['cantidad'] == 10, 'producto'])
#El monitor fue quien creo este valor atipico, pues en laventa 31 se vendieron 10 monitores a 910 cada uno.

print("\n" + "="*40)
print("       RESUMEN DE INSIGHTS (EDA)       ")
print("="*40)

# 1. Insight sobre Calidad de Datos e Imputación
print(f"1. LIMPIEZA: Se recuperaron filas con nulos mediante lógica de negocio.")
print(f"   - Producto 'Teclado' identificado por precio ($45).")
print(f"   - Ciudad 'Bogotá' asignada por ser la moda en ventas de Mouse.")

# 2. Insight sobre el Outlier de Ventas
venta_max = df.loc[df['cantidad'].idxmax()]
print(f"\n2. VALOR ATÍPICO DETECTADO:")
print(f"   - La venta mayorista de {venta_max['cantidad']} unidades de '{venta_max['producto']}'")
print(f"     generó un ingreso de ${venta_max['ingreso_total']:,.2f}.")
print(f"   - Esto rompe el patrón del 75% de los clientes que solo compran 3 unidades o menos.")

# 3. Insight sobre Concentración de Mercado
top_ciudad = df['ciudad'].value_counts().idxmax()
porcentaje_top = (df['ciudad'].value_counts(normalize=True).max() * 100)
print(f"\n3. DOMINIO GEOGRÁFICO:")
print(f"   - {top_ciudad} es el centro de operaciones principal,")
print(f"     concentrando el {porcentaje_top:.1f}% de las transacciones totales.")

# 4. Comparativa de Precios (Mediana vs Promedio)
print(f"\n4. ESTRUCTURA DE PRECIOS:")
print(f"   - El 50% de los productos vendidos cuestan ${df['precio'].median():.2f} o menos,")
print(f"     aunque el promedio sea de ${df['precio'].mean():.2f} debido a productos de lujo.")
print("="*40)
