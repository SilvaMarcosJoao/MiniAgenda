from biblioteca.operacoes import *
from biblioteca.visual import *
import os
from time import sleep
while True:
    os.system('cls')
    titulo('MENU PRINCIPAL')
    menu(['Cadastrar Contato', 'Listar Contatos', 'Ver um Contato', 'Sair'])
    op = leiaInt('Escolha uma opção: ')
    if op == 1:
        titulo('CADASTRAR NOVO CONTATO')
        n = str(input('Nome: ')).strip().upper()
        t = validaFone('Telefone: ')
        cadastrar(n, t)
        
    elif op == 2:
        mostrarContatos()
    elif op == 3:
        titulo('VER CONTATO')
        linha = leiaInt('ID do contato: ')
        mostrarContato(linha)
    elif op == 4:
        print('Finalizando programa...')
        sleep(0.4)
        print('Programa encerrado')
        break
    else:
        print('\033[1;33mErro, digite uma opção válida\033[m')
    os.system('pause')