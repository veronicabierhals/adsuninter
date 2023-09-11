def borda(s1):
    tam = len(s1) #lê o tamanho da string
    
    if tam: #só imprime caso exista algum caractere, retornar verdadeiro
        print('+', '-' *tam, '+') #multiplicao os traços pelo tamanho da string
        print('|', s1, '|')
        print('+', '-' *tam, '+')

#programa principal
borda('Olá, Mundo!')
borda('Lógica de Programação e Algorítmos')