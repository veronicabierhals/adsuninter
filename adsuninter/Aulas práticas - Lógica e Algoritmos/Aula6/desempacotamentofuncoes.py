def soma(*num): #o asterisco significa desempacotamento
    soma = 0
    print('Tupla: {}' .format(num))
    for i in num: #percorre os elementos da tupla
        soma += i
    return soma 

#programa principal
print('Resultado: {}\n' .format(soma(1,2)))
print('Resultado: {}\n' .format(soma(1,2,3,4,5,6,7,8,9)))