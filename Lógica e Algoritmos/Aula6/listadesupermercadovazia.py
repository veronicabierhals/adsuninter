item = [] #lista vazia, que receberá um item preenchido com nome, quantidade e valor
mercado = [] #depois coloca o item dentro da lista de compras do mercado

for i in range(3): #informa o número de itens dentro da lista
     item.append(input('Digite o nome do item:')) #dados da lista item
     item.append(int(input('Digite a quantidade:'))) #dados da lista item
     item.append(float(input('Digite o valor:'))) #dados da lista item
     mercado.append(item[:]) #coloca a lista item copiada dentro da lista de mercado
     item.clear() #limpa a lista para reiniciar a reinserção de novos dados na nova lista
print(mercado)

#forma simplificada
mercado = []

for i in range(3):
    nome = input('Digite o nome do item:')
    qtd = int(input('Digite a quantidade'))
    valor = float(input('Digite o valor:'))
    mercado.append([nome, qtd, valor])
print(mercado)
