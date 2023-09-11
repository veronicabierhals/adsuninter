def contador(fim, inicio=0, passo=1):
    for i in range(inicio, fim, passo):
        print('{}'.format(i, end=''))
    print('\n')

#programa principal
contador(20, 10, 2)
contador(12)