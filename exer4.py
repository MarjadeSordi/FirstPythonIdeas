'''Faça um algoritmo que faça o somatório
dos números ímpares situados na faixa de valores
de 4 a 0.
ALGORITMO SOMAR
VAR
X, SOMA: INTEIRO
INÍCIO
SOMA  0
PARA X  4 ATÉ 0 PASSO -1 FAÇA
SE ( X MOD 2 <> 0 ) ENTÃO
SOMA  SOMA + X
FIMSE
FIMPARA
ESCREVER (‘A SOMA DOS NÚMEROS ÍMPARES SITUADOS ENTRE 4 E 0 É: ’,
SOMA)
FIM'''
#algaritmo soma dos números impares
soma=0
for x in range (-1,4):
    if (x%2!=0):
        soma=soma+x
print("A soma dos números impares situados entre 4 e 0 é",soma)
