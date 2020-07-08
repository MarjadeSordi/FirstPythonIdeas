'''Faça um algoritmo que leia um número N,
e realize a soma dos números de 1 a N. Ao final,
deve-se escrever o resultado da soma.
ALGORITMO SOMAR
VAR
Y, N, SOMA: INTEIRO
INÍCIO
SOMA  0
ESCREVER (‘INFORME UM NÚMERO INTEIRO: ’)
LER ( N )
PARA Y  1 ATÉ N FAÇA
SOMA  SOMA + Y
FIMPARA
ESCREVER (‘A SOMA DOS NÚMEROS DE 1 ATÉ ’, N, ‘ É: ’, SOMA)
FIM'''
#algoritimo N
soma=0
n=int(input("Informe um número inteiro:  "))
for y in range (1,n):
    soma=soma+y
print("A soma dos números de 1 até",n,"é:",soma)
