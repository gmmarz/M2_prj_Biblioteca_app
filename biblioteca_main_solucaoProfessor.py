"""
Classes 
Livro
    -id
    -titulo
    -autor
    -disponível(bool)

Membro
    -Numero_membro
    -Nome
    -Historico_livro(Livro[])

Biblioteca
    -Catalago_livros(Livro[])
    -Registro_Membros(Membro[])

    -Adicionar_livro(Livro)
    -Adicionar_membro(Membro)
    -Emprestar_livro(membro,livro)
    -devolver_livro(livro)
    -pesquisar_livros_por_id(id)


"""

class Livro:
    def __init__(self,id:str,titulo:str,autor:str) -> None:
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Membro:
    def __init__(self,numero_membro:str,nome:str) -> None:
        self.numero_membro = numero_membro
        self.nome = nome
        self.historico_livros:list[Livro] = []
    
class Biblioteca:
    def __init__(self) -> None:
        self.catalago_livros : list[Livro] = []
        self.registro_membros : list[Membro] = []

    def adicionar_livro(self, livro:Livro):
        self.catalago_livros.append(livro)
        print(f'O Livro {livro.titulo} adicionado com sucesso.')

    def adicionar_membro(self, membro:Membro):
        self.registro_membros.append(membro)
        print(f'O membro {membro.nome} foi adicionado com sucesso')
    
    def emprestar_livro(self, membro:Membro, livro:Livro):
        if livro.disponivel:
            membro.historico_livros.append(livro)
            livro.disponivel = False
            print(f'O Livro {livro.titulo} foi emprestado ao membro {membro.nome} com sucesso')
        else:
            print(f'O livro {livro.titulo} está indisponível')

    def devolver_livro(self,livro:Livro):
        if not livro.disponivel:
            livro.disponivel = True
            print(f'O livro {livro.titulo}foi devolvido com sucesso')
        else:
            print(f'O livro {livro.titulo} ja se encontra disponível')

    def pesquisar_livros_por_id(self,id:str):
        for livro in self.catalago_livros:
            if livro.id == id:
                return livro
            
# livro1 = Livro('001','Homem de ferro','Marvel')
# livro2 = Livro('002','Alice no pais das maravilhas','Leo Stronda')
# livro3 = Livro('003','Taxi','Teste')

# membro1 = Membro('001','Not')
# membro2 = Membro('002','Guilherme')

biblioteca1 = Biblioteca()
biblioteca2 = Biblioteca()

# biblioteca1.adicionar_livro(livro1)
# biblioteca1.adicionar_livro(livro3)

# biblioteca1.adicionar_membro(membro1)

# biblioteca2.adicionar_livro(membro1)
# biblioteca2.adicionar_membro(membro2)

def opcao_adicionar_livro(Biblioteca:Biblioteca):
    id = input('Digite o id do livro: ')
    titulo = input('Digite o titulo do livro: ')
    autor = input('Digite o autor do livro: ')
    livro = Livro(id,titulo,autor)


while True:
    print('='*30)
    print('1.Adicionar')
    print('0 sair')

    op = int(input('Escolha uma das opcoes'))
    match op:
        case 1:
            opcao_adicionar_livro(biblioteca1)
        case 0:
            break
        case _:
            print("Digite uma opção valida")
            continue

for livro in biblioteca1.catalago_livros:
    print(livro.__dict__)
            


    