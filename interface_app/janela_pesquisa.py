import tkinter as tk
from tkinter import ttk
from app_classes import Biblioteca, Livro, Membro

class JanelaPesquisa(tk.Toplevel):
    def __init__(self,parent_wnd, bibli_obj:Biblioteca):
        super().__init__(parent_wnd)
        
        #Atributos
        self.parent_wnd = parent_wnd
        self.bibli_obj = bibli_obj
        
        #Configurar janela
        self.configurar_janela('Pesquisa',(900,850))
        
        #Configurar widgets
        self.pesquisa_notebook = PesquisaNotebook(self,bibli_obj)
    
    def configurar_janela(self,titulo:str,size:tuple):
        self.title(titulo)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        
class PesquisaNotebook(ttk.Notebook):
    def __init__(self,parent_wnd:JanelaPesquisa,bibli_obj:Biblioteca):
        super().__init__(parent_wnd)
        
        #Atributos
        self.bibli_obj = bibli_obj
        
        #Configurar layout
        self.configurar_layout()
        
        #Criar widgets
        self.criar_widgets()
        self.add(self.tab_pes_membro,text='Membros')
        self.add(self.tab_pes_livro,text='Livros')
        
        #Posicionamento
        self.grid(row=0, column=0)
        
    def configurar_layout(self):
        self.configure(width=900, height=700)
        
    def criar_widgets(self):
        #Criando Widgets
        self.tab_pes_membro = TabMembroPesquisa(self,self.bibli_obj)
        self.tab_pes_livro = TabLivroPesquisa(self,self.bibli_obj)

#=================================================================================================================
#Classes Membros   
        
class TabMembroPesquisa(ttk.Frame):
    def __init__(self,parent_obj:ttk.Notebook,bilbli_obj:Biblioteca):
        super().__init__(parent_obj)
        
        #Atributos
        self.bibli_obj = bilbli_obj
        
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
        frame_resultado = TabMembroResultado(self,self.bibli_obj)
        frame_menu_acoes = TabMembroMenuAcoes(self,self.bibli_obj,frame_resultado)
        frame_menu_acoes.place(x=0,y=0,relwidth=0.16,relheight=1)
        frame_resultado.place(x=100,y=0,relwidth=1,relheight=1)
        
    def pegar_informacoes_membro(self,tbl_obj:ttk.Treeview):
        lst_membros:list[Membro] = self.bibli_obj.membros
        tbl_obj.delete(*tbl_obj.get_children())
        
        if len(lst_membros)>0:
            for membro in lst_membros:
                tbl_obj.insert('','end',text=membro.id,values=(membro.nome,membro.hist_livros))
                
    def pesquisar_item_membro(self,tbl_obj:ttk.Treeview,item_pesquisa:str):
        lst_result :list[Membro] = self.bibli_obj.pesquisar_membros(item_pesquisa)
        
        tbl_obj.delete(*tbl_obj.get_children())
        
        if len(lst_result)>0:
            for membro in lst_result:
                tbl_obj.insert('','end',text=membro.id,values=(membro.nome,membro.hist_livros))
                
class TabMembroResultado(ttk.Frame):
    def __init__(self,parent_obj:TabMembroPesquisa,bibli_obj:Biblioteca):
        super().__init__(parent_obj)

        #Atributos
        self.parent_obj = parent_obj
        self.bibli_obj = bibli_obj
        self.tree_membros = ttk.Treeview(master=self)
        
        #Configurar layout
        self.configurar_layout()
        
        #Criar widgets
        self.criar_widgets()
        
        #Posicionamento
        self.grid(row=0,column=0)
        
    def criar_widgets(self):
        
        self.tree_membros['columns'] = ('nome','hist_livros')
        self.tree_membros.column('#0',width=100,minwidth=100,anchor='center')
        self.tree_membros.column('nome',width=150,minwidth=150,anchor='center')
        self.tree_membros.column('hist_livros',width=200,minwidth=200,anchor='center')
        
        self.tree_membros.heading('#0',text='id')
        self.tree_membros.heading('nome',text='nome')
        self.tree_membros.heading('hist_livros',text='hist_livros')
        
        self.tree_membros.pack(side='left',fill='both',expand=True)
    
    def configurar_layout(self):
        self.configure(relief='solid',border=1,borderwidth=1)

class TabMembroMenuAcoes(ttk.Frame):
    def __init__(self,parent_obj:TabMembroPesquisa,bibli_obj:Biblioteca,frame_resultado_obj:TabMembroResultado):
        super().__init__(parent_obj)

        #Atributos
        self.parent_obj = parent_obj
        self.bibli_obj = bibli_obj
        self.frame_resultado = frame_resultado_obj
        self.membro_inf_pesquisa = tk.StringVar()
        
        #Configurar layout
        self.configurar_layout()
        
        #Criar widgets
        self.criar_widgets()
        
        #Posicionamento
        # self.place(x=0,y=0,relwidth=0.16,relheight=1)
        
    def criar_widgets(self):
        #configurando os elementos
        btn_pegar_membros_info = ttk.Button(master=self,text='Listar Membros',command=lambda: self.parent_obj.pegar_informacoes_membro(self.frame_resultado.tree_membros))
        lbl_item_pesquisar = ttk.Label(master=self,text='Pesquisa')
        lbl_opcoes_pesquisa = ttk.Label(master=self,text='Id/Nome')
        tx_in_pesquisa = ttk.Entry(master=self,textvariable=self.membro_inf_pesquisa)
        btn_pesquisar_item = ttk.Button(master=self,text='Pesquisar',command=lambda: self.parent_obj.pesquisar_item_membro(self.frame_resultado.tree_membros,self.membro_inf_pesquisa.get()))
        
        #posisionando os elementos
        btn_pegar_membros_info.grid(row=0,column=0)
        lbl_item_pesquisar.grid(row=1,column=0)
        lbl_opcoes_pesquisa.grid(row=2,column=0)
        tx_in_pesquisa.grid(row=3,column=0)
        btn_pesquisar_item.grid(row=4,column=0)
        
    
    def configurar_layout(self):
        self.configure(relief='solid',border=1,borderwidth=1)
        
