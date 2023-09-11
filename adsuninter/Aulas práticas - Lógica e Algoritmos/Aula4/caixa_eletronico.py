valor = int(input('Digite o valor em R$:'))
qtd = 0

#todos com if pois passará por todos eles
#1º verificar quantas notas de cada valor há dentro no número informado
#2º colocar dentro de um laço de repetição, pois assim ele não verificará todas as notas caso o valor acabe antes, isso otimiza o programa.
while True:
    if valor >= 100:
        cedulas100 = valor // 100 #divisão pegando somente parte inteira
        valor -= cedulas100 * 100 # valor - nº cedulas para saber quantas cédulas serão
        print('cédulas de 100: {}' .format(cedulas100))
        if not valor: #se sobrar valor 0
            break #encerra o programa
    if valor >= 50:
        cedulas50 = valor // 50 
        valor -= cedulas50 * 50 
        print('cédulas de 50: {}' .format(cedulas50))
        if not valor:
            break
    if valor >= 20:
        cedulas20 = valor // 20 
        valor -= cedulas20 * 20 
        print('cédulas de 20: {}' .format(cedulas20))
        if not valor:
            break
    if valor >= 10:
        cedulas10 = valor // 10 
        valor -= cedulas10 * 10 
        print('cédulas de 10: {}' .format(cedulas10))
        if not valor:
            break
    if valor >= 5:
        cedulas5 = valor // 5
        valor -= cedulas5 * 5 
        print('cédulas de 5: {}' .format(cedulas5))
        if not valor:
            break
    if valor: #o que sobrar será cédulas de 1
        cedulas1 = valor
        print('cédulas de 1: {}' .format(cedulas1))
        break
