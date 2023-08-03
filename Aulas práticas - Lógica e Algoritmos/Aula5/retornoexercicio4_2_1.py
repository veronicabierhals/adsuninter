def valida_string(pergunta, min, max): #dados na linha 10
    s1 = input(pergunta) #lê a palavra
    tam = len(s1) #vê o tamanho
    while ((tam < min) or (tam > max)):#verifica o tamanho informado na linha 10 - min=10, max=30
        s1 = input(pergunta)
        tam = len(s1)
    return s1

#programa principal
x = valida_string('Digite uma string: ', 10, 30)
print('Você digitou a string: {}. \n Dado válido. Encerrando o programa...' .format(x))