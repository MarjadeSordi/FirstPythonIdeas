'''2. Faça um algoritmo que leia 5 números e some os que forem pares.
Ao final, deve-se escrever
o resultado da soma.
ALGORITMO SOMAR
VAR
X, N, SOMA: INTEIRO
INÍCIO
SOMA  0
PARA X  1 ATÉ 5 FAÇA
INÍCIO
ESCREVER (‘INFORME UM NÚMERO A SER SOMADO: ’)'''
#algoritomoexer2
soma=0
for x in range (1,5):
    num=int(input("Infome um número a ser somado: "))
    if num%2==0:
        soma=soma+num
print(soma)
        
    
    
