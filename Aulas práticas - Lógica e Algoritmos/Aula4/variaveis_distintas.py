inicio = int(input('Digite um valor inicial:'))
fim = int(input('Digite outro valor final:'))

positivo = 0
par = 0
impar = 0
soma_positivo = 0
soma_par = 0
soma_impar = 0
cont = inicio

if (inicio < fim):
    while (cont <= fim):
        if (cont > 0): #checar se numero é positivo
            positivo = positivo + 1
            soma_positivo = soma_positivo + cont
        if (cont % 2 == 0): #checar número par
            par = par + 1
            soma_par = soma_par + cont
        else:
            impar = impar + 1
            soma_impar = soma_impar + cont
        cont = cont + 1

    media_positivo = soma_positivo / positivo
    media_par = soma_par / par
    media_impar = soma_impar / impar

    print('Quantidade de valores positivos: {}' .format(positivo))
    print('Média valores positivos: {}' .format(media_positivo))
    print('Quantidade de valores pares: {}' .format(par))
    print('Média valores pares: {}' .format(media_par))
    print('Quantidade de valores impares: {}' .format(impar))
    print('Média valores impares: {}' .format(media_impar))

else:
    print('Você digitou um valor inicial maior ou igual ao final. Encerrando o programa...')
