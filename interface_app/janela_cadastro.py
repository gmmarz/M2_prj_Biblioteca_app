import tkinter as tk
from tkinter import ttk
from app_classes import Biblioteca, Livro, Membro

class JanelaCadastro(tk.Toplevel):
    def __init__(self,parent_wnd,bibli_obj:Biblioteca):
        super().__init__(parent_wnd)
        self.bibli_obj = bibli_obj
        
        self.configurar_janela('Biblioteca cadastro',(400,200))
                
        #Configurar Widgets
        self.cadastro_notebook = CadastroNotebook(self,bibli_obj)

    
    def configurar_janela(self,titulo:str,size:tuple):
        self.title(titulo)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
     

class CadastroNotebook(ttk.Notebook):
    def __init__(self,parent_wnd:tk.Toplevel,bibli_obj:Biblioteca):
        super().__init__(parent_wnd)
        
        self.bilbli_obj = bibli_obj
                
        self.pack()
        
        self.criar_widgets()
        
        self.add(self.tab_cadastro,text='Cadastro Membro')
    
    def criar_widgets(self):
        self.tab_cadastro = TabCadastro(self,self.bilbli_obj)
    
class TabCadastro(ttk.Frame):
    def __init__(self,parent_obj:CadastroNotebook,bibli_obj:Biblioteca) -> None:
        super().__init__(parent_obj)
        self.parent_obj = parent_obj
        
        self.novo_membro_nome = tk.StringVar()
        self.wnd_cad_membro_result = tk.StringVar()
        
        self.pack()
        self.criar_widgets()
        
    def criar_widgets(self):
        
        lbl_nome = ttk.Label(self,text='Nome:')
        tx_in_novo_nome = ttk.Entry(self,textvariable=self.novo_membro_nome)
        lbl_result = ttk.Label(self,textvariable=self.wnd_cad_membro_result)
        btn_cad_membro = ttk.Button(self,text='Cadastrar membro',command=self.but_cadastrar_membro)
        btn_cad_clear_membro_wnd = ttk.Button(self,text='Novo Cadastro',command=self.but_clear_membro_wnd)
        
        #Mostrando elementos:
        lbl_nome.grid(row=0,column=0)
        tx_in_novo_nome.grid(row=0,column=1)
        btn_cad_clear_membro_wnd.grid(row=2,column=0)
        btn_cad_membro.grid(row=2,column=1)
        lbl_result.grid(row=3,column=0,columnspan=2)
    
    #Funcções de botões da tela de cadastro.
    def but_cadastrar_membro(self):
        novo_membro_inf ={'nome':self.novo_membro_nome.get()} 
        cad_result = self.bibli_obj.cadastrar_novo_membro(novo_membro_inf)
        self.wnd_cad_membro_result.set(cad_result[1])
        self.novo_membro_nome.set('')   
    
    def but_clear_membro_wnd(self):
        self.novo_membro_nome.set('')
        self.wnd_cad_membro_result.set('')
        