#Uma loja de departamentos está oferecendo diferentes formas de pagamento, conforme opções listadas a seguir.
#Faça um algoritmo que leia o valor total de uma compra e calcule o valor do pagamento final de acordo com a opção escolhida.
#Se a escolha for por pagamento parcelado, calcule também o valor de cada parcela. Ao final, apresente o valor total da compra e o valor das parcelas:
#- Pagamento à vista – conceder desconto de 5%;
#- Pagamento em 3x – o valor não sofre alterações;
#- Pagamento em 5x – acréscimo de 2%;
#- Pagamento em 10x – acréscimo 8%.

compra = float(input('Qual valor total da sual compra?'))
print('Escolha a forma de pagamento:')
print('1 - à vista')
print('2 - Parcelado 3x')
print('3 - Parcelado 5x')
print('4 - Parcelado 10x')
pag = input('Digite a opção da forma de pagamento')

if pag == '1':
    total = compra - 0.05
    parc = total
elif pag == '2':
    total = compra
    parc = total / 3
elif pag == '3':
    total = compra + 0.02
    parc = total / 5
elif pag == '4':
    total = (compra + 0.08)
    parc = total / 10
print('O valor total da sua compra é R${}. E o valor de cada parcela será R${:.2f}' .format(total, parc))
