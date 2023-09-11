idade = int(input('Qual a sua idade?'))
while idade >0:
    sexo = input('Qual seu sexo? (Responda M para masculino e F para feminino).')
    if ((sexo == 'M') or (sexo == 'm')):
        print('Boa noite, Senhor. Sua idade é {}. ' .format(idade))
    else:
        if ((sexo == 'F') or (sexo == 'f')):
            print('Boa noite, Senhora. Sua idade é {}. ' .format(idade))
        else:
            print('Opção de sexo inexistente.')
    idade = int(input('Qual a sua idade?'))
print('Encerrando...')
