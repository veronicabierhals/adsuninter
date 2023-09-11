#mesma referência
x = [5, 7, 9, 11]
y = x
print(x)
print(y)

y[0] = 2
print(x)
print(y)

# cópia
x = [5, 7, 9, 11]
y = x[:] # [:] cria uma cópia na memória, diferente da outra variável
print(x)
print(y)

y[0] = 2
print(x)
print(y)