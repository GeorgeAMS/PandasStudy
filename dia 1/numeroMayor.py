nums = [1,2,3,4,5,6,7,8,9,10]

mayor = nums[0]

for num in nums:
    if num > mayor:
        mayor = num


print(f"El numero mayor es: {mayor}")