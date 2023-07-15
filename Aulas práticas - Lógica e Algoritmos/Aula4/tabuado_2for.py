#2 for (é possível fazer for pois o número de iterações é finito)
for tabuada in range(1, 11, 1):
    print('TABUADA DO {}' .format(tabuada))
    for i in range(1, 11, 1):
        print('{} x {} = {}' .format(tabuada, i, tabuada * i))