def promedio(lista):
    tamaño = len(lista)
    contador = 0
    for num in lista:
        contador = contador + num

    return contador/tamaño

nums = [10,20,30,40]

resultado = promedio(nums)

print(f"el promedio es {resultado}")