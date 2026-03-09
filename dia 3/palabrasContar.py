texto = "el sol brilla y el sol calienta"
textoEnLista = texto.split()
print(textoEnLista)

diccionario = {}

for i in textoEnLista:
    if i in diccionario:
        diccionario[i] +=1
    else:
        diccionario[i] = 1
maxActual = 0
stopwords = ["el", "la", "los", "las", "de", "y"]
for clave in diccionario:
     if diccionario[clave] > maxActual and clave not in stopwords:
         maxActual = diccionario[clave]
         palabra = clave
print(f"La palabra mas repetida es: {palabra} con {maxActual}")

print(diccionario)