print('CALCULADORA')
print('+ adição')
print('- subtração')
print('* multiplicação')
print('/ divisão')
print('Digite SAIR para sair')

op = input('Qual operação deseja fazer?')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite um número:'))
    y = int(input('Digite mais um número:'))

while (op != 's'):
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
        print('Operação inválida!')
    op = input('Qual operação deseja fazer?')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite um número:'))
        y = int(input('Digite mais um número:'))

print('Encerrando o programa...')