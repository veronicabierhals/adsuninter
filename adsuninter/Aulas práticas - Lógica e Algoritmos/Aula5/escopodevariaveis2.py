#cada escopo possúi variáeis diferentes
#neste caso 'ovos' aparece nas duas porém não interferem entre sim

def comida():
    ovos = 12
    bacon()
    print(ovos)

def bacon():
    ovos = 6

#programa principal
comida()