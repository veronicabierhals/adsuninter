mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0])

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0][0]) #1º item, 1ª letra da string
print(mochila[2][1]) #3º item, 2ª letra da string

#varredura dupla
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for item in mochila:
    for letra in item:
        print(letra, end='')
    print()

#varredura dupla alternativa
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for i in range(0, len(mochila), 1): #varredura da lista
    for j in range(0,len(mochila[i]), 1): #varredura string
        print(mochila[i][j], end='')
    print()