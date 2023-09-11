#Exercício 2
#Escreve um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

kmPercorrido = float(input('Quantos km você percorreu?'))
dias = float(input('Por quantos dias você alugou o carro?'))

preco = dias * 60
kmRodado = kmPercorrido * 0.15

pagar = preco + kmRodado

print('O preço que você pagará pelo carro é: R${}' .format(pagar))