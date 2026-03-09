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
totalUnidades = df_final["cantidad"].sum()
totalGanado = df_final['ingreso_total'].sum()
ticketpromedio = totalGanado/len(df_final)
ingresoPorciudad = df_final.groupby('ciudad')['ingreso_total'].sum()
ventasPorciudad = df_final.groupby('ciudad')['cantidad'].sum()
dineropromedioporcompra  = ingresoPorciudad/ventasPorciudad
productoMasVendido = df_final.groupby('nombre')['cantidad'].sum().idxmax()
productoMasRentable = df_final.groupby('nombre')['ingreso_total'].sum().idxmax()
ingreso_por_categoria = df_final.groupby('categoria')['ingreso_total'].sum()
porcentaje_categoria = (ingreso_por_categoria / totalGanado) * 100

print("-" * 50)
print("ANÁLISIS ESTRATÉGICO DE VENTAS")
print("-" * 50)

print(f"1. DESEMPEÑO GLOBAL:")
print(f"   - Ingreso Total: ${totalGanado:,.2f}")
print(f"   - Unidades Vendidas: {totalUnidades}")
print(f"   - Valor ticket promedio: ${ticketpromedio:,.2f}")
print(f"   > INSIGHT: Dinero promedio por compra (transacción).")
print()

print(f"2. RENDIMIENTO POR CIUDAD :")
print(dineropromedioporcompra.sort_values(ascending=False))
print(f"   > INSIGHT: La ciudad de '{dineropromedioporcompra.idxmax()}' genera el mayor valor por unidad vendida.")
print()

print(f"3. ANÁLISIS DE PRODUCTOS:")
print(f"   - El más vendido (Volumen): {productoMasVendido}")
print(f"   - El más rentable (Dinero): {productoMasRentable}")
print(f"   > INSIGHT: Si el producto más vendido no es el más rentable, hay una oportunidad de up-selling.")
print()

print(f"4. CONCENTRACIÓN POR CATEGORÍA (% del Ingreso Total):")
print(porcentaje_categoria.map("{:.2f}%".format))
categoria_top = porcentaje_categoria.idxmax()
print(f"   > INSIGHT: El negocio depende fuertemente de la categoría '{categoria_top}', con un {porcentaje_categoria.max():.2f}% de participación.")
print()


#Un ticket es lo que deja el cliente cuando compra, es decir entre mas compre o compre productos de valor, el ticket promedio 
#Sera alto, si las ventas bajan o si ya no se esta comprando tanto un producto, baja el ticket.

#Up-selling: Oportunidad de vender un producto con mayor calidad o venta 
#mas cara, moderna o completa del producto o servicio que inicialmente pensaba comprar