import funcoes
import interface

funcoes.criar_tabela()
janela = interface.tk.Tk()
app = interface.App(janela)
janela.mainloop()