'''Faça um algoritmo que leia a nota de vários alunos de uma turma,
valor negativo para
nota, encerra. Ao final, deve ser escrita a média geral da turma.
'''
nota=0
media=0
var1=0
while nota >=0:
    nota=int(input("Digite a nota de um aluno:"))
    if nota >=0:
        media+=1 
        var1 = nota + var1

media_turma=(var1)/media
print ("A média da turma é",media_turma )

             
        
        
