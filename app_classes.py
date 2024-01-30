from cls_utilidades import Utilidades

class Livro:
    def __init__(self, id:str,titulo:str,autor:str) -> None:
        self._id = id
        self.titulo = titulo
        self.autor = autor
        self._esta_emprestado = False

    @property
    def esta_emprestado(self) -> bool:
        return self._esta_emprestado
    
    @esta_emprestado.setter
    def esta_emprestado(self, novo_status:bool):
        self._esta_emprestado = novo_status
        
    def to_dict(self) -> dict:
        dict_livro = {
            'id':self._id,
            'titulo': self.titulo,
            'autor':self.autor
        }
        return dict_livro

class Membro:
    def __init__(self,id:str,nome:str) -> None:
        self._id = id
        self.nome = nome
        self.hist_livros = []
    
class Biblioteca:
    def __init__(self) -> None:
        self.catalago = []
        self.membros  = []
    
    def adicionar_livro_catalago(self,novo_livro:Livro) ->None:
        self.catalago.append(novo_livro)
    
    def adicionar_membro(self,novo_membro:Membro) -> None:
        self.membros.append(novo_membro)
        
    def cadastrar_novo_livro(self, livro_info:dict) -> tuple:
        util = Utilidades()
        
        proximo_id = util.get_next_id(self.catalago)
        if proximo_id == None:
            proximo_id = 'l-0001'
        titulo = livro_info.get('titulo')
        autor = livro_info.get('autor')
        if titulo == None or autor == None:
            return (False,'Umas das informações necessárias para o livro está incorreta')
        else:
            novo_livro = Livro(proximo_id,titulo,autor)
            self.adicionar_livro_catalago(novo_livro)
            return (True,'Cadastrado com sucesso')
    

            
        

        
    
    


        

    
    


    
