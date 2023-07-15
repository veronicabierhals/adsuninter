#2 while
tabuada = 1 #vai de 1
while tabuada <= 10: #até 10
    print('TABUADA {}' .format(tabuada))
    i = 1 #inicio laço interno
    while i <= 10:
        print('{} x {} = {}' .format(tabuada, i, tabuada * i))
        i += 1
    tabuada += 1 #iterador