mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print('Tupla: ', mochila)
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista: ', mochila)

mochila[2] = 'Laranja'
print('Lista: ', mochila)

##inserir um dado no final da lista
mochila.append('Ovos')
print('Lista: ', mochila)

#inserir um dado em um determinado local da lista
mochila.insert(1, 'Canivete')
print('Lista: ', mochila)

#deletar um dado da lista
del mochila[1]
print('Lista: ', mochila)
mochila.remove('Ovos')
print('Lista: ', mochila)