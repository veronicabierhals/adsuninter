kwh = float(input('Quantos kWh foram consumidos?'))
print('Tipo de instalação:')
print('R para residências')
print('C para comércios')
print('I para indústrias')
tipo = input('Digite o tipo de instalação:')

if (tipo == "R" and kwh <= 500):
    preco = kwh * 0.40
elif(tipo == "R" and kwh > 500):
    preco = kwh * 0.65
elif(tipo == "C" and kwh <= 1000) or (tipo == "I" and kwh <= 5000):
    preco = kwh * 0.55
else:
    preco = kwh * 0.60
print('Valor da conta de energia elétrica é R${}' .format(preco))
