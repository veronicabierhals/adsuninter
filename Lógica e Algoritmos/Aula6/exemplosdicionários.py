game = {'nome':'Super Mario', #chave:dado
        'desenvolvedora':'Nintendo',
        'ano':1990}
print(game)

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

#values
print(game.values())

#outra forma
for i in game.values():
    print(i)

#keys
print(game.keys())

#outra forma
for i in game.keys():
    print(i)

#items
print(game.items())

#outra forma
for i,j in game.items(): #i = chave, j = dado
    print('{} = {}' .format(i,j))