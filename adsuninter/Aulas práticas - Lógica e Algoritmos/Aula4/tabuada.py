x = int(input('Digite o número da tabuada que você deseja:'))
print('Tabuada do {}' .format(x))

cont = 1

while (cont <= 10):
    res = cont * x
    print('{} x {} = {}' .format(cont, x, res))
    cont = cont + 1