#========================================================================================================================================
#Classes tab livro
class TabLivroPesquisa(ttk.Frame):
    def __init__(self,parent_obj:ttk.Notebook,bilbli_obj:Biblioteca):
        super().__init__(parent_obj)
        
        #Atributos
        self.bibli_obj = bilbli_obj
        
        #Configurar layout
        self.configurar_layout()
        
        #Criar Widgets
        self.criar_widgets()
        
        #Posicionar
        self.pack(side='left',fill='both')
        
    def configurar_layout(self):
        self.configure(relief='solid',border=1,borderwidth=1)
        
    def criar_widgets(self):
        #Configurando widgets
        frame_resultado = TabLivroResultado(self,self.bibli_obj)
        frame_menu_acoes = TabLivroMenuAcoes(self,self.bibli_obj,frame_resultado)
        frame_menu_acoes.place(x=0,y=0,relwidth=0.16,relheight=1)
        frame_resultado.place(x=100,y=0,relwidth=1,relheight=1)
        
    def pegar_informacoes_livro(self,tbl_obj:ttk.Treeview):
        lst_livros:list[Livro] = self.bibli_obj.catalago
        tbl_obj.delete(*tbl_obj.get_children())
        
        if len(lst_livros)>0:
            for livro in lst_livros:
                tbl_obj.insert('','end',text=livro.id,values=(livro.titulo,livro.autor,livro.esta_emprestado))
                
    def pesquisar_item_livro(self,tbl_obj:ttk.Treeview,item_pesquisa:str):
        lst_result :list[Livro] = self.bibli_obj.pesquisar_livros(item_pesquisa)
        
        tbl_obj.delete(*tbl_obj.get_children())
        
        if len(lst_result)>0:
            for livro in lst_result:
                tbl_obj.insert('','end',text=livro.id,values=(livro.titulo,livro.autor,livro.esta_emprestado))

class TabLivroResultado(ttk.Frame):
    def __init__(self,parent_obj:TabLivroPesquisa,bibli_obj:Biblioteca):
        super().__init__(parent_obj)

        #Atributos
        self.parent_obj = parent_obj
        self.bibli_obj = bibli_obj
        self.tree_livros = ttk.Treeview(master=self)
        
        #Configurar layout
        self.configurar_layout()
        
        #Criar widgets
        self.criar_widgets()
        
        #Posicionamento
        self.grid(row=0,column=0)
        
    def criar_widgets(self):
        
        self.tree_livros['columns'] = ('titulo','autor','emprestado')
        self.tree_livros.column('#0',width=100,minwidth=100,anchor='center')
        self.tree_livros.column('titulo',width=150,minwidth=150,anchor='center')
        self.tree_livros.column('autor',width=200,minwidth=200,anchor='center')
        self.tree_livros.column('emprestado',width=200,minwidth=200,anchor='center')
        
        self.tree_livros.heading('#0',text='id')
        self.tree_livros.heading('titulo',text='titulo')
        self.tree_livros.heading('autor',text='autor')
        self.tree_livros.heading('emprestado',text='emprestado')
        
        self.tree_livros.pack(side='left',fill='both',expand=True)
    
    def configurar_layout(self):
        self.configure(relief='solid',border=1,borderwidth=1)
        
class TabLivroMenuAcoes(ttk.Frame):
    def __init__(self,parent_obj:TabLivroPesquisa,bibli_obj:Biblioteca,frame_resultado_obj:TabLivroResultado):
        super().__init__(parent_obj)

        #Atributos
        self.parent_obj = parent_obj
        self.bibli_obj = bibli_obj
        self.frame_resultado = frame_resultado_obj
        self.livro_inf_pesquisa = tk.StringVar()
        
        #Configurar layout
        self.configurar_layout()
        
        #Criar widgets
        self.criar_widgets()
        
        #Posicionamento
        # self.place(x=0,y=0,relwidth=0.16,relheight=1)
        
    def criar_widgets(self):
        #configurando os elementos
        btn_pegar_livros_info = ttk.Button(master=self,text='Listar livros',command=lambda: self.parent_obj.pegar_informacoes_livro(self.frame_resultado.tree_livros))
        lbl_item_pesquisar = ttk.Label(master=self,text='Pesquisa')
        lbl_opcoes_pesquisa = ttk.Label(master=self,text='Id/Nome/Status')
        tx_in_pesquisa = ttk.Entry(master=self,textvariable=self.livro_inf_pesquisa)
        btn_pesquisar_item = ttk.Button(master=self,text='Pesquisar',command=lambda: self.parent_obj.pesquisar_item_livro(self.frame_resultado.tree_livros,self.livro_inf_pesquisa.get()))
        
        #posisionando os elementos
        btn_pegar_livros_info.grid(row=0,column=0)
        lbl_item_pesquisar.grid(row=1,column=0)
        lbl_opcoes_pesquisa.grid(row=2,column=0)
        tx_in_pesquisa.grid(row=3,column=0)
        btn_pesquisar_item.grid(row=4,column=0)
        
    
    def configurar_layout(self):
        self.configure(relief='solid',border=1,borderwidth=1)
        
        
if __name__ == '__main__':
    print('Este arquivo é um módulo e não deve ser executado diretamente')
    print('Executar app.py')