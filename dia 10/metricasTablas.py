import pandas as pd

df_producto = pd.read_csv("dia 9/producto.csv")

df_venta = pd.read_csv("dia 9/venta.csv")
print(df_producto)
print(df_venta)
df_venta['existe_en_catalogo'] = df_venta['id_producto'].isin(df_producto['id_producto'])
#Verificamos valores nulos en las tablas
print(df_producto.isnull().sum())
print()
print(df_venta.isnull().sum())
print()
#No hay valores nulos, haremos merge.
df_final = pd.merge(df_venta,df_producto, on = 'id_producto', how = "left" )
df_final['ingreso_total'] = df_final['cantidad'] * df_final['precio']
print(df_final)

ciudades = df_final.groupby('ciudad').agg({'ingreso_total': 'sum', 'cantidad': 'sum', 'ciudad':'count'})
ciudades['ticket_promedio'] = ciudades['ingreso_total'] / df_final.groupby('ciudad').size()

categoria = df_final.groupby('categoria').agg({'ingreso_total' : 'sum', 'cantidad':'sum', 'categoria' : 'count'})
categoria['ticket_promedio'] = categoria['ingreso_total'] / df_final.groupby('categoria').size()

producto = df_final.groupby('nombre').agg({'ingreso_total': 'sum', 'cantidad' : 'sum', 'nombre' : 'count'})
producto['ticket_promedio'] = producto['ingreso_total'] / df_final.groupby('nombre').size()

# --- REPORTE DE INSIGHTS ---

print("=== DESEMPEÑO POR CIUDAD ===")
# Ordenado por ingresos para ver quién aporta más capital
print(ciudades.sort_values(by='ingreso_total', ascending=False).round(2))
print(f"\nCiudad con mayor ticket promedio: {ciudades['ticket_promedio'].idxmax()}")
print("-" * 30)

print("\n=== ANÁLISIS POR CATEGORÍA ===")
# Ordenado por cantidad para ver qué categoría tiene más rotación
print(categoria.sort_values(by='cantidad', ascending=False))
print(f"\nCategoría líder en ingresos: {categoria['ingreso_total'].idxmax()}")
print("-" * 30)

print("\n=== TOP PRODUCTOS (RENTABILIDAD) ===")
# Ordenado por ticket_promedio para ver el valor percibido de cada producto
print(producto.sort_values(by='ticket_promedio', ascending=False).round(2))
print("-" * 30)

# Resumen Ejecutivo rápido
total_ventas = df_final['ingreso_total'].sum()
print(f"\nRESUMEN GLOBAL:")
print(f"Ingresos Totales: ${total_ventas:,.2f}")
print(f"Producto más vendido (unidades): {df_final.groupby('nombre')['cantidad'].sum().idxmax()}")
