nums = [1,1,2,3,3,3,4,4,5]
conteo = {}

for num in nums:
    
    if num in conteo:
        conteo[num] +=1
    else:
        conteo[num] = 1


for num in conteo:
    print(f"{num} hay {conteo[num]}")