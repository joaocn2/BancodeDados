# Joao Vitor Savaris
# Executar o codigo .py no diretorio do Spyder
# Banco de dados deve estar em ..\Users\Usuario\.spyder-py3
#se nao
#create table player(
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#    nome text not null,
#    vida integer not null,
#   municao integer not null
#)

import sqlite3
import os
import sys
from sqlite3 import Error
import time


def conectarBanco():
    conexao = None
    try:
        database = 'banco.db'
        if not os.path.isfile(database):
            raise sqlite3.DatabaseError

        conexao = sqlite3.connect(f'file:{database}?mode=rw',
                                  uri=True)
        print('BD aberto com sucesso!')
    except sqlite3.DatabaseError:
        print('Erro: Banco de dados não existe')
        sys.exit()
    except Error as erro:
        print(erro)
        sys.exit()

    return conexao

def incluir(conexao):
    cursor = conexao.cursor()
   
    print('Rotina de inclusão de dados \n')
    nome = input('\n Nome: ')
    Vida = int(input('\n Vida: '))
    Municao = int(input('\n Municao: '))
   
    comando = f'INSERT INTO player (nome, vida, municao) VALUES("{nome}", {Vida}, {Municao} )'
    try:
        cursor.execute(comando)
        conexao.commit()
        print('INSERCAO COM SUCESSO')
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
    except Error as erro:
        print(erro)
        time.sleep(7)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu(conn)

def alterar(conexao):
    cursor = conexao.cursor()
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(3)
    print('Rotina de alteração de dados \n')
    cursor.execute("""SELECT * FROM player;""")
    for linha in cursor.fetchall():
       print(linha)
    print('\n')
    time.sleep(1)
    idd = int(input('\n ID a ser alterado os dados: '))
    nome = input('\n Nome: ')
    Vida = int(input('\n Vida: '))
    Municao = int(input('\n Municao: '))
    try:
        cursor.execute("""UPDATE player SET nome = ?, 
                   vida = ?, municao = ? WHERE id = ?""", (nome, Vida, Municao, idd))
        conn.commit()
        print('ALTERACAO COM SUCESSO')
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
    except Error as erro:
        print(erro)
        time.sleep(7)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu(conn)
     

def excluir(conexao):
    cursor = conexao.cursor()
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(3)
    print('Rotina de exclusão de dados')
    cursor.execute("""SELECT * FROM player;""")
    for linha in cursor.fetchall():
       print(linha)
    print('\n')
    time.sleep(1)
    print('Escolha o player a ser removido')
    idd = int(input('\n ID a ser removido os dados: '))
    resp = input('Deseja remover mesmo? y , n')
    if resp == 'y':
        try:
            cursor.execute("""DELETE FROM player WHERE id = ?""", (idd,))
            conn.commit()
            print('\n Registro excluido com sucesso.')
            time.sleep(4)
            os.system('cls' if os.name == 'nt' else 'clear')
        except Error as erro:
            print(erro)
            time.sleep(7)
            os.system('cls' if os.name == 'nt' else 'clear')
            menu(conn)
    else:
        menu(conn)


def listar(conexao):
    cursor = conexao.cursor()
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    try:
        cursor.execute("""SELECT * FROM player;""")
        for linha in cursor.fetchall():
           print(linha)
        print("Pressione enter para continuar")
        enter = input(' ')
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(2)
    except Error as erro:
        print(erro)
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu(conn)
       
def menu(conexao):
    opcao = 1
    while opcao != 5:
        print('MENU DE OPÇÕES')
        print('--------------')
        print('1. Incluir dados')
        print('2. Alterar dados')
        print('3. Excluir dados')
        print('4. Listar dados')
        print('5. Sair')
        time.sleep(0.5)
        opcao = int(input('Opção [1-5]: '))

        if opcao == 1:
            incluir(conexao)
        elif opcao == 2:
            alterar(conexao)
        elif opcao == 3:
            excluir(conexao)
        elif opcao == 4:
            listar(conexao)
        elif opcao == 5:
            print('Encerrando o programa...')
            conn.close()
            break
        else:
            print('Opção inválida, tente novamente')

        print()

conn = conectarBanco()
menu(conn)