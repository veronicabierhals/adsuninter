print('CALCULADORA')
print('+ adição')
print('- subtração')
print('* multiplicação')
print('/ divisão')
print('Digite SAIR para sair')

op = input('Qual operação deseja fazer?')
while op == '+' or op == '-' or op == '*' or op == '/': #irá verificar se é uma operação válida, se não for, encerra o programa
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
    op = input('Qual operação deseja fazer?')
if op == 'SAIR' or op == 'sair':
    print('Você digitou SAIR')
else:
    print('Operação inválida!')

print('Encerrando o programa...')