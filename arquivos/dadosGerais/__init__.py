def arquivoExiste(arquivo):

    try:
        a = open(arquivo, 'rt')
        a.close()

    except FileNotFoundError:
        return False

    else:
        return True
    

def criarArquivo(arquivo):

    try:
        a = open(arquivo, 'wt+')
        a.close()
    
    except:
        print('Houve um erro na criação do arquivo!')

    else:
        print(f'Arquivo {arquivo} criado com sucesso!')


def lerArquivo(arquivo):

    try:
        a = open(arquivo, 'rt')

    except:
        print('Erro ao ler o arquivo!')

    else:
        print('\033[1;30m-'*57)
        print('                   PESSOAS CADASTRADAS')
        print('-'*57)
        print(f'{"Nome":<30}{" Idade":>1}{"CPF":>15}')
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>1} anos{dado[2]:>20}')

    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0, cpf=0):

    try:
        a = open(arquivo, 'at')

    except:
        print('Houve um erro na abertura do arquivo!')

    else:

        try:
            a.write(f'{nome};{idade};{cpf}\n')
        
        except:
            print('Houve um erro na hora de escrever os dados!')
        
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

