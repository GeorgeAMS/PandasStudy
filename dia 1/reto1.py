nums = [10, 20, 30, 40, 50]

def numeroMayor(lista):
    mayor = lista[0]

    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

def numeroMenor(lista):
    menor = lista[0]

    for num in lista:
        if num < menor:
            menor = num
    return menor

def promedio(lista):
    tamaño = len(lista)
    contador = 0
    for num in lista:
        contador = contador + num

    return contador/tamaño

mayor = numeroMayor(nums)
menor = numeroMenor(nums)
prom = promedio(nums)

print(f"Numero mayor: {mayor}")
print(f"Numero menor: {menor}")
print(f"Numero promedio: {prom}")