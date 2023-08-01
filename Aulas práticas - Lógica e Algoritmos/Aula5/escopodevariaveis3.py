def comida():
    ovos = 'variável local de comida'
    print(ovos) #variável local comida

def bacon():
    ovos = 'variável local de bacon'
    print(ovos) #variável local bacon
    comida() #invoca comida
    print(ovos) #variável local bacon

#programa principal
ovos = 'variável global'
bacon() #invoca bacon
print(ovos)