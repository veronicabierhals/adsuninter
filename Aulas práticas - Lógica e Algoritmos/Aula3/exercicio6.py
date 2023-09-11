#descubra se um número inteiro digitado é par ou é ímpar.
# e encontrar se o número é múltiplo de 7


x = int(input('Digite um valor inteiro:'))
if (x % 2 == 0): #número inteiro, se resto da divisão (%) é igual (==) a zero
    print('O número é par!)')
else:
    print('O número é ímpar!')
if (x % 7 == 0):
    print('Múltiplo de 7!')
else:
    print('Não é múltiplo de 7!')