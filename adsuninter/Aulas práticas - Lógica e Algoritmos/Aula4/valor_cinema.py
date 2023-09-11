idade = int(input('Qual a sua idade?'))
if idade < 3:
    print('Você tem {} anos. Seu ingresso é gratuíto' .format(idade))
elif idade >= 3 and idade < 12:
    print('Você tem {} anos. O valor do ingresso é R$15,00' .format(idade))
else:
    print('Você tem {} anos. O valor do ingresso é R$30,00' .format(idade))