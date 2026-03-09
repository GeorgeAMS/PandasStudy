texto = "Hola!!! hola?? HOLA..."


hola= texto.lower().split()
lista = []
diccionario = {}
for i in hola:
    lista.append(i.strip('?!.'))
for palabrita in lista:
    if palabrita in diccionario:
        diccionario[palabrita] += 1
    else:
        diccionario[palabrita] = 1

print(diccionario)