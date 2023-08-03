from biblioteca.visual import *


def leiaInt(num):
    """
    Verifica se o valor passado é realmente inteiro.
    :param num: é valor a ser verificado.
    :return n: tendo sido verificado, retorna o valor para utilização durante o fluxo do programa.
    """

    while True:
        try:
            n = int(input(num))
        except(ValueError, TypeError):
            print (f'\033[1;31mErro, digite um número inteiro\033[m')
        else:
            return n
        
        
def validaFone(valor):
    """
    Verifica se está de acordo com a condição imposta, para ser um telefone 
    aceito pelo mini-sistema.
    :param valor: obtém o telefone passado pelo usuário no ato do cadastro.
    :return n: depois de validado, retorna o  telefone para proseguimento no processo de cadastro.
    """

    while True:
        n = input(valor).strip()
        if len(n) == 9:
            return n
        else:
            print('\033[;31mErro, digite um telefone válido\033[m')


def cadastrar(nome, telefone):
    """
    Realiza o cadastro de um contato no arquivo txt.
    :param nome: nome do contato.
    :param telefone: telefone do contato.
    :return: sem retorno.
    """

    nomeArq = 'Dados.txt'
    caminho = '..\\MiniAgenda\\AgendaPy\\Dados.txt'
    pessoa= [nome, telefone]
    try:
        if nomeArq in caminho:   
            arq = open(f'..\\MiniAgenda\\AgendaPy\\{nomeArq}', 'a')
            arq.write(f'{pessoa}\n')
        else:
            arq = open(f'..\\MiniAgenda\\AgendaPy\\{nomeArq}', 'wt+')
            arq.write(f'{pessoa}\n')
    except Exception (FileNotFoundError, NotADirectoryError) as erro:
        print(f'\033[1;31mErro, ao salvar os dados: {erro}\033[m')
    else:
        print('\033[1;32mDados salvos com sucesso!\033[m')
        arq.close()
        
    
def lerArquivo():
    """
    Tem com objetivo ler o arquivo que irá ser utilizado para gravar os dados cadastros.
    :return linhas: retorna o conteúdo do arquivo.
    """

    nomeArq = 'Dados.txt'
    caminho = '..\\MiniAgenda\\AgendaPy\\Dados.txt'
    try:
        if nomeArq in caminho:
            arq = open(f'..\\MiniAgenda\\AgendaPy\\{nomeArq}', 'r')
            linhas = arq.readlines()
    except(FileNotFoundError, NameError):
        print('\033[1;31mErro ao manipular o arquivo\033[m')
    else:
        arq.close()
        return linhas
        

def mostrarContatos():
    """
    Exibir todos os contatos cadastrados.
    :return: sem retorno.
    """

    titulo('LISTA DOS CADASTRADOS')
    linhas = lerArquivo()
    print(' NOME  - TELEFONE')   
    for l in linhas:
        print(f'{l:<15}')



def mostrarContato(lin):
    """
    Exibe um contato especifico, através da linha passada.
    :param lin: recebe a posição que o contato está na no arquivo txt.
    :return: sem retorno
    """

    arq = '..\\MiniAgenda\\AgendaPy\\Dados.txt'
    print(' NOME  - TELEFONE')
    with open(arq, 'r') as contato:
        linha = contato.readlines()
        if lin <= len(linha):
            print(linha[lin])
        else:
            print('Esse contato não existe!')
