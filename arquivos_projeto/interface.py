import tkinter as tk
from tkinter import ttk, messagebox
import funcoes
import classes

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento de Clientes")
        self.root.geometry("700x500")

        # Frame principal que mudará com cada função
        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        # Botões para cada função
        self.btnCadastrar = tk.Button(root, text="Cadastrar Cliente", command=lambda: self.carregar_tela("cadastrar"))
        self.btnConsultar = tk.Button(root, text="Consultar/Alterar Cliente", command=lambda: self.carregar_tela("consultar"))

        self.btnCadastrar.pack(side=tk.LEFT, padx=10, pady=10)
        self.btnConsultar.pack(side=tk.LEFT, padx=10, pady=10)

        self.cpf_var = tk.StringVar()  # Armazena o valor do campo CPF
        self.cpf_var.trace("w", self.limitar_cpf)


        # Exibir lista de clientes inicialmente

        self.ordem_descendente = False

        self.carregar_tela("consultar")

    def carregar_tela(self, operacao):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()  # Limpa a área para a próxima operação

        if operacao == "cadastrar":
            self.tela_cadastro()
        elif operacao == "consultar":
            self.tela_consulta()

    # Tela de Cadastro
    def tela_cadastro(self):
        tk.Label(self.frame_principal, text="Cadastro de Cliente", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_principal, text="CPF:").pack()
        self.txtCpf = tk.Entry(self.frame_principal, textvariable=self.cpf_var)
        self.txtCpf.pack()

        tk.Label(self.frame_principal, text="Nome:").pack()
        self.txtNome = tk.Entry(self.frame_principal)
        self.txtNome.pack()

        tk.Label(self.frame_principal, text="Idade:").pack()
        self.txtIdade = tk.Entry(self.frame_principal)
        self.txtIdade.pack()

        btnSalvar = tk.Button(self.frame_principal, text="Cadastrar", command=self.cadastrar_cliente)
        btnCancelar = tk.Button(self.frame_principal, text="Cancelar", command=lambda: self.carregar_tela("consultar"))
        btnSalvar.pack(pady=10)
        btnCancelar.pack(pady=10)

    def limitar_cpf(self, *args):
        cpf = self.cpf_var.get()

        # Limitar a entrada a 11 caracteres numéricos
        if not cpf.isdigit():
            self.cpf_var.set("".join(filter(str.isdigit, cpf)))
        elif len(cpf) > 11:
            self.cpf_var.set(cpf[:11])

    def cadastrar_cliente(self):
        cpf = self.txtCpf.get()
        nome = self.txtNome.get()
        idade = self.txtIdade.get()

        try:
            funcoes.cadastrar_cliente(cpf, nome, idade)
            self.carregar_tela("consultar")  # Volta para a tela de consulta
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

    # Tela de Consulta e Alteração
    def tela_consulta(self):
        tk.Label(self.frame_principal, text="Consulta e Alteração de Clientes", font=("Arial", 14)).pack(pady=10)

        # Campo de busca
        tk.Label(self.frame_principal, text="Buscar Cliente:").pack(pady=5)
        self.entry_busca = tk.Entry(self.frame_principal)
        self.entry_busca.pack()
        
        # Botão para buscar
        btnBuscar = tk.Button(self.frame_principal, text="Buscar", command=self.filtrar_clientes)
        btnBuscar.pack(pady=5)

        

        self.tree = ttk.Treeview(self.frame_principal, columns=("Codigo", "CPF", "Nome", "Idade"), show="headings")
        self.tree.heading("Codigo", text="Código", command=lambda: self.ordenar_por_coluna("Codigo", 0))
        self.tree.heading("CPF", text="CPF", command=lambda: self.ordenar_por_coluna("CPF", 1))
        self.tree.heading("Nome", text="Nome", command=lambda: self.ordenar_por_coluna("Nome", 2))
        self.tree.heading("Idade", text="Idade", command=lambda: self.ordenar_por_coluna("Idade", 3))
        self.tree.column("Codigo", width=10)
        self.tree.column("CPF", width=100)
        self.tree.column("Nome", width=200)
        self.tree.column("Idade", width=10)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Carrega dados no Treeview
        self.carregar_dados_treeview()
        self.ordem_descendente = False
        self.ordenar_por_coluna("Codigo", 0)

        # Botão para Alterar Cliente e Excluir dados
        btnAlterar = tk.Button(self.frame_principal, text="Alterar Selecionado", command=self.alterar_dados_cliente)
        btnAlterar.pack(pady=10)

        btnExcluir = tk.Button(self.frame_principal, text="Excluir Selecionado", command=self.excluir_cliente)
        btnExcluir.pack(pady=10)

    def alterar_dados_cliente(self):
        try:
            item = self.tree.selection()[0]
            codigo, cpf, nome, idade = self.tree.item(item, "values")
            
            # Limpar tela e colocar os campos de alteração
            self.carregar_tela("alterar")
            
            tk.Label(self.frame_principal, text="Atualizar Cliente", font=("Arial", 14)).pack(pady=10)
            tk.Label(self.frame_principal, text="CPF:").pack()
            txtCpf = tk.Entry(self.frame_principal)
            txtCpf.insert(0, cpf)
            txtCpf.pack()

            tk.Label(self.frame_principal, text="Nome:").pack()
            txtNome = tk.Entry(self.frame_principal)
            txtNome.insert(0, nome)
            txtNome.pack()

            tk.Label(self.frame_principal, text="Idade:").pack()
            txtIdade = tk.Entry(self.frame_principal)
            txtIdade.insert(0, idade)
            txtIdade.pack()

            btnSalvar = tk.Button(self.frame_principal, text="Salvar Alterações", command=lambda: self.salvar_alteracao(codigo, txtCpf, txtNome, txtIdade))
            btnCancelar = tk.Button(self.frame_principal, text="Cancelar", command=lambda: self.cancelar_acao())
            btnSalvar.pack(pady=10)
            btnCancelar.pack(pady=10)
            
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione um cliente para alterar.")
        

    def excluir_cliente(self):

        try:
            item = self.tree.selection()[0]
            codigo = self.tree.item(item, "values")[0]

            funcoes.deletar_dados(codigo)
            self.carregar_tela("consultar")  # Volta para a tela de consulta
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione um cliente para excluir.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir: {e}")

    def carregar_dados_treeview(self):
        registros = funcoes.listar_tabela()
        for registro in registros:
            self.tree.insert("", "end", values=registro)

    def filtrar_clientes(self):
        busca = self.entry_busca.get()
        registros = funcoes.listar_tabela()  # Obtém todos os registros

        # Limpa o Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Filtra e exibe os registros que correspondem ao termo de busca
        for registro in registros:
            if busca.lower() in str(registro).lower():  # Filtra por qualquer campo que contenha o termo de busca
                self.tree.insert("", "end", values=registro)

    def salvar_alteracao(self, codigo, txtCpf, txtNome, txtIdade):
        cpf = txtCpf.get()
        nome = txtNome.get()
        idade = txtIdade.get()

        funcoes.alterar_dados(codigo, cpf=cpf if cpf else None,
                  nome=nome if nome else None,
                  idade=int(idade) if idade else None)
        
    
    def ordenar_por_coluna(self, coluna, indice):
        # Extrai os dados do Treeview
        dados = [(self.tree.set(k, coluna), k) for k in self.tree.get_children("")]

        # Verifica a coluna e converte para inteiro para ordenação numérica
        if coluna == "Codigo" or coluna == "CPF" or coluna == "Idade":
            dados.sort(key=lambda t: int(t[0]), reverse=self.ordem_descendente)
        else:
            dados.sort(reverse=self.ordem_descendente, key=lambda t: t[0].lower() if isinstance(t[0], str) else t[0])

        # Alterna a ordem para a próxima vez que a coluna for ordenada
        self.ordem_descendente = not self.ordem_descendente

        # Rearranja os itens do Treeview
        for index, (val, k) in enumerate(dados):
            self.tree.move(k, "", index)


    def cancelar_acao(self):
        self.carregar_tela("consultar")
    