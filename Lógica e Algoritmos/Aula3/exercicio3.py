#Lê dois valores numéricos inteiros e compara se o primeiro é maior do que o segundo, utilizando uma condicional simples.
#Caso seja (resultado verdadeiro), ele imprime na tela a mensagem informando que o primeiro valor digitado é maior do que o segundo.
#Expandindo este exercício, podemos colocar duas condicionais simples.
#Uma realizando o teste para verificar se o primeiro valor é maior do que o segundo, e outra para verificar se o segundo é maior do que o primeiro.

x = int(input('Digite um valor inteiro:'))
y = int(input('Didite um segundo valor inteiro:'))
if (x > y):
    print('O primeiro valor é maior que o segundo!')
if (x < y):
    print('O segundo valor é maior que o primeiro!')