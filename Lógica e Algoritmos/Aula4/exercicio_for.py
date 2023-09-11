soma = 0
qtd = 0
for i in range(1,101): #se o passo for de 1 em 1 não é necessário informar
    if (i % 2 == 0): #verificar se número é par
        soma += i
        qtd += 1
media = soma / qtd
print('A média dos pares de 1 até 100 é: {}' .format(media))