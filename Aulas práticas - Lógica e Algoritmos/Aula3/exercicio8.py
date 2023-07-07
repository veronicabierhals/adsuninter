# (x)Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário.
# Verifique se os valores formam um triângulo e classifique como:
# a) Equilátero (três lados iguais);
# b) Isósceles (dois lados iguais);
# c) Escaleno (três lados diferentes).
# Lembre-se de que, para formar um triangulo, nenhum dos lados pode ser igual a zero e um lado não pode ser maior do que a soma dos outros dois.

A = int(input('Digite o valor do 1º lado do triângulo:'))
B = int(input('Digite o valor do 2º lado do triângulo:'))
C = int(input('Digite o valor do 3º lado do triângulo:'))
if A > 0 and B > 0 and C > 0:
    if A + B > C and A + C > B and B + C > A:
        if A != B and A != C and B != C:
            print('Trângulo escaleno!')
        else:
            if A == B and B == C:
                print('Trângulo esquilátero!')
            else:
                print('Triângulo isóceles!')
    else:
        print('Ao menos um dos valores indicados não serve para formar o triângulo.')
else:
     print('Ao menos um dos valores indicados não serve para formar o triângulo.')
