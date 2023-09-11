hora_inicial = int(input('Digite a hora inicial (0 à 23h)'))
hora_final = int(input('Digite a hora final (0 à 23h)'))

while (hora_inicial > hora_final) or (hora_inicial < 0) or (hora_inicial > 23) or (hora_final < 0) or (hora_final > 23):
    hora_inicial = int(input('Digite a hora inicial (0 à 23h)'))
    hora_final = int(input('Digite a hora final (0 à 23h)'))

for h in range(hora_inicial, hora_final + 1, 1):
    for m in range(0,60,1):
        for s in range(0,60,1):
            print('{:02d}:{:02d}:{:02d}'.format(h, m, s))