#resultado multiplicação
x = int(input('Digite um número:'))
y = int(input('Digite mais um número:'))

cont = 1 #controle do loop
multi = 0 #armazena resultado multiplicação
while (cont <= x):
    multi = multi + y
    cont = cont + 1
print('O resultado de {} x {} é: {}' .format(x, y, multi))