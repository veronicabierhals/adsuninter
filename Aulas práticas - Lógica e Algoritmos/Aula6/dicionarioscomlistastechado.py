games = {'nome':[], 'videogame':[], 'ano':[]} #dicionário - palavra-chave e lista vazia
for i in range(3):
    nome = input('Qual o nome do jogo?')
    videogame = input('Para qual video-game ele foi lançado?')
    ano = input('Qual o ano de lançamento?')
#povaomento do dicionário
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-'*20)
print(games)