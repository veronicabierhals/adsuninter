#numeros primos de 2 a 100
for numero in range(2, 100, 1):
    #variável que altera seu valor caso o num não seja primo
    flag = 0
    for i in range(2, numero, 1):
    #o num for divisível qualquer valor, não é primo
        if (numero % i == 0):
            flag = 1
            #caso encontre um valor divisível já faz um break,
            #assim não precisa testar até o final sem necessidade
            break
    if (not flag):
        print(numero)