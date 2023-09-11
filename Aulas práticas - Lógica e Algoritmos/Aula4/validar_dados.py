#validar dados de entrada
x = int(input('Digite um valor maior que zero:')) #pede o valor
while (x <= 0): #testa ele
    x = int(input('Digite um valor maior que zero:'))
print ('Você digitou {}. Encerrando o programa...' . format(x))