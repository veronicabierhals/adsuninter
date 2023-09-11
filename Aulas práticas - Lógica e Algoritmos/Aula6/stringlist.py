s1 = list('Algoritmos')
print(s1) #print separado
print(''.join(s1)) #print agrupado

#assim é possível alterar a string pois ela é uma lista
s1[0] = 'a'
print(''.join(s1))