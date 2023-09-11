nome = '' #valor falso, string vazia
while not nome: #while True
    nome = input('Digite seu nome:')
valor = int(input('Digite um número qualquer:'))
if valor: #se for True != 0
    print('Você digitou um valor diferente de zero.')
else: #se for false == 0
    print('Você digitou zero.')