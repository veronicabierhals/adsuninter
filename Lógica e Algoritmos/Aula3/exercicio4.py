#desenvolva um algoritmo que solicite o seu ano de nascimento e o ano atual.
#Calcule a sua idade e apresente na tela, despreze o dia e o mês do ano.
#Após o cálculo, verifique se a idade é maior ou igual a 18 anos e apresente na tela uma mensagem informando que já é possível tirar a carteira de motorista caso seja de maior.

nascimento = int(input('Qual seu ano de nascimento?'))
anoAtual = int(input('Em que ano estamos?'))

idade = anoAtual - nascimento

print ('Você tem {} anos'.format(idade)) 

if (idade >= 18):
    print ('Você já pode tirar a carteira de motorista!')