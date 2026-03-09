texto = "banana"
letras = {}
for i in texto:
    letras[i] = letras.get(i,0) + 1

print(letras)