import tkinter as tk
from tkinter import ttk
from app_classes import Biblioteca, Livro, Membro

class JanelaPesquisa(tk.Toplevel):
    def __init__(self,parent_wnd):
        super().__init__(parent_wnd)
        self.configurar_janela('Pesquisa',(600,600))
        
        lbl_teste = ttk.Label(master=self,text='TESTE DE LABEL NA NOVA JANELA de PESQUISA')
        lbl_teste.pack(padx=50,pady=50)
    
    def configurar_janela(self,titulo:str,size:tuple):
        self.title(titulo)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])