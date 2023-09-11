#---------------- Início das Variáveis Globais ----------------
lista_produto = []
codigo_produto = 0
#------------------ Fim das Variáveis Globais ------------------

#--------------- Inicio de cadastrar_produto() ----------------
def cadastrar_produto(codigo):
    print('Bem-Vindo ao menu de Cadastrar Produto')
    print('Código do Produto: {}' .format(codigo))
    nome = input('Entre com o NOME do produto:')
    fabricante = input('Entre com o FABRICANTE do produto:')
    preco = int(input('Entre com o PREÇO(R$) do produto:'))
    dicionario_produto = {'codigo'     : codigo,
                          'nome'       : nome,
                          'fabricante' : fabricante,
                          'preco'      : preco} #armazenamento dos dados em um dicionario
    lista_produto.append(dicionario_produto.copy()) #coloca o dicionario dentro de uma lista
#---------------- Fim de cadastrar_produto() ------------------

#--------------- Inicio de consultar_produto() ----------------
def consultar_produto():
    print('Bem-Vindo ao menu de Consultar Produto')
    while True:
        opcao_consultar = input('\nEscolha a opção desejada:\n'+
                                '1-Consultar TODOS os Produtos\n'+
                                '2-Consultar Produto por CÓDIGO\n'+
                                '3-Consultar Produto(s) por FABRICANTE\n'+
                                '4-Retornar\n'+
                                '>>')
        if opcao_consultar == '1':
           print('Você escolheu a opção Consultar TODOS os produtos')
           for produto in lista_produto: #produto vai varrer toda a lista de produtos
               print('-'*20)
               for key, value in produto.items(): #varrer todos os conjuntos chave:dado do dicionário produto
                    print('{}: {}' .format(key,value))
               print('-'*20)
        elif opcao_consultar == '2':
           print('Você escolheu a opção Consultar Produto(s) por CÓDIGO')
           valor_desejado = int(input('Entre com o CÓDIGO desejado: '))
           for produto in lista_produto:
               if produto['codigo'] == valor_desejado: #o valor do campo código desse dicionário é igual o valor desejado
                print('-'*20)
                for key, value in produto.items(): #varrer todos os conjuntos chave:dado do dicionário produto
                        print('{}: {}' .format(key,value))
                print('-'*20)
        elif opcao_consultar == '3':
            print('Você escolheu a opção Consultar Produto(s) por FABRICANTE')  
            valor_desejado = input ('Entre com o FABRICANTE desejado: ')
            for produto in lista_produto:
               if produto['fabricante'] == valor_desejado: #o valor do campo código desse dicionário é igual o valor desejado
                print('-'*20)
                for key, value in produto.items(): #varrer todos os conjuntos chave:dado do dicionário produto
                        print('{}: {}' .format(key,value))
                print('-'*20)
        elif opcao_consultar == '4':
            return #sai da função consultar produto e volta para Main
        else:
            print('Opção inválida. Tente novamente')
            continue #retorna para o início do laço
#---------------- Fim de consultar_produto() ------------------

#---------------- Inicio de remover_produto() -----------------
def remover_produto():
    print('Bem-Vindo ao menu de Remover Produto')
    valor_desejado = int(input('Entre com o CÓDIGO do produto que deseja remover: '))
    for produto in lista_produto:
        if produto['codigo'] == valor_desejado: #verifica se o código digitdo está na lista (dicionário)
            lista_produto.remove(produto)
            print('Produto Removido')
#----------------- Fim de remover_produto() -------------------

#----------------------- Inicio de Main ------------------------
print('Bem-Vindo a Mercearia da Veronica Veiga Bierhals')
while True:
    opcao_principal = input('\nEscolha a opção desejada:\n'+
                            '1-Cadastrar Produto\n'+
                            '2-Consultar Produto(s)\n'+
                            '3-Remover Produto\n'+
                            '4-Sair\n'+
                            '>>')
    if opcao_principal == '1':
        codigo_produto += 1 #para gerar código novo a cada produto
        cadastrar_produto(codigo_produto) #cada vez que a função cadastrar produto for solicitada ela vai chamar/gerar um cód produto
    elif opcao_principal == '2':
        consultar_produto()
    elif opcao_principal == '3':
        remover_produto()
    elif opcao_principal == '4':
        break #encerra o laço principal e o programa acaba
    else:
        print('Opção inválida. Tente novamente')
        continue #retorna para o início do laço
#----------------------- Fim de Main ------------------------