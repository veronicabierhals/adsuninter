inicial = int(input('Digite um número para saber seus 10 primeiros múltiplos de 3:'))
x = inicial
contador = 0

while (contador < 10):
    if (x % 3 == 0): #verificação múltiplos de 3
        print(x)
        contador = contador + 1
    x = x + 1