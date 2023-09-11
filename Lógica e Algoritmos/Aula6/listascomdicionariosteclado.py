game = {} #dicionário vazio
games = [] #lista vazia
for i in range(3): #para povoar a lista
    game['nome'] = input('Qual o nome do jogo?')
    game['videogame'] = input('Para qual video-game ele foi lançado?')
    game['ano'] = input('Qual o ano de lançamento?')
    games.append(game.copy())#inserção dos dados na lista
print('-'*20)
for e in games: #para andar na lista
    for i, j in e.items(): #anda dentro dos dicionários
        print('O campo {} tem o valor {}' .format(i,j)) #imprimir chave:dado