#Exercicio 3 de 4 da Atividade Prática

#Início da função volumeFeijoada()
def volumeFeijoada():
    print('-'*20, 'Menu 1 de 3 - Volume feijoada', '-'*20)
    while True:
        try:
            volumeF = int(input('Digite a quantidade desejada (ml): '))
            if (volumeF >= 300) and (volumeF <= 5000): #if 300 <= volumeF <= 5000:
                return  volumeF * 0.08
            else:
                print('Pare de digitar valores abaixo de 300 e acima que 5000')
                continue #retorna para a pergunta (início do laço)
        except ValueError: #caso o usuário digite letras ou números com vírgula
            print('Pare de digitar valores não inteiros')
#Fim da função volumeFeijoada()

#Início da função opcaoFeijoada()
def opcaoFeijoada():
    print('-'*20, 'Menu 2 de 3 - Opção feijoada', '-'*20)
    while True:
        opcaoF = input('Qual opção de feijoada deseja \n' + 
                       'b - Básica (Feijão + paiol + costelinha)\n' +
                       'p - Premium (Feijão + paiol + costelinha + partes de porco) \n' +
                       's - Suprema (Feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon) \n' +
                       '>>' ) #\n é pular linha
        opcaoF = opcaoF.lower()#converte para letras minúsculas
        opcaoF = opcaoF.strip() #remove os espaços em branco
        if opcaoF == 'b':
            return 1.00
        elif opcaoF == 'p':
            return 1.25
        elif opcaoF == 's':
            return 1.50
        else:
            print('Pare de digitar opções diferentes de n/p/s')
            continue #se cair nessa condição volta para o início do laço
#Fim da função opcaoFeijoada()

#Início da função acompanhamentoFeijoada()
def acompanhamentoFeijoada():
    print('-'*20, 'Menu 3 de 3 - Acompanhamento feijoada', '-'*20)
    acumulador = 0 #para o usuário ter a opção de solicitar mais acompanhamentos
    while True:
        acompanhamentoF = input('Deseja mais algum adicional: \n' +
                                '0 - Não desejo mais acompanhamentos (encerrar pedido)\n' +
                                '1 - 200g arroz \n' +
                                '2 - 150g de farofa especial \n' +
                                '3 - 100g de couve cozida \n' +
                                '4 - 1 laranja descascada\n' +
                                '>>' )
        if acompanhamentoF == '0': #trabalhar nº como string para não precisar try/except dando margem a erros
            return acumulador #aqui ele sai da função pois, o usuário não quer mais nenhum acompanhamento
        elif acompanhamentoF == '1':
            acumulador = acumulador + 5
            continue #volta para o inicio do laço
        elif acompanhamentoF == '2':
            acumulador = acumulador + 6
            continue
        elif acompanhamentoF == '3':
            acumulador = acumulador + 7
            continue
        elif acompanhamentoF == '4':
            acumulador = acumulador + 3
            continue
        else:
            print('Pare de digitar opções diferentes de 0/1/2/3/4!')  
#Fim da função acompanhamentoFeijoada()

#Início do Main
print ('-'*20, 'Bem-Vindo ao Programa de Feijoada da Veronica Veiga Bierhals', '-'*20)
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()
total = volume * opcao + acompanhamento
print ('O total ficou: R${:.2f} (Volume: R${:.2f}, Opção: R${:.2f}, Acompanhamento: R${:.2f} )' .format(total, volume, opcao, acompanhamento))