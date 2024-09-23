import sqlite3 as conector 
def criar_tabelas():
    try:   
        conexao = conector.connect('registro_notas.db')
        cursor = conexao.cursor()
        sql1 = '''CREATE TABLE if not exists tbaluno (
        matricula INTEGER NOT NULL,
        nome TEXT NOT NULL,
        curso TEXT NOT NULL,
        PRIMARY KEY (matricula) 
        );'''
        sql2 = '''CREATE TABLE if not exists tbnota (
        item INTEGER PRIMARY KEY AUTOINCREMENT,
        valor FLOAT NOT NULL,
        matricula INTEGER NOT NULL,
        FOREIGN KEY (matricula) REFERENCES tbaluno(matricula)
        );'''
        cursor.execute(sql1)
        cursor.execute(sql2)
        conexao.commit()
        print('Banco de dados ok')
    except conector.DatabaseError as err:
        print('Erro de banco de dados',err)
    finally:
        if(conexao):
            cursor.close()
            conexao.close()
criar_tabelas() 
