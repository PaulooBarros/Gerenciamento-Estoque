'''
Tentativa da criação de um Sistema de Estoque para aprimorar com o tempo.
'''

# Variáveis Globais
username = ''
senha = ''
conta_criada = False
login = False
nome = ''
saldo_em_caixa = 00.00
produtos = {}  # Dicionário para armazenar as informações do produto.
opcao = 10


def menu_inicial():
    print('')
    print('')
    print('=' * 50)
    print('')
    print('' * 15 + 'Gerenciamento de Estoque')
    print('')
    print('' * 10 + 'Nossa função é cuidar bem do seu sonho!')
    print('')
    print('=' * 50)
    print('')
    print('1 - Criar Conta')
    print('2 - Fazer Login')
    print('0 - Sair')


def menu_principal():
    print('=' * 50)
    print('')
    print('' * 15 + 'Menu Principal')
    print('')
    print('3 - Cadastrar Produto')
    print('4 - Excluir Produto')
    print('5 - Editar Produto')
    print('6 - Resumo do estoque')
    print('7 - Sair da Conta')
    print('0 - Sair do Sistema')


def criar_conta():
    global username, senha, conta_criada
    nome = input('Digite aqui seu nome: ')
    print(f'Olá, {nome}!A nossa empresa agradece sua escolha. \n Vamos iniciar a criação da sua conta: ')
    username = input('Digite aqui o nome de usuário de sua preferência: ')
    while True:
        senha = input('Digite aqui sua senha: ')
        if len(senha) >= 4:
            break
        else:
            print('A senha deve possuir no mínimo 4 Caracteres')
    conta_criada = True
    print('Conta criada com sucesso!')
    return


def entrar_conta():
    global username, senha, conta_criada, login
    if not login:
        teste_username = input('Digite aqui seu username: ')
        teste_senha = input('Digite aqui sua senha: ')
        if teste_username == username and teste_senha == senha:
            login = True
            print('Login Realizado com Sucesso')
        else:
            print('Usuário e/ou senha estão incorretos.')
            return
    else:
        print('Você está logado!')


def sair_conta():
    global login, conta_criada
    if login and conta_criada:
        login = False
        print('Deslogando...')
        return
    else:
        print('Faça primeiro o login')
        return


def cadastrar_produto():
    global produtos
    if login:
        nome_produto = input('Digite aqui o nome do produto: ')
        while True:
            try:
                quantidade_produto = int(input('Digite aqui a quantidade disponível: '))
                break
            except:
                print('A quantidade deve ser um número inteiro.')
        while True:
            try:
                valor_produto = float(input('Digite aqui o valor do produto: '))
                break
            except:
                print('O valor do produto deve ser um número.')
        produtos[nome_produto] = {'Quantidade': quantidade_produto, 'Preço': valor_produto, 'Nome do Produto': nome_produto}
        print(f'O produto {nome_produto} foi cadastrado com sucesso.')
    else:
        print('É preciso estar logado para cadastrar um produto. ')

def excluir_produto():
    global produtos
    if login:
        produto_excluido = input('Digite aqui o nome do produto a ser excluído: ')
        if produto_excluido in produtos:
            del produtos[produto_excluido]
            print(f'Produto {produto_excluido} foi excluído com sucesso.')
        else:
            print('Produto inexistente no Estoque.')
    else:
        print('Você precisa estar logado para excluir.')


def editar_produto():
    global produtos
    if login:
        nome_produto_editar = input('Digite o nome do produto a ser editado: ')
        if nome_produto_editar in produtos:
            while True:
                try:
                    quantidade_produto = int(input('Digite a quantidade do produto: '))
                    break
                except:
                    print('A quantidade do produto deve ser um número inteiro')
            while True:
                try:
                    valor_produto = float(input('Digite aqui o valor do produto: '))
                    break
                except:
                    print('O valor do produto deve ser um número.')
        produtos[nome_produto_editar] = {'Quantidade':quantidade_produto, 'Preço': valor_produto}
        print(f'O produto {nome_produto_editar} foi editado com sucesso. Quantidade: {quantidade_produto} e Preço: {valor_produto}')
    else:
        print('Você precisa estar logado para editar um produto.')


def cadastrar_venda():
    pass
def resumo_estoque():
    global produtos
    if login:
        if produtos:
            print('\nResumo Estoque')
            for nome_produto, info in produtos.items():
                quantidade = info.get('Quantidade', 'Informação não disponível')
                valor = info.get('Preço', 'Informação não disponível')
                print(f'Produto: {nome_produto}, Quantidade: {quantidade}, Valor: {valor}')
        else:
            print('Não há produtos no estoque.')
    else:
        print('É preciso estar logado para ver o resumo do estoque.')



def sair_conta():
    global login
    if login:
        login = False
        print('Você foi deslogado.')
    else:
        print('Você não está logado.')

def main():
    global opcao
    while True:
        if login:
            menu_principal()
        else:
            menu_inicial()
        while True:
            try:
                opcao = int(input('Digite aqui a opção desejada: '))
                break
            except:
                print('A opção desejada deve ser um número inteiro.')
        if opcao == 1 and not login:
            criar_conta()
        elif opcao == 2 and not login:
            entrar_conta()
        elif opcao == 3 and login:
            cadastrar_produto()
        elif opcao == 4 and login:
            excluir_produto()
        elif opcao == 5 and login:
            editar_produto()
        elif opcao == 6 and login:
            resumo_estoque()
        elif opcao == 7 and login:
            sair_conta()
        elif opcao == 0:
            print('Saindo...')
            break
        else:
            print('Opção Inválida. Tente Novamente.')

main()



