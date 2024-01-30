Classes 
 -Biblioteca
 -Membro
 -Livros

Relação

1 Biblioteca - N Livros


1 Biblioteca - N Membros

1Membro - N livros 

Exemplo para escrever na base de dados:
===============================================================================================================

from tinydb import TinyDB

class Biblioteca:
    def __init__(self) -> None:
        self.catalago = []
        self.membros = []

    def adicionar_livro(self, novo_livro: Livro) -> None:
        self.catalago.append(novo_livro)

    def adicionar_membro(self, novo_membro: Membro) -> None:
        self.membros.append(novo_membro)

    def save_catalog_to_db(self, db):
        for livro in self.catalago:
            livro.save_to_db(db)

# Exemplo de uso:
biblioteca = Biblioteca()

# Adicione alguns livros ao catálogo
livro1 = Livro(id='1', titulo='Harry Potter', autor='J.K. Rowling')
livro2 = Livro(id='2', titulo='Senhor dos Anéis', autor='J.R.R. Tolkien')

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

# Crie uma instância do TinyDB e adicione o catálogo à base de dados
db = TinyDB('livros_db.json')
biblioteca.save_catalog_to_db(db)
