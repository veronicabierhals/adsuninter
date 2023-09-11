#interrompendo um loop com break
print('Digite uma mensagem que irei repetir para você!')
print('Para encerrar escreva "sair".')
while True: #loop infinito, não testa condição
    texto = input('')
    print(texto)
    if texto == 'sair':
        break

print('Encerrando o programa...')