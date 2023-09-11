inicial = int(input('Qual o valor deseja iniciar a contagem?'))
final = int(input('Qual valor deseja encerrar a contagem?'))
x = inicial
while(x <= final):
    if (x % 2 == 0): #verificação de número par
        print(x)
    x = x + 1