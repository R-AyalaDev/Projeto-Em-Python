def leiaStr(msg):

    while True:
        a = 0
        try:
            nome = input(msg)
        
        except KeyboardInterrupt:
            print('\033[1;31mUsuário prefiriu não digitar o nome.\033[1;30m')
            return 'desconhecido'

        if nome.isnumeric() or len(nome) >= 30:
            print('\033[1;31mERRO! Digite um nome válido.\033[1;30m')
            continue
            
        for letra in nome:

            if letra.isnumeric():
                print('\033[1;31mERRO! Digite um nome válido.\033[1;30m')
                a = 2
                break
        
        if a == 2:
            continue
                
        else:
            return nome


def leiaInt(msg):

    while True:      

        try:
            n = int(input(msg))

        except KeyboardInterrupt:
            print('\033[1;31mUsuário prefiriu não digitar esse número.\033[1;30m')
            return 0
        
        except:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[1;30m')

        else:
            return n


def leiaCPF(msg):

    while True:

        try:
            c = input(msg)
        
        except KeyboardInterrupt:
            print('\033[1;31mUsuário prefiriu não digitar o CPF.\033[1;30m')
            return 0
        
        try:
            if (len(c) != 14) and (c[3] != '.') and (c[7] != '.') and (c[11] != '-'):
                print('\033[1;31mERRO! Digite um CPF válido!\033[1;30m')
            
        except:
            print('\033[1;31mERRO! Digite um CPF válido!\033[1;30m')

        else:
            return c


def linha(tam=42):
    return '\033[1;30m-'* tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c}\033[1;30m - \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[33mSua Opção: ')
    return opc