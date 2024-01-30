# from cls_livro import Livro
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

class Membro:
    def __init__(self,id:str,nome:str) -> None:
        self._id = id
        self.nome = nome
        self.hist_livros = []
    
class Biblioteca:
    def __init__(self) -> None:
        self.catalago = list[Livro]
        self.membros = list[Livro]
    
    def adicionar_livro(self,novo_livro:Livro) ->None:
        self.catalago.append(novo_livro)
    
    def adicionar_membro(self,novo_membro:Membro) -> None:
        self.membros.append(novo_membro)
    
    


        

    
    


    
