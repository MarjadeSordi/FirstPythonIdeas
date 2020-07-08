'''Faça um algoritmo que calcule o valor da compra de um cliente em
uma loja de peças.
O algoritmo deve ler o código e a
quantidade comprada de cada peça, sendo que a leitura é
encerrada quando o usuário informar 0 (zero)
para o código da peça. O algoritmo deve
informar o valor total da compra.
O cálculo dos valores é feito com base na tabela a seguir:
001 Parafuso R$ 0,50
002 Bucha R$ 1,00
003 Prego R$ 0,70
004 Chave Fenda R$ 5,00
005 Alicate R$ 8,00
'''
total=0
qua=0
cod= str("1")
while cod!= str ("0"):
    cod=str(input("Digite o códido do produto"))
    if cod=="001":
        qua=int(input("Digite a quantidade de mercadorias"))
        total=0.50*qua + total
    if cod=="002":
        qua=int(input("Digite a quantidade de mercadorias"))
        total=1.00*qua + total
    if cod=="003":
        qua=int(input("Digite a quantidade de mercadorias"))
        total=0.70*qua + total
    if cod=="004":
        qua=int(input("Digite a quantidade de mercadorias"))
        total=5.00*qua + total
    if cod =="005":
        qua=int(input("Digite a quantidade de mercadorias"))
        total=8.00*qua + total
print("O valor total de mercadorias é R$",total)


        
    
