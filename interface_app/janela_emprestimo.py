import tkinter as tk
from tkinter import ttk
from app_classes import Biblioteca, Livro, Membro

class JanelaEmprestimo(tk.Toplevel):
    def __init__(self,parent_wnd,bibli_obj:Biblioteca):
        super().__init__(parent_wnd)
        self.bibli_obj = bibli_obj
        
        self.configurar_janela('Biblioteca Emprestimo',(400,200))
                
        #Configurar Widgets
        self.emprestar_frame = FrameEmprestimo(self,bibli_obj)

    
    def configurar_janela(self,titulo:str,size:tuple):
        self.title(titulo)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        
class FrameEmprestimo(ttk.Frame):
    def __init__(self,parent_wnd:JanelaEmprestimo,bibli_obj:Biblioteca):
        super().__init__(parent_wnd)
        
        #Atributos
        self.bibli_obj = bibli_obj
        
        self.membro_id = tk.StringVar()
        self.livro_id = tk.StringVar()
        self.emprestimo_result = tk.StringVar()
        
        #Configurar layout
        self.configurar_layout()
        
        #Criar Widgets
        self.criar_widgets()
        
        #Posicionar
        self.pack()
        
    def configurar_layout(self):
        self.configure(relief='solid',border=1,borderwidth=1)
        
    def criar_widgets(self):
        #Configurando widgets
        lbl_titulo_emprestimo = ttk.Label(master=self,text='Emprestimo')
        lbl_membro_id = ttk.Label(master=self,text='id Membro:')
        tx_in_membro_id = ttk.Entry(master=self,textvariable=self.membro_id)
        lbl_livro_id = ttk.Label(master=self,text='id Livro:')
        tx_in_livro_id = ttk.Entry(master=self,textvariable=self.livro_id)
        btn_emprestar = ttk.Button(master=self,text='Emprestar',command=self.emprestar_livro)
        lbl_emprestimo_result = ttk.Label(master=self,textvariable=self.emprestimo_result)
        
        #Posisionamdo
        lbl_titulo_emprestimo.grid(row=0,column=0, columnspan=3)
        lbl_membro_id.grid(row=1,column=0)
        tx_in_membro_id.grid(row=1,column=1)
        lbl_livro_id.grid(row=2,column=0)
        tx_in_livro_id.grid(row=2,column=1)
        btn_emprestar.grid(row=3,column=0,columnspan=3)
        lbl_emprestimo_result.grid(row=4,column=0,columnspan=3)
        
    def emprestar_livro(self):
        self.emprestimo_result.set('')
        result = self.bibli_obj.emprestar_livro(self.membro_id.get(),self.livro_id.get())
        self.emprestimo_result.set(result[1])
        
        



