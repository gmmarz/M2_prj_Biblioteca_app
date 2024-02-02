from cls_utilidades import Utilidades

class Item:
    def __init__(self,id:str) -> None:
        self._id = id

    @property
    def id(self) -> str:
        return self._id

class Livro(Item):
    def __init__(self, id:str,titulo:str,autor:str) -> None:
        super().__init__(id)
        self.titulo = titulo
        self.autor = autor
        self._esta_emprestado = False
        
    @property
    def id(self)->str:
        return self._id

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

class Membro(Item):
    def __init__(self,id:str,nome:str) -> None:
        super().__init__(id)
        self.nome = nome
        self.hist_livros = []
        
    @property
    def id(self) -> str:
        return self._id
    
class Biblioteca:
    def __init__(self) -> None:
        self.catalago :list[Livro ]= []
        self.membros :list[Membro]  = []
        
    def get_last_id(self,lst_items:list[Item]) -> str:
        
        lst_ids_str :list[str] = [item.id for item in lst_items]
        lst_ids_num = [id_str.split('-')[1] for id_str in lst_ids_str]
        if lst_ids_str[0].split('-')[0] == 'l':
            prefix = 'l'
        else:
            prefix = 'm'
        ultimo_id = prefix + '-' + str(max(lst_ids_num).zfill(4))
        
        return ultimo_id
    
    def get_next_id(self,lst_items:list[Item]) -> str:
        
        if len(lst_items) == 0:
            return None
        else:
            last_id  = self.get_last_id(lst_items)
            last_id_inf = last_id.split('-')
            next_id_num = int(last_id_inf[1]) + 1
            return last_id_inf[0] +'-'+ str(next_id_num).zfill(4)
    
    def adicionar_livro_catalago(self,novo_livro:Livro) ->None:
        self.catalago.append(novo_livro)
    
    def adicionar_membro(self,novo_membro:Membro) -> None:
        self.membros.append(novo_membro)
        
    def cadastrar_novo_livro(self, livro_info:dict) -> tuple:
                
        if len(self.catalago) == 0:
            proximo_id = 'l-0001'
        else:
            proximo_id = self.get_next_id(self.catalago)
        titulo = livro_info.get('titulo')
        autor = livro_info.get('autor')
        if titulo == None or autor == None:
            return (False,'Umas das informações necessárias para o livro está incorreta')
        else:
            novo_livro = Livro(proximo_id,titulo,autor)
            self.adicionar_livro_catalago(novo_livro)
            return (True,'Cadastrado com sucesso')
    
    def cadastrar_novo_membro(self,membro_info:dict) -> tuple:
        util = Utilidades()
        
        proximo_id = util.get_next_id(self.membros)
        if proximo_id == None:
            proximo_id = 'm-0001'
        nome = membro_info.get('nome')
        if nome == None:
            return (False,'Informação necessário para cadastrar membros está incorreta')
        else:
            novo_membro = Membro(proximo_id,nome)
            self.adicionar_membro(novo_membro)
            return (True, 'Membro cadastrado com sucesso')
       
    def pesquisar_livros(self,valor_pesquisa:str)->list[Livro]:
        livros_encontrados : list[Livro] = []
        for livro in self.catalago:
            if valor_pesquisa in livro.id or valor_pesquisa in livro.titulo or valor_pesquisa in livro.autor:
                livros_encontrados.append(livro)
        return livros_encontrados
   


            
        

        
    
    


        

    
    


    
