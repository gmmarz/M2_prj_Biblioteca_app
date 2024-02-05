from tinydb import TinyDB, Query
import os

class IAcessoBase:
    def criar_base(self,nome_base:str) -> None:
        pass
    
    def inserir_dados(self) -> None:
        pass
    
    def atualizar_dados(self) -> None:
        pass
    
    def deletar_dados(self)->None:
        pass
    
    def listar_registros(self,nome_tabela:str) -> list:
        pass
    
    def pesquisar_id(self,nome_tabela:str,id_obj:str)->list:
        pass
    
    def pesquisar_nome(self,nome_tabela:str,nome:str)->list:
        pass
    
    def pesquisar_titulo(self,nome_tabela:str,titulo:str)->list:
        pass
    
    def pesquisar_autor(self,nome_tabela:str,autor:str)->list:
        pass
    
    def pesquiser_emprestimo_status(self,nome_table:str,pesquisa_esta_emprestado:bool)->list:
        pass
    
class BibliotecaTinyDb(IAcessoBase):
    
    def __init__(self,db_nome:str) -> None:
        self.db_nome = db_nome
        self.db_obj:TinyDB = self.criar_base()
        
    def criar_base(self) -> None:
        return TinyDB(f'./database/{self.db_nome}.json', indent=2)
   
    def inserir_dados(self, nome_tabela:str,data:dict) -> None:
        self.db_obj.table(nome_tabela).insert(data)
       
    
    