# import funcoes
from sqlite3 import *
from time import *
import os
import msvcrt

def exibe(a, row):

    if a == 0:
        print('NOME: ' + row)
    elif a == 1:
        print('IDADE: ' + row)
    elif a == 2:
        print('CPF: ' + row)
    elif a == 3:
        print('EMAIL: ' + row)
    elif a == 4:
        print('TELEFONE: ' + row)
    elif a == 5:
        print('ENDEREÇO: ' + row)
    elif a == 6:
        print('CADASTRADO EM: ' + row)

def ct():


    cursor.execute("DROP TABLE IF EXISTS clientes")
    db.commit()

    cursor.execute("""
    CREATE TABLE clientes(
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        endereco TEXT,
        criado_em DATE NOT NULL
    );
    """)
    print("TABELA CRIADA COM SUCESSO!")


def inserir():
    import time

    n = str(input('NOME: ')).upper()
    i = int(input('IDADE: '))
    c = int(input('CPF: '))
    e = str(input('EMAIL: '))
    f = int(input('TELEFONE: '))
    p = str(input('ENDEREÇO: ')).upper()
    d = str(time.strftime('%d/%m/%Y'))

    cursor.execute('INSERT INTO clientes VALUES (?,?,?,?,?,?,?)', (n,i,c,e,f,p,d))
    db.commit()

    print()
    print('CLIENTE CADASTRADO COM SUCESSO')
    press = msvcrt.getch()
    clear = os.system('cls')

def listar():

    print()

    pessoa = str(input('NOME: ')).upper()

    sql = 'SELECT * FROM clientes WHERE nome = ?'

    for row in db.execute(sql, (pessoa,)):
        print()

        for a in range(7):
            print('------------------------')
            # print(row[a])
            exibe(a, str(row[a]))

            a+=1
        print('------------------------')

    press = msvcrt.getch()
    clear = os.system('cls')


db = connect('clientes.db')
cursor = db.cursor()

# ct()

a = int(input('(1) - CADASTRAR | (2) - PESQUISAR | (3) - DELETAR | (5) - FECHAR\n-> '))

while(True):

    if a == 1:

        clear = os.system('cls')

        print('CADASTRO')

        inserir()

    elif a == 2:

        clear = os.system('cls')

        print('PESQUISAR')

        listar()

    elif a == 3:

        clear = os.system('cls')

        print('DELETAR')

        nome = str(input('NOME: ')).upper()

        cursor.execute('DELETE FROM clientes WHERE nome = ?', (nome,))
        db.commit()

    elif a == 4:

        campo = str(input('NOME: ')).lower()

        mudanca = str(input('NOVO %s: ')).upper()

        nome = str(input('NOME: ')).upper()

        cursor.execute('UPDATE cliente SET ? = ? WHERE name = ?', (campo, mudanca, nome,))


    elif a == 5:

        exit()

    a = int(input('(1) - CADASTRAR | (2) - PESQUISAR | (3) - DELETAR | (5) - FECHAR\n-> '))

db.close()
