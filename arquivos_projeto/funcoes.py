from tkinter import messagebox
import psycopg2
import classes


def conectar_banco():

    try:
        conexao = psycopg2.connect(database = "postgres", user = "postgres", password = "123", host = "127.0.0.1", port = "5432")
        cursor = conexao.cursor()
        return conexao, cursor
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
        return None, None

def fechar_conexao(conexao, cursor):
    if(conexao):
            cursor.close()
            conexao.close()
        
def gerar_codigo():
    try:
        conexao, cursor = conectar_banco()
        sql = 'SELECT MAX(codigo) FROM public.cadastro'
        cursor.execute(sql)
        max_codigo = cursor.fetchone()[0]
        if max_codigo is None:
            return 1 
        else:
            return max_codigo + 1
    except psycopg2.DatabaseError as err:
        messagebox.showinfo('Erro ao gerar código: ', err)
    finally:
        fechar_conexao(conexao, cursor)   

def criar_tabela():
    try:
        conexao, cursor = conectar_banco()
        sql = "CREATE TABLE IF NOT EXISTS cadastro (Codigo INT PRIMARY KEY NOT NULL, CPF VARCHAR(11) NOT NULL, nome TEXT NOT NULL, idade INT NOT NULL);" 
        cursor.execute(sql)
        conexao.commit()
    except psycopg2.DatabaseError as err:
        messagebox.showinfo('Erro ao gerar código: ', err)
    finally:
        fechar_conexao(conexao, cursor)  

def cadastrar_cliente(cpf, nome, idade):
    
    try:
        conexao, cursor = conectar_banco()
        if not conexao:
            return
            
        codigo = gerar_codigo()
        sql = 'INSERT INTO public.CADASTRO (codigo, cpf, nome, idade) VALUES (%s,%s,%s,%s);'
        cursor.execute(sql,(codigo, cpf, nome, idade))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
              
    except psycopg2.DatabaseError as err:
        messagebox.showinfo('Erro de banco de dados: ',err)
    finally:
        fechar_conexao(conexao, cursor)

def alterar_dados(codigo, cpf=None, nome=None, idade=None):
    try:
        conexao, cursor = conectar_banco()

        resposta = messagebox.askyesno("Confirmação", "Você deseja continuar?")
        if resposta:
            if cpf:
                sql = "UPDATE public.cadastro SET cpf = %s WHERE codigo = %s"
                cursor.execute(sql, (cpf, codigo))
                
            if nome:
                sql = "UPDATE public.cadastro SET nome = %s WHERE codigo = %s"
                cursor.execute(sql, (nome, codigo))
                
            if idade:
                sql = "UPDATE public.cadastro SET idade = %s WHERE codigo = %s"
                cursor.execute(sql, (idade, codigo))

            conexao.commit()
            messagebox.showinfo("Sucesso", "Dados alterados com sucesso!")
        else:
            messagebox.showinfo("Ação cancelada", "nenhuma alteração foi feita.")
        
    except psycopg2.DatabaseError as err:
        messagebox.showinfo('Erro de banco de dados: ',err)
    finally:
        fechar_conexao(conexao, cursor)

def deletar_dados(codigo):
    try:
        conexao, cursor = conectar_banco()
        
        resposta = messagebox.askyesno("Confirmação", "Você deseja continuar?")
        if resposta:
            sql = 'DELETE FROM public.cadastro WHERE codigo = %s;'
            cursor.execute(sql, (codigo,))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        else:
            messagebox.showinfo("Ação cancelada", "nenhuma alteração foi feita.")
        
    except psycopg2.DatabaseError as err:
        messagebox.showinfo('Erro de banco de dados: ',err)
    finally:
        fechar_conexao(conexao, cursor)
    
def listar_tabela():
        try:
            conexao, cursor = conectar_banco()
            sql = "select * from public.cadastro"
            cursor.execute(sql)
            registros = cursor.fetchall()             
                
        except (Exception, psycopg2.Error) as error:
            messagebox.showinfo("Error in select operation", error)
    
        finally:
            fechar_conexao(conexao, cursor)
        return registros