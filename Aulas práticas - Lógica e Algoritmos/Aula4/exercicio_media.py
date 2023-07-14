soma = 0
qtd_num = 0
x = 0

while True:
    x = int(input('Digite um valor inteiro:'))
    if x < 0:
        continue
    if not x:
        break
    soma += x
    qtd_num += 1
media = soma / qtd_num
print('A média dos valores digitados é: {}' .format(media))