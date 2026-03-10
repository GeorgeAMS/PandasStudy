#Las tablas dinamicas nos ayudan a responder preguntas como:
#¿Que ciudad genera mas ingreso por producto?
#¿Cual es el ticket promedio por ciudad?
#¿Que categoria vende mas en cada ciudad?

#filas: ciudades
#columnas: productos
#valor: ingresos
#operación: suma

import pandas as pd

df = pd.read_csv("dia 11/ventas_eda.csv")

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

df['ingreso_total'] = df['precio'] * df['cantidad']

print(df)

tabla_ingresos = df.pivot_table(
    index='ciudad',         # Las filas
    columns='producto',      # Las columnas
    values='ingreso_total',  # Los datos a calcular
    aggfunc='sum'           # La operación (suma)
)

tabla_ingresos = tabla_ingresos.fillna(0)

print(tabla_ingresos)

tabla_cantidad = df.pivot_table(
    index='ciudad',         # Las filas
    columns='producto',      # Las columnas
    values='cantidad',  # Los datos a calcular
    aggfunc='sum'           # La operación (suma)
)
tabla_cantidad = tabla_cantidad.fillna(0)
print(tabla_cantidad)

# 1. Calculamos los totales por producto
totales_producto = tabla_cantidad.sum().sort_values(ascending=False)

# 2. Identificamos al líder y al menos vendido
top_producto = totales_producto.index[0]
top_valor = totales_producto.iloc[0]

print("--- INSIGHTS DE ROTACIÓN ---")
print(f"1. Líder de ventas: El {top_producto} es el que más rota con {top_valor} unidades.")
print(f"2. Menor rotación: La {totales_producto.index[-1]} con {totales_producto.iloc[-1]} unidades.")
print(f"3. Diversidad: Bogotá es la ciudad con mayor variedad de productos vendidos.")
print(f"4. Especialización: Cali concentra el 100% de la rotación de Teclados.")



# Ticket promedio general de la ciudad
ticket_ciudad = df.pivot_table(index='ciudad', values='ingreso_total', aggfunc='mean')
# Suponiendo que tu pivot se llama ticket_ciudad
print("--- RANKING DE RENTABILIDAD POR CIUDAD ---")
ranking = ticket_ciudad.sort_values(by='ingreso_total', ascending=False)

for ciudad, valor in ranking['ingreso_total'].items():
    print(f"En {ciudad:12} cada venta deja en promedio: ${valor:,.2f}")

# 1. Cálculo de totales
total_ingresos = tabla_ingresos.sum().sum()
ingresos_producto = tabla_ingresos.sum().sort_values(ascending=False)
top_producto = ingresos_producto.index[0]
participacion_top = (ingresos_producto.iloc[0] / total_ingresos) * 100

print(f"--- INSIGHTS DE RENTABILIDAD ---")
print(f"1. EL REY DE LA CAJA: La {top_producto} genera ${ingresos_producto.iloc[0]:,.2f}.")
print(f"   Representa el {participacion_top:.1f}% de todo el dinero de la empresa.")

print(f"\n2. EFICIENCIA VS VOLUMEN:")
print(f"   Aunque el Mouse rota mucho, solo genera ${ingresos_producto['Mouse']:,.2f}.")
print(f"   ¡Necesitas vender {(ingresos_producto.iloc[0] / ingresos_producto['Mouse']):.0f} Mouses para igualar una sola Laptop!")

print(f"\n3. FOCO GEOGRÁFICO:")
# Buscamos la ciudad con el ingreso más alto
ciudad_top = tabla_ingresos.sum(axis=1).idxmax()
print(f"   {ciudad_top} es tu mercado premium con el ingreso más alto acumulado.")

print(f"\n4. ALERTA ESTRATÉGICA:")
print(f"   Cali tiene alta rotación de Teclados, pero su aporte financiero es marginal (${ingresos_producto['Teclado']:,.2f}).")
