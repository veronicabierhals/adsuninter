def comida():
    global ovos
    ovos = 'comida'

#programa principal
ovos = 'global'
comida() #invoca a função comida
print(ovos)