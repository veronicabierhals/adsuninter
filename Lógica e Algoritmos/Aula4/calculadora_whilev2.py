print('CALCULADORA')
print('+ adição')
print('- subtração')
print('* multiplicação')
print('/ divisão')
print('Digite SAIR para sair')



while True:
    op = input('Qual operação deseja fazer?')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite um número:'))
        y = int(input('Digite mais um número:'))

    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}' .format(x, y, res))
        continue #volta para o começo do laço
    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}' .format(x, y, res))
        continue
    elif (op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}' .format(x, y, res))
        continue
    elif (op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}' .format(x, y, res))
        continue
    elif (op == 's'):
        break
    else:
        print('Operação inválida!')

print('Encerrando o programa...')