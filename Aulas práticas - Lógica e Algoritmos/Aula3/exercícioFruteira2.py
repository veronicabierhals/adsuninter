#Escreva um algoritmo em que o usuário escolhe se ele quer comprar maçãs, laranjas ou bananas.
#Deverá ser apresentado na tela um menu com a opção 1 para maçã, 2 para laranja e 3 para banana.
#Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar.
#O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela.
#Considere que uma maçã custa R$ 2,30, uma laranja R$ 3,60 e uma banana 1,85.
#escrito vom estrutura elif

print('Escolha a fruta que deseja comprar:')
print('1 - Maçã')
print('2 - laranja')
print('3 - banana')
produto = int(input('Qual sua escolha?'))
qtd = int(input('Quantas unidades?'))

if (produto == 1):
    preco = qtd * 2.30
    print('Você comprou {} maçãs. Total à pagar: R${}' .format(qtd,preco))
elif (produto == 2):
    preco = qtd * 3.60
    print('Você comprou {} laranjas. Total à pagar: R${}' .format(qtd,preco))
elif (produto == 3):
    preco = qtd * 1.85
    print('Você comprou {} bananas. Total à pagar: R${}' .format(qtd,preco))
else:
    print('Produto inexistente!')