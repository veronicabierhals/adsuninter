#Exercício 2
#Escreve um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado
#outra forma de resolver

km = int(input('Quantos km você percorreu?'))
dias = int(input('Por quantos dias você alugou o carro?'))

preco = 60 * dias + 0.15 * km

print('Km: {}. Dias: {}' .format (km, dias))
print('O preço que você pagará pelo carro é: R${}' .format(preco))