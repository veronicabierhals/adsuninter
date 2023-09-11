def div():
    try:
        num1 = int(input('Digite um número:'))
        num2 = int(input('Digite um número:'))
        res = num1 / num2
    except ZeroDivisionError: #se try falhar executa essa linha
        print('Oops!  Erro de divisão por zero...')
    except: #qualquer outro erro executar esse print
        print('Algo de errado aconteceu...')
    else: #se try der executa essa linha
        return res
    finally: #sempre que colocar finally depois de try ele executará
        print('Executará sempre!')

#programa principal
print(div())   
