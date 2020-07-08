print("Olá Sirlei! Bem vinda a atividade n° 2 da disciplina de lógica!")
prob=int(input("Para avaliar o primeiro programa digite 1, o segundo digite 2, e o terceiro digite 3, para encerrar digite 4:  "))
while prob >=1 and prob <=3:
   
   if prob ==1:
        print("Encontre o valor de delta utilizando Bhaskara nas equações de segundo grau desejadas:")
        A=float(input("Digite o valor de A: "))
        B=float(input("Digite o valor de B: "))
        C=float(input("Digite o valor de C:"))
        D=(B**2)-(4*A*C)
        E=D/2
        print ("O valor da equação de segundo grau com os valores de", A, B,C,"tem o delta",D)
        print ("O valor de delta dividido por 2 é", E)
        prob=int(input("Para avaliar o primeiro programa digite 1, o segundo digite 2, e o terceiro digite 3, para encerrar digite 4:  "))

   if prob ==2:
        inicio=0
        nota1=0
        media=0
        maior=0
        mediaturma=0
        while inicio !=-1:
            nota=float(input("Digite a nota do aluno: "))
            nota1= nota1 + nota
            media+=1
            if nota > maior:
               maior=nota
            inicio=int(input("Digite -1 para encerrar e 0 para continuar: "))
        
        mediaturma=nota1/media   
        print("A media da turma é",mediaturma)
        print("A nota mais alta da turma é", maior)
        prob=int(input("Para avaliar o primeiro programa digite 1, o segundo digite 2, e o terceiro digite 3, para encerrar digite 4:  "))

   if prob ==3:
        for x in range (1,4):
            nome=str(input("Qual é seu nome: "))
            peso=float(input("Qual seu peso: "))
            altura=float(input("Qual sua altura: "))
            IMC=peso/(altura**2)
            print(nome," seu peso é:",peso,"kg, sua altura é ",altura,"e seu IMC é de %.2f" % (IMC))
        prob=int(input("Para avaliar o primeiro programa digite 1, o segundo digite 2, e o terceiro digite 3, para encerrar digite 4:  "))

print ("FIM")
        
    



    
        
