import tkinter as tk
from tkinter import ttk
from interface_app.janela_cadastro import JanelaCadastro
from interface_app.janela_pesquisa import JanelaPesquisa
from app_classes import Biblioteca,Membro,Livro,Item
# from db import livros,membros

class BibliotecaApp(tk.Tk):
    def __init__(self, biblioteca_obj:Biblioteca, wnd_titulo:str,size:tuple) -> None:
        
        #Configuração 
        super().__init__()
        self.bibli_obj = biblioteca_obj
        self.configurar_app_wnd(wnd_titulo,size)
        
        # #Variáveis dinamicas
        # self.novo_membro_nome = tk.StringVar()
        # self.novo_titulo = tk.StringVar()
        # self.novo_autor = tk.StringVar()
        # self.wnd_cad_membro_result = tk.StringVar()
        # self.wnd_cad_livro_result = tk.StringVar()
        
        #Widgets
        self.menu = MainMenu(self)
        
        #Rodando o APP
        self.mainloop()
        
    def configurar_app_wnd(self,wnd_titulo:str,size:tuple):
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        self.title(wnd_titulo)
        
    def abrir_janela_cadastro(self):
        janela_cadastro = JanelaCadastro(self,self.bibli_obj)
    
    def abrir_janela_pesquisa(self):
        janela_pesquisa = JanelaPesquisa(self)
 
class MainMenu(ttk.Frame):
    def __init__(self,parent:BibliotecaApp):
        super().__init__(parent)
        self.parent = parent
        self.pack()
        self.criar_widgets()
        
    def criar_widgets(self):
        
        #Criando os wifgets
        btn_open_cadastro = ttk.Button(master=self,text='Cadastro',command= self.parent.abrir_janela_cadastro)
        btn_open_pesquisa = ttk.Button(master=self,text='Pesquisar', command= self.parent.abrir_janela_pesquisa)   

        #Posicionando
        #Criando as colunas
        self.columnconfigure((0,1,2), weight=1,uniform='a')
        self.rowconfigure((0,1,2,3,4),weight=1,uniform='a')
        btn_open_cadastro.grid(row=2,column=0, columnspan=2)
        btn_open_pesquisa.grid(row=3,column=0, columnspan=2)
        
b1 = Biblioteca()       
BibliotecaApp(b1,'TestClassAPP',(400,200))