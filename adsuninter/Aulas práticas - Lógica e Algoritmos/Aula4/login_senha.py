#voltando ao inicio do laço com continue
while True:
    nome = input('Qual o seu nome?')
    if (nome != 'Lenhadorzinho'): #se a condição é verdadeira vai para o continue
        continue #volta ao inicio até ser digitado o nome de usário correto
    senha = input('Qual a sua senha?')
    if (senha == 'UnInTer'):
        break

print('Acesso concedido.')