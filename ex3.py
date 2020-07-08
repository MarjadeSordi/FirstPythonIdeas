temperatura = []
mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
maior = 0
menor = 100
for x in range(0,12):
    print ("Temperatura do mês de ",mes[x])
    temp = float (input ("Digite: "))
    temperatura.append(temp)
    if temp >= maior:
        maior = temp
        ma = mes[x]
    if temp <= menor:
        menor = temp
        me = mes[x]
print ("A maior temperatura foi ",maior," no mês de ",ma)
print ("A menor temperatura foi ",menor," no mês de ",me)
