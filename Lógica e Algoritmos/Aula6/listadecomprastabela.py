mercado = [['Cebola', 2, 0.58], ['Tomate', 3, 0.48], ['Alface', 1, 2.0]]

soma = 0
print('Lista de compras:')
print('-'*52)
print('item | quantidade | valor unitário | total do item')
for item in mercado:
    print('{} | {} | {} | {}' .format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print('-'*52)
print('Total a ser pago: {}' .format(soma))