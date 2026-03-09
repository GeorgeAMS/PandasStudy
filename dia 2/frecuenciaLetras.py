texto = "banana"
palabra ={}

for letra in texto:
    if letra in palabra:
        palabra[letra] += 1
    
    else:
        palabra[letra] = 1
for i in palabra:
    print(i,palabra[i])

print(palabra)