'''
Trabalho de Lógica - Primeira entrega.
Faça um algoritmo que leia um código e leia três valores. Os códigos válidos são 1,
2, 3, 4 e 5; se o código for diferente desses, apresentar a mensagem "CÓDIGO
INVÁLIDO" e terminar o algoritmo. Se:
 código = 1: multiplicar os três valores;
 código = 2: somar os três valores;
 código = 3: subtrair os três valores;
 código = 4: somar o cubo dos 3 valores;
 código = 5: somar o quadrado dos 3 valores.'''
Pro=print("Digite três números e atribua um código de 1 a 5 para realizar uma operação matemática")
num1=float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número:  "))
num3=float(input("Digite o terceiro número:  "))
cod=int(input("Digite um código de 1 a 5:  "))
if cod ==1:
    print("O valor dos 03 números multiplicados é:",(num1*num2*num3))
elif cod ==2:
    print("A soma dos 03 valores é:",(num1+num2+num3))
elif cod ==3:
    print("A subtração dos 03 números é:",(num1-num2-num3))
elif cod ==4:
    print ("A soma dos 03 valores elevados ao cubo é:",(num1**3+num2**3+num3**3))
elif cod ==5:
    print ("A soma dos 03 valores elevados ao quadrado é:",(num1**2+num2**2+num3**2))
else:
    print ("CÓDIGO INVALIDO")
    
