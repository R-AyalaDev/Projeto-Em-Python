from arquivos import interface
from arquivos import dadosGerais
from time import sleep

arq = 'rickiproducoes.txt'

if not dadosGerais.arquivoExiste(arq):
    dadosGerais.criarArquivo(arq)

while True:

    resposta = interface.menu(['\033[1;36mVer Pessoas Cadastradas', '\033[1;32mCadastrar Pessoas Novas', '\033[1;34mRemover Dados Existentes', '\033[1;31mSair do Sistema'])

    if resposta == 1:
        dadosGerais.lerArquivo(arq)

    elif resposta == 2:
        interface.cabecalho('NOVO CADASTRO')
        nome = interface.leiaStr('Nome e Sobrenome: ')
        idade = interface.leiaInt('Idade: ')
        cpf = interface.leiaCPF('CPF: ')
        dadosGerais.cadastrar(arq, nome, idade, cpf)

    elif resposta == 3:
        dadosGerais.removerTudo
        interface.cabecalho('DADOS REMOVIDOS COM SUCESSO')
        print('\033[1;30m')

    elif resposta == 4:
        print('\033[1;31mSaindo do sistema!! Até Logo...\033[m')
        break

    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')

    sleep(1)