#Escreva um algoritmo que obtenha do usuário uma frase de tamanho entre 10 e 30 caracteres (faça a validação desse dado).
# Após a frase ter sido digitada corretamente, faça a impressão dela na tela da maneira exata como foi digitada
#em seguida, remova os espaços da frase e imprima novamente, sem espaços.
#Para resolver esse exercício, utilize os conhecimentos fatiamento e tamanho de *strings*

frase = input('Escreva uma frase entre 10 e 30 caracteres:')
tam = len(frase)
while (tam < 10) or (tam > 30):
    frase = input('Escreva uma frase entre 10 e 30 caracteres:')
    tam = len(frase)
print('Com espaços: {}' .format(frase))
print('Sem espaços: ', end='')
for i in range(0, tam, 1):
    if (frase[i] != ' '):
        print(frase[i], end='')