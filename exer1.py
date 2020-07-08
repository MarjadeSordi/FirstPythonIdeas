'''Elabore um algoritmo que calcule e escreva a soma de 5 números lidos.
ALGORITMO SOMAR
VAR
CONT, N, SOMA: INTEIRO
INÍCIO
SOMA  0
PARA CONT  1 ATÉ 5 FAÇA
INÍCIO
ESCREVER (‘INFORME UM NÚMERO A SER SOMADO: ’)
LER ( N )
SOMA  SOMA + N
FIM
FIMPARA
ESCREVER (‘A SOMA DOS NÚMEROS LIDOS É: ’, SOMA)
FIM'''
#algoritimo exerc1
soma=0
num=int(input("informe um número a ser somado: "))
for i in range (1,5):
    soma=soma + num
    print("A soma dos números lidos é",soma)
