#app de vendas empresa x que vende por atacado
#descontos por unidade
#até 4 - 0% / entre 5 e 19 - 3% / entre 20 e 99 - 6% / maior ou igual 100 - 10%
#(x)entrar com valor unitário do produto (decimal é feito com ponto e não com vírgula)
#(x)entrar com a quantidade do produto
#retornar valor total sem desconto
#retornar valor total após desconto
#usar if, elif e else
#usar exemplo SAÍDA DE CONSOLE de compra de mais de 10unid
#Ex de saida
#(x) Bem Vindo a Loja do Renan Portela Jorge (Identificador Pessoal)
#(x)Entre com valor do produto: 12.40
#(x)Entre com a quantidade: 10 )numero inteiro
#O valor sem desconto foi: R$124.00 (colocar :.2f)
#O valor com desconto foi: R$120.28 (desconto de 3%)

print('Bem-Vindo a Loja da Veronica Veiga Bierhals')
valor = float(input('Digite o valor do produto:'))
qtd = int(input('Digite a quantidade desejada:'))
#teste em cima da variável quantidade
if (qtd <= 4):
    desc = 0.00
elif (qtd >= 5 and qtd <= 19): #outra forma (5 <= qtd <= 19)
    desc = 0.03
elif (qtd >= 20 and qtd <= 99):
    desc = 0.06
else:
    desc = 0.10

total_sem_desc = valor * qtd
print('O valor sem desconto foi: R${}' .format(total_sem_desc))

total_com_desconto = total_sem_desc - (total_sem_desc * desc) #o valor entre parenteses é para calcular o desconto, o resultado subtrai pelo valor que está fora do parenteses.
print('O valor com desconto foi: R${:.2f}' .format(total_com_desconto))