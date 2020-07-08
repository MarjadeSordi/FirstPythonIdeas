numeros = []
par = 0
impar = 0
for x in range(0,6):
    num = int (input ("Digite um número: "))
    numeros.append(num)
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print ("Quantidade de pares: ",par)
print ("Quantidade de ímpares: ",impar)
for nums in numeros:
    print (nums)

'''
E se quisesse separar os pares e os ímpares?
'''
