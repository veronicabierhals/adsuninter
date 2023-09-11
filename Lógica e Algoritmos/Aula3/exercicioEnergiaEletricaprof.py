kwh = float(input('Quantos kWh foram consumidos?'))
print('Tipo de instalação:')
print('R para residências')
print('C para comércios')
print('I para indústrias')
tipo = input('Digite o tipo de instalação:')

if(tipo == 'R'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65

elif(tipo == 'C'):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.6

elif(tipo == 'I'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6
else:
    print('Tipo de instalação inválida!')

print('Total a pagar: R${}' .format(kwh * preco))