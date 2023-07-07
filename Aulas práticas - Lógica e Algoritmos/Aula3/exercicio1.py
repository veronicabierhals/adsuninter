#Escreva um algoritmo que lê um valor inteiro qualquer. Após, verifique se este valor está contido dentro dos seguintes intervalos:
#-100 <= x <= -1 e 1 <= x <= 100. 
#Imprima na tela uma mensagem caso ele esteja em um dos intervalos.

x = int(input('Digite um valor inteiro:'))
if -100 <= x and x <= -1 or 1 <= x and x <= 100:
    print ('O valor {} está dentro do intervalo!' .format(x))
else:
    print ('O valor {} não está dentro do intervalo!' .format(x))