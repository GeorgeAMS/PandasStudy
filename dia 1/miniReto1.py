conteo = {1:2, 2:1, 3:3, 4:1}

for num, cantidad in conteo.items():
    if cantidad == 1:
        print(f"Aparece una vez {num}, {cantidad}")