total = 0 #acumulador pessoas
dinheiro = 0 #acumulador valor ingressos

while True:
    idade = input('Qual a sua idade?')
    if idade == 'sair' or idade == 'SAIR':
       break
    idade = int(idade) #idade recebe ela mesmo e converte para inteiro
    total += 1 #acumulador idade
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso #acumulador dinheiro


media = dinheiro / total 
print('Total de pessoas {}' .format(total))
print('Total arrecadação {}' .format(dinheiro))
print('Média arrecadada {}' .format(media))