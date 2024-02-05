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
            'autor':self.autor,
            'esta_emprestado': self.esta_emprestado
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
        self.devolucao_hist : list[dict] = []
        
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
    
    #Metodos sobre os membros   
    def adicionar_membro(self,novo_membro:Membro) -> None:
        self.membros.append(novo_membro)
        
    def cadastrar_novo_membro(self,membro_info:dict) -> tuple:
        
        proximo_id = self.get_next_id(self.membros)
        if proximo_id == None:
            proximo_id = 'm-0001'
        nome = membro_info.get('nome')
        if nome == None:
            return (False,'Informação necessário para cadastrar membros está incorreta')
        else:
            novo_membro = Membro(proximo_id,nome)
            self.adicionar_membro(novo_membro)
            return (True, f'Membro {novo_membro.nome} cadastrado com sucesso')
    
    def pesquisar_membros(self,valor_pesquisa:str) -> list[Membro]:
        membros_encontrados: list[Membro] = []
        
        for membro in self.membros:
            if valor_pesquisa in membro.id or valor_pesquisa in membro.nome:
                membros_encontrados.append(membro) 
        return membros_encontrados
    
    def adicionar_livro_hist(self,membro_atual:Membro,livro:Livro)->tuple:
        for index, membro in enumerate(self.membros):
            if membro_atual.id == membro.id:
                self.membros[index].hist_livros.append(livro.titulo)
                return (1,f'Histórico membro {membro_atual.nome} atualizado')
        else:
            return (-1,f'Usuário não encontrado')
    
    def listar_membros(self):
       for membro in self.membros:
           print('-'*30)
           print(f'ID:{membro.id}') 
           print(f'Titulo: {membro.id}')
           print(f'Auto:{membro.nome}')
           print(f'Hist livros: {membro.hist_livros}')  
    #---------------------------------------------------------------------
    
    #Metodos sobre livros
    def adicionar_livro_catalago(self,novo_livro:Livro)->None:
        self.catalago.append(novo_livro)
        
    def cadastrar_novo_livro(self, livro_info:dict)->tuple:
                
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
            return (True,f'O livro {novo_livro.titulo} foi cadastrado com sucesso')

    def pesquisar_livros(self,valor_pesquisa:str)->list[Livro]:
        livros_encontrados : list[Livro] = []
        for livro in self.catalago:
            if valor_pesquisa in livro.id or valor_pesquisa in livro.titulo or valor_pesquisa in livro.autor:
                livros_encontrados.append(livro)
        return livros_encontrados
    
    def atulizar_status_livro(self,id_livro:str,foi_emprestado:bool)->None:
        for index,livro in enumerate(self.catalago):
            if id_livro == livro.id:
                self.catalago[index].esta_emprestado = foi_emprestado
                break
    
    def emprestar_livro(self,membro:Membro,livro:Livro)->tuple:
        
        if livro.esta_emprestado:
            return (-1,f'livro {livro.titulo} não está disponível')
        else:
            foi_emprestado = True
            self.atulizar_status_livro(livro.id,foi_emprestado)
            func_result = self.adicionar_livro_hist(membro,livro)
            if func_result[0] == -1:
                return func_result
            else:
                return(1,f'o livro {livro.titulo} foi emprestado para usuário {membro.nome}')
    
    def listar_livros(self):
       for livro in self.catalago:
           print('-'*30)
           print(f'ID:{livro.id}') 
           print(f'Titulo: {livro.titulo}')
           print(f'Auto:{livro.autor}')
           print(f'Está emprestado: {livro.esta_emprestado}')
     
    def devolver_livro(self,data_devo:str,livro:Livro,membro:Membro) ->None:
        self.atulizar_status_livro(livro.id,False)
        dict_devo = {
            'data_devolucao':data_devo,
            'id_livro':livro.id,
            'livro_titulo':livro.titulo,
            'id_membro':membro.id,
            'nome_membro':membro.nome
            }
        self.devolucao_hist.append(dict_devo)
           
   
        

                   
            
