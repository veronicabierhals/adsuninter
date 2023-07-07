#Escreva um algoritmo que leia dois valores numéricos
#que pergunte ao usuário qual operação ele deseja realizar: adição (+), subtração (-), multiplicação (*) ou divisão (/).
#Exiba na tela o resultado da operação desejada.

n1 = float(input('Digite um número:'))
n2 = float(input('Digite mais um número:'))
print('Qual operação deseja realizar?')
print('adição (+)')
print('subtração (-)')
print('multiplicação (*)')
print('divisão (/)')
op = input ('Digite uma das opções:')

if (op == '+'):
    res = n1 + n2
elif (op == '-'):
    res = n1 - n2
elif (op == '*'):
    res = n1 * n2
else:
    res = n1 / n2

print('Resultado: {} {} {} = {}' .format(n1, op, n2, res))
