texto = "ingenieria de datos"
textoNormalizado = texto.lower()
contador = 0
for letra in textoNormalizado:
    if letra in 'aeiou':
        contador = contador + 1

print(f"en la cadena de texto hay {contador} vocales")


