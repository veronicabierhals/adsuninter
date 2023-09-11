#Um aluno, para passar de ano, precisa estar aprovado em todas as matérias que ele está cursando.
#Assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente.
#Escreva um algoritmo que leia a nota final do aluno em cada matéria, e informe na tela se ele passou de ano ou não.

materia1 = float(input('Qual nota você tirou em matemática?'))
materia2 = float(input('Qual nota você tirou em física?'))
materia3 = float(input('Qual nota você tirou em Português?'))

if (materia1 >= 7 and materia2 >= 7 and materia3 >=7):
    print ('Você passou de ano!')
else:
    print('Você não passou de ano!')