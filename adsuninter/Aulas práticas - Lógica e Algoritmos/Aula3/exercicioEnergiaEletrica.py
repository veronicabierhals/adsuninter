#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
#Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.

kwh = float(input('Quantos kWh foram consumidos?'))
print('Tipo de instalação:')
print('R para residências')
print('I para indústrias')
print('C para comércios')
tipo = input('Digite o tipo de instalação:')

if (tipo == "R" and kwh <= 500):
    preco = kwh * 0.40
elif(tipo == "R" and kwh > 500):
    preco = kwh * 0.65
elif (tipo == "I" and kwh <= 1000):
    preco = kwh * 0.55
elif (tipo == "I" and kwh > 1000):
    preco = kwh * 0.60
elif (tipo == "C" and kwh <= 5000):
    preco = kwh * 0.55
else:
    preco = kwh * 0.60
print('Valor da conta de energia elétrica é R${}' .format(preco))