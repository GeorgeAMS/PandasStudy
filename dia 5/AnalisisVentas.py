import pandas as pd

df = pd.read_csv("dia 5/ventas.csv")
df['ingreso_total'] = df['precio'] * df['cantidad']

print(df) 
print('------------------------------------------------')
print(f"La suma de todos los ingresos por ciudad es: {df['ingreso_total'].sum()}")
print('------------------------------------------------')
ventas_totales = df.groupby('producto')['cantidad'].sum() #Agrupamos estas dos columnas y la sumamos
print(f"El producto mas vendido en todas las ciudades es: {ventas_totales.idxmax()}")
print('------------------------------------------------')
ingresos_totales = df.groupby('ciudad')['ingreso_total'].sum()
print(f"La ciudad con mas ingresos es: {ingresos_totales.idxmax()}")
print('------------------------------------------------')
categoriaPorVenta = df.groupby('categoria')['ingreso_total'].sum()
print("Ventas por categoria: ")
for categoria, valor in categoriaPorVenta.items():
    print(f"{categoria} - {valor}")
print('------------------------------------------------')
print("Valores de productos vendidos ordenado")
topProductos = df.groupby('producto')['ingreso_total'].sum()
print(f"{topProductos.sort_values(ascending=False)}")
print('------------------------------------------------')
print(f"Categoria que domina el monopolio: {categoriaPorVenta.idxmax()}")
print(f"Producto que genera mas dinero: {topProductos.idxmax()}")