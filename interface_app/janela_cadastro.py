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
        
        #Biblioteca obj
        self.bilbli_obj = bibli_obj
        
        #Configurar layout
        self.configurar_layout()
        
        #Criar widget
        self.criar_widgets_membro()
        self.add(self.tab_membro,text='Cadastro Membro')
        
        self.criar_widgets_livro()
        self.add(self.tab_livro,text='Cadastro Livro')
                
        #Posicionamento
        self.grid(row=0, column=0)
    
    def configurar_layout(self):
        self.configure(width=400,height=150)
    
    def criar_widgets_membro(self):
        self.tab_membro = TabMembro(self,self.bilbli_obj)
        
    def criar_widgets_livro(self):
        self.tab_livro = TabLivro(self,self.bilbli_obj)
    
class TabMembro(ttk.Frame):
    def __init__(self,parent_obj:CadastroNotebook,bibli_obj:Biblioteca) -> None:
        super().__init__(parent_obj)
        
        #Atributos
        self.parent_obj = parent_obj
        self.bibli_obj = bibli_obj
        self.novo_membro_nome = tk.StringVar()
        self.wnd_cad_membro_result = tk.StringVar()
        
        #Criar widgets
        self.criar_widgets()
        
        #Posicionar
        self.pack()
        
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

class TabLivro(ttk.Frame):
    def __init__(self,parent_obj:CadastroNotebook,bibli_obj:Biblioteca):
        super().__init__(parent_obj)
        
        #Atributos
        self.parent_obj = parent_obj
        self.bibli_obj = bibli_obj
        
        self.novo_titulo = tk.StringVar()
        self.novo_autor = tk.StringVar()
        self.wnd_cad_livro_result = tk.StringVar()
        
        #Widgets
        self.criar_widgets()
    
    
    def criar_widgets(self):
        #Configurar elementos
        lbl_tituo = ttk.Label(master=self,text='Titulo:')
        tx_in_novo_titulo = ttk.Entry(master=self,textvariable=self.novo_titulo)
        lbl_autor = ttk.Label(master=self,text='Autor:')
        tx_in_novo_autor = ttk.Entry(master=self,textvariable=self.novo_autor)
        
        btn_cad_livro = ttk.Button(master=self,text='Cadastrar Livro',command=self.but_cadastrar_livro)
        lbl_result_livro = ttk.Label(master=self,textvariable=self.wnd_cad_livro_result)
        
        #Posicionar os elementos
        lbl_tituo.grid(row=0,column=0,padx=3,pady=3)
        tx_in_novo_titulo.grid(row=0,column=1,columnspan=2,padx=3,pady=3)
        lbl_autor.grid(row=1,column=0,padx=3,pady=3)
        tx_in_novo_autor.grid(row=1,column=1,columnspan=2,padx=3,pady=3)
        btn_cad_livro.grid(row=2,column=1,columnspan=2,padx=3,pady=3)
        lbl_result_livro.grid(row=3,column=1,columnspan=2,padx=3,pady=3)
    
    #Metodos para cadastro livro na biblioteca
    def but_cadastrar_livro(self):
        novo_livro_inf = {'titulo': self.novo_titulo.get(),'autor':self.novo_autor.get()}
        cad_result = self.bibli_obj.cadastrar_novo_livro(novo_livro_inf)
        self.wnd_cad_livro_result.set(cad_result[1])
        self.novo_autor.set('')
        self.novo_titulo.set('')
        

if __name__ == '__main__':
    print('Este é um modulo e não deve ser executado diretamente')
    print('Executar o app.py')