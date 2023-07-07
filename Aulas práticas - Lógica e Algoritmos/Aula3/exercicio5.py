#uma empresa concedeu um bônus de 20% para todos seus funcionários com mais de 5 anos de empresa.
#Todos os outros que não se enquadram nessa categoria receberam uma bonificação de 10%, somente.
#Escreva um algoritmo que leia o salário do funcionário e seu tempo de empresa, e apresente a bonificação de cada funcionário na tela.

salario = float(input('Qual o seu salário?'))
tempo = int(input('Há quantos anos você trabalha na empresa?'))

if (tempo > 5):
    bonificacao = salario * 0.2
else:
    bonificacao = salario * 0.1

print('Sua bonificação é de: R${}' .format(bonificacao))
