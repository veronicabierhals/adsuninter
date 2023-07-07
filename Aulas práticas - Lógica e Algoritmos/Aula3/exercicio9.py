#escreva um algoritmo que lê um nome e uma idade
#caso o nome digitado seja Vinicius, escreva isso na tela
#caso o usuário digite qualquer outro nome, verifique sua idade.
#se for menor que 18 anos, informe que é de menor.
#se for maior que 100 anos, informe que essa pessoa possivelmente não existe.

nome = input('Qual seu nome?')
idade = int(input('Qual sua idade?'))

if nome == 'Vinicius':
    print('Olá, Vinicius')
elif idade < 18:
    print('Você não é Vinicius! E é menor de idade')
elif idade > 100:
    print ('Diferente de você, o Vinicius não é imortal!')