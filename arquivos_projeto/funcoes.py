import sqlite3 as conector
import classes

def dados_cliente():
    while True:
        try:
            codigo = int(input("Código do cliente: "))
            break
        except ValueError:
            print("Por favor, insira um número válido para o código.")
   
    nome = input("Nome do cliente: ")
    while True:
        try:
            idade = int(input("idade do cliente: "))
            break
        except ValueError:
            print("Por favor, insira apenas numeros.")

    return classes.Cliente(codigo,nome,idade)

def conectar_banco():
    
    conexao = conector.connect('academia.db')
    cursor = conexao.cursor()
    return conexao, cursor

def fechar_conexao(conexao, cursor):
    if(conexao):
            cursor.close()
            conexao.close()

def criar_tabela():
    conexao, cursor = conectar_banco()
    sql = "CREATE TABLE if not exists cadastro (codigo integer, nome text, idade integer)" 
    cursor.execute(sql)
    #print("digite os dados que deseja inserir: ")
    #codigo = int(input("codigo do cliente: "))
    #nome = input("nome do cliente: ")
    #idade = int(input("idade do cliente: "))
    #cliente = classes.Cliente(cliente.codigo,cliente.nome,cliente.idade)
    #sql = "insert into cadastro (codigo, nome, idade) values (?, ?, ?)" 
    #cursor.execute(sql,(codigo, nome, idade))
    #sql = "insert into cadastro (codigo, nome, idade) values (?, ?, ?)"
    #cursor.execute(sql,(codigo, nome, idade))
    fechar_conexao(conexao, cursor)
    

def inserir_dados():
    try:
        conexao, cursor = conectar_banco()
        quantidade = int(input("digite quantas pessoas deseja cadastrar: "))
        for i in range(quantidade):
            cliente = dados_cliente()
            sql = 'INSERT INTO cadastro (codigo, nome, idade) VALUES (?,?,?);'
            cursor.execute(sql,(cliente.codigo,cliente.nome,cliente.idade))
            conexao.commit()
            print('Dados inseridos!!!')
    except conector.DatabaseError as err:
        print('Erro de banco de dados: ',err)
    finally:
        fechar_conexao(conexao, cursor)

def alterar_dados():
    try:
        conexao, cursor = conectar_banco()
        codigo = int(input("Digite o código do cliente que deseja realizar uma alteração: "))
        verificar_cliente(cursor,codigo)
        dado = input("Oque deseja alterar ?:")
        if dado in ["codigo", "nome", "idade"] :
            dado_novo = input("digite sua alteração: ")
            sql = f"UPDATE cadastro SET {dado} = ? WHERE codigo = ?"
            cursor.execute(sql,(dado_novo, codigo))
            while True:
                resposta = input("Deseja realmante realizar esta alteração?(S/N):")
                resposta = resposta.upper()
                if resposta == "S":
                    print("Novo registro: ")
                    conexao.commit()
                    print("Dados Alterados com sucesso.")
                    break
                elif resposta == "N":
                    conexao.rollback()
                    print("Ação cancelada, nenhuma alteração foi feita.")
                    break
        else:
            print("Erro: dado inválido.")
        
    except conector.DatabaseError as err:
        print('Erro de banco de dados: ',err)
    finally:
        fechar_conexao(conexao, cursor)

def deletar_dados():
    try:
        conexao, cursor = conectar_banco()
        codigo = int(input("Digite o código do cliente a ser deletado: "))
        sql = 'SELECT * FROM cadastro WHERE codigo = ?;'
        cursor.execute(sql, (codigo,))
        cliente = cursor.fetchone()
        if cliente:
            print(f"Cliente encontrado: Código: {cliente[0]} Nome: {cliente[1]} Idade: {cliente[2]}")
        else:    
            print(f"Cliente com código {codigo} não encontrado.")
        while True:
            resposta = input("Deseja realmante apagar os dados deste cliente ? (S/N):")
            resposta = resposta.upper()
            if resposta == "S":
                sql = 'DELETE FROM cadastro WHERE codigo = ?;'
                cursor.execute(sql, (codigo,))
                conexao.commit()
                print("Dados deletados com sucesso.")
                break
            elif resposta == "N":
                conexao.rollback()
                print("Ação cancelada, nenhuma alteração foi feita.")
                break
            else:
                print("Entrada inválida. Por favor, digite apenas 'S' para sim ou 'N' para não.")
    except conector.DatabaseError as err:
        print('Erro de banco de dados: ',err)
    finally:
        fechar_conexao(conexao, cursor)


def listar_tabela():
    try: 
        conexao, cursor = conectar_banco()
        sql = 'SELECT * FROM cadastro'
        cursor.execute(sql)
        registros = cursor.fetchall()
        for reg in registros:
            codigo,nome,idade = reg
            print('codigo:',codigo,'Nome:',nome,'idade:',
            idade)
    except conector.DatabaseError as err:
        print('Erro de banco de dados',err)
    finally:
        fechar_conexao(conexao, cursor)



def verificar_cliente(cursor,codigo):
    sql = 'SELECT * FROM cadastro WHERE codigo = ?;'
    cursor.execute(sql, (codigo,))
    cliente = cursor.fetchone()
    if cliente:
        print(f"Cliente encontrado: Código: {cliente[0]} Nome: {cliente[1]} Idade: {cliente[2]}")
    else:    
        print(f"Cliente com código {codigo} não encontrado.")
    
if __name__ == "__main__":
    alterar_dados()

def confirmar_acao():
    while True:
                resposta = input("Deseja realmante apagar os dados deste cliente ? (S/N):")
                resposta = resposta.upper()
                if resposta == "S":
                    sql = 'DELETE FROM cadastro WHERE codigo = ?;'
                    cursor.execute(sql, (codigo,))
                    conexao.commit()
                    print("Dados deletados com sucesso.")
                    break
                elif resposta == "N":
                    conexao.rollback()
                    print("Ação cancelada, nenhuma alteração foi feita.")
                    break