s1 = 'Lógica de Programação e Algorítmos'
s1.startswith('Lógica') #verifica se a palavra lógica está no início da string

s1 = 'Lógica de Programação e Algorítmos'
s1.endswith('Algoritmos')

s1 = 'Lógica de Programação e Algorítmos'
s1.endswith('algoritmos') #com letra minúscula False

#alterando para minúsculo
s1 = 'Lógica de Programação e Algorítmos'
s1.lower().endswith('algoritmos') #lower() converte toda a string pára minúsculo para depois verificar

s1 = 'Lógica de Programação e Algorítmos'
print(s1.upper())
print(s1.lower())