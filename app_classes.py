from dataclasses import dataclass,field

@dataclass
class Livros:
    id_livro : str
    titulo : str
    autor: str
    esta_emprestado: bool = False
    
@dataclass
class Membros:
    id_membro: str
    nome: str
    hist_livros: list = field(default_factory=list)
    


    
