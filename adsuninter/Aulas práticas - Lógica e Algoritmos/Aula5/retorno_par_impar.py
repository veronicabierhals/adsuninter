#par ou ímpar com funções
def par_impar(x):
    if (x % 2 == 0):
        return 'par'
    else:
        return 'ímpar'
    
#programa principal
print(par_impar(int(input('Digite um valor inteiro: '))))