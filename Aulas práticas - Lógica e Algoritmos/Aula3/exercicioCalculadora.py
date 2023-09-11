#Escreva um algoritmo que leia dois valores numéricos
#que pergunte ao usuário qual operação ele deseja realizar: adição (+), subtração (-), multiplicação (*) ou divisão (/).
#Exiba na tela o resultado da operação desejada.

#linhas 6 a 11 interface amigável para usuário, explicando o que ele precisa fazer.
print('CALCULADORA')
print('+ adição')
print('- subtração')
print('* multiplicação')
print('/ divisão')
print('Pressione outra tecla para sair')

op = input('Qual operação deseja fazer?')
if op == '+' or op == '-' or op == '*' or op == '/': #irá verificar se é uma operação válida, se não for, encerra o programa
    x = int(input('Digite um número:'))
    y = int(input('Digite mais um número:'))

if (op == '+'):
    res = x + y
    print('Resultado: {} + {} = {}' .format(x, y, res))
elif (op == '-'):
    res = x - y
    print('Resultado: {} - {} = {}' .format(x, y, res))
elif (op == '*'):
    res = x * y
    print('Resultado: {} * {} = {}' .format(x, y, res))
elif (op == '/'):
    res = x / y
    print('Resultado: {} / {} = {}' .format(x, y, res))
else:
    print('Operação inválida')

print('Encerrando o programa...')
