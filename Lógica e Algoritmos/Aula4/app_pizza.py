print('Bem-Vindo a Pizzaria da Veronica Veiga Bierhals')
print('-' * 21, 'CARDÁPIO', '-' * 21)
print('| Código | Descrição  | Pizza Média | Pizza Grande |')
print('|   21   | Napolitana |    R$ 20,00 |      R$26,00 |')
print('|   22   | Margherita |    R$ 20,00 |      R$26,00 |')
print('|   23   | Calabresa  |    R$ 25,00 |      R$32,50 |')
print('|   24   | Toscana    |    R$ 30,00 |      R$39,00 |')
print('|   25   | Portuguesa |    R$ 30,00 |      R$39,00 |')
print('-' * 52)


acumulador = 0

while True:
    tam = input('Qual tamanho de pizza que deseja (M/G):')
    if tam != 'M' and tam != 'G':
        print('Opção inválida! Digite M ou G.')
        continue  # se o usuário digitar algo inválido volta para o começo do while
    
    cod = input('Entre com o código do sabor desejado (21, 22, 23, 24, 25):')
    if cod != '21' and cod != '22' and cod != '23' and cod != '24' and cod != '25':
        print('Opção inválida! Digite 21, 22, 23, 24 ou 25.')
        continue  # se o usuário digitar algo inválido, volta para o começo do while

    if cod == '21' and tam == 'M':
        print('Você escolheu a pizza Napolitana tamanho M')
        acumulador += 20  # 20 é o valor da pizza
    elif cod == '21' and tam == 'G':
        print('Você escolheu a pizza Napolitana tamanho G')
        acumulador += 26

    elif cod == '22' and tam == 'M':
        print('Você escolheu a pizza Margherita tamanho M')
        acumulador += 20  # 20 é o valor da pizza
    elif cod == '22' and tam == 'G':
        print('Você escolheu a pizza Margherita tamanho G')
        acumulador += 26

    elif cod == '23' and tam == 'M':
        print('Você escolheu a pizza Calabresa tamanho M')
        acumulador += 25  # 25 é o valor da pizza
    elif cod == '23' and tam == 'G':
        print('Você escolheu a pizza Calabresa tamanho G')
        acumulador += 32.5

    elif cod == '24' and tam == 'M':
        print('Você escolheu a pizza Toscana tamanho M')
        acumulador += 30  # 30 é o valor da pizza
    elif cod == '24' and tam == 'G':
        print('Você escolheu a pizza Toscana tamanho G')
        acumulador += 39

    elif cod == '25' and tam == 'M':
        print('Você escolheu a pizza Portuguesa tamanho M')
        acumulador += 30  # 30 é o valor da pizza
    elif cod == '25' and tam == 'G':
        print('Você escolheu a pizza Portuguesa tamanho G')
        acumulador += 39

    add = input('Deseja pedir mais alguma pizza (S/N)?')
    add = add.upper()  # resolvo o problema de digitar letras maiúsculas ou minúsculas
    if add == 'S':
        continue
    else:
        print('O valor total a ser pago: R${:.2f}'.format(acumulador))
        break