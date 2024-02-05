import tkinter as tk
from tkinter import ttk
from app_classes import Biblioteca,Membro,Livro,Item

class BibliotecaAPP:
    def __init__(self, biblioteca:Biblioteca) -> None:
        
        self.bibli_obj = biblioteca
        
        self.root = tk.Tk()
        
        self.novo_membro_nome = tk.StringVar()
        self.novo_titulo = tk.StringVar()
        self.novo_autor = tk.StringVar()
        self.wnd_cad_membro_result = tk.StringVar()
        self.wnd_cad_livro_result = tk.StringVar()
        
        self.configurar_main_wnd()
        self.bibli_main_wnd()
        
    def configurar_main_wnd(self):
        self.root.title('Biblioteca')
        self.root.geometry('400x300')
        
    def configurar_child_wnd(self,wnd_nome:tk.Toplevel):
        wnd_nome.geometry('400x300')
    
    #Janela principal
    #-------------------------------------------------------------------------------------------    
    def bibli_main_wnd(self) -> None:
        
        #Criando elementos pagina home
        btn_open_cadastro = ttk.Button(self.root, text='Cadastro', command=self.abrir_cadastro_wnd)
        
        #Mostrando elementos
        btn_open_cadastro.pack(pady= 10)
    
    #Janelas
    #---------------------------------------------------------------------------------------------------------
    #Janela de cadastro livro e membro
    def abrir_cadastro_wnd(self):
        cadastro_wnd = tk.Toplevel(self.root)   
        cadastro_wnd.title('Biblioteca cadastro')
        self.configurar_child_wnd(cadastro_wnd)
        
        #Conteúdo cadastro
        cadastro_notebook = ttk.Notebook(cadastro_wnd,width=320,height=190)
        
        tab_cad_membro = tk.Frame(cadastro_notebook,relief='solid',borderwidth=1,width=1)
        tab_cad_livro = tk.Frame(cadastro_notebook,relief='solid',borderwidth=1,width=1)
        
        #Tab cadastro membro:
        #config elementros
        lbl_nome = ttk.Label(tab_cad_membro,text='Nome:')
        tx_in_novo_nome = ttk.Entry(tab_cad_membro,textvariable=self.novo_membro_nome)
        lbl_result = ttk.Label(tab_cad_membro,textvariable=self.wnd_cad_membro_result)
        btn_cad_membro = ttk.Button(tab_cad_membro,text='Cadastrar membro',command=self.but_cadastrar_membro)
        btn_cad_clear_membro_wnd = ttk.Button(tab_cad_membro,text='Novo Cadastro',command=self.but_clear_membro_wnd)
        
        #Mostrando elementos:
        lbl_nome.grid(row=0,column=0)
        tx_in_novo_nome.grid(row=0,column=1)
        btn_cad_clear_membro_wnd.grid(row=2,column=0)
        btn_cad_membro.grid(row=2,column=1)
        lbl_result.grid(row=3,column=0,columnspan=2)
        
        #Tab cadastro livro:
        #config elementos
        lbl_titulo = ttk.Label(tab_cad_livro,text='Titulo:')
        tx_in_novo_titulo = ttk.Entry(tab_cad_livro,textvariable=self.novo_titulo)
        lbl_autor = ttk.Label(tab_cad_livro,text='Autor:')
        tx_in_novo_autor = ttk.Entry(tab_cad_livro,textvariable=self.novo_autor)
        btn_cad_livro = ttk.Button(tab_cad_livro,text='Cadastrar livro', command=self.but_cadastrar_livro)
        lbl_cad_livro_result = ttk.Label(tab_cad_livro,textvariable=self.wnd_cad_livro_result)

        #Mostrando elementos
        lbl_titulo.grid(row=0,column=0)
        tx_in_novo_titulo.grid(row=0,column=1)
        lbl_autor.grid(row=1,column=0)
        tx_in_novo_autor.grid(row=1,column=1)
        btn_cad_livro.grid(row=2,column=1)
        lbl_cad_livro_result.grid(row=3,column=0,columnspan=2)
        
        #Exbir contúdo tela de cadastro
        cadastro_notebook.add(tab_cad_membro,text='Cadastro Membro')
        cadastro_notebook.add(tab_cad_livro,text='Cadastro Livro')
        
        cadastro_notebook.pack()
        
    #==========================================================================================================
    
    #Funcções de botões da tela de cadastro.
    def but_cadastrar_membro(self):
        novo_membro_inf ={'nome':self.novo_membro_nome.get()} 
        cad_result = self.bibli_obj.cadastrar_novo_membro(novo_membro_inf)
        self.wnd_cad_membro_result.set(cad_result[1])
        self.novo_membro_nome.set('')
    
    def but_clear_membro_wnd(self):
        self.novo_membro_nome.set('')
        self.wnd_cad_membro_result.set('')
        
    def but_cadastrar_livro(self):
        novo_livro_inf ={'titulo':self.novo_titulo.get(),'autor':self.novo_autor.get()} 
        cad_result = self.bibli_obj.cadastrar_novo_livro(novo_livro_inf)
        self.wnd_cad_livro_result.set(cad_result[1])
        self.novo_autor.set('')
        self.novo_titulo.set('')
    #********************************************************
    
        
    def run_app(self):
        self.root.mainloop()  
        
def main():
    
    b1 = Biblioteca()
    
    app = BibliotecaAPP(b1)
    app.run_app()
    
     

if __name__ == '__main__':
    main()
    
    
    
#Dica para estilizar
        
        # self.style = ttk.Style()
        # self.style.theme_create(
        #     'BibliotecaTheme',parent='alt',settings={
        #         'TNotebook':{'configure':{'tabmargins':[2,5,2,0]}},
        #         'TNotebook.Tab':{
        #             'configure':{'padding':[5,1],'background':'#475C7A'},
        #             'map':{'background':[('selected','#305F72')],
        #                    'expand':[('selected',[1,1,1,0])]}
        #         }
        #     }
        # )
        # self.style.theme_use('BibliotecaTheme')
