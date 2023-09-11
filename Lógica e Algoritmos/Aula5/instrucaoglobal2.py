def comida():
    global ovos
    ovos = 'comida'
    bacon()

def bacon():
    ovos = 'bacon'
    pimenta()

def pimenta():
    print(ovos)

#programa principal
ovos = 12
comida()
print(ovos)