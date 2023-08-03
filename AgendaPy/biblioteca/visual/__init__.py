def menu(lista):
    """
    Exibi as operações disponíveis para o usuário utilizar.
    :param lista: é uma lista que contém o nome de cada funcionalidade
    que pode ser operada pelo usuário.
    :return: sem retorno
    """
    c = 1
    for l in lista:
        print(f'[{c}] - {l}')
        c+=1

def titulo(msg):
    """
    Tem a tarefa de exibir o título do mini-sistema de forma mais agradável.
    :param msg: recebe um texto como titulo.
    :return: sem retorno.
    """
    print('-'*len(msg))
    print(f'{msg}'.center(len(msg)))
    print('-'*len(msg))
