texto = "  Hola, Python!!! Es Genial, genial...   "

t = texto.lower().split()
lista = []
diccionario ={}
print(t)
for palabra in t:
    lista.append(palabra.strip(',!...'))
    
    
for palabrita in lista:
    if palabrita in diccionario:
        diccionario[palabrita] += 1
    else:
        diccionario[palabrita] = 1

print(diccionario)