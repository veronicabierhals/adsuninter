mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)

print(mochila[0]) #print do Elemento 1 - índice 0
print(mochila[2]) #print do elemento 3 - índice 2
print(mochila[0:2]) #print do elemento 1 e 2 - índice 0 e 1 (0 a 2 faz até o índice anterior)
print(mochila[2:]) #print dos elementos a partir do índice 2
print(mochila[-1]) #print do último elemento (o negativo lê a lista de traz para frente)

for item in mochila:
   print('Na minha mochila tem: {}' .format(item))

tam = len(mochila)
for i in range (0, tam, 1): #início (0), fim (tam), de um em um (1)
    print('Na minha mochila tem: {}' .format(mochila[i]))

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade

print(mochila)
print(upgrade)
print(mochila_grande)

mochila_grande_invertida = upgrade + mochila
print(mochila_grande)
print(mochila_grande_invertida)