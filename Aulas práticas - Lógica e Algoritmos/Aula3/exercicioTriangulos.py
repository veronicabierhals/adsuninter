# Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. (linhas 8,9,10)
# Verifique se os valores formam um triângulo e classifique como:
# a) Equilátero (três lados iguais);
# b) Isósceles (dois lados iguais);
# c) Escaleno (três lados diferentes).
# para formar um triangulo, nenhum dos lados pode ser igual a zero (linha 12)
# e um lado não pode ser maior do que a soma dos outros dois. (linha 13)

A = int(input('Digite o valor do 1º lado do triângulo:'))
B = int(input('Digite o valor do 2º lado do triângulo:'))
C = int(input('Digite o valor do 3º lado do triângulo:'))
if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B + C) > A: #é possível colocar linhas 11 e 12 juntas
    #se você chegou até aqui, é porque o trinângulo é válido!
        if A != B and A != C and B != C: #todos os lados diferentes
            print('Trângulo escaleno!')
        else:
            if A == B and A == C and B == C:
                print('Trângulo esquilátero!')
            else:
                print('Triângulo isóceles!')
    else:
        print('Ao menos um dos valores indicados não serve para formar o triângulo.') #referente a linha 13, executado se a condicional for False
else:
     print('Ao menos um dos valores indicados não serve para formar o triângulo.') #referente a linha 12, executado se a condicional for False
