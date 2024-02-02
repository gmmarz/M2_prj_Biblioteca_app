from app_classes import Biblioteca,Livro,Membro
from db import livros

b1 = Biblioteca()
lst_livros = livros

print('ORIGINAL')
print('-'*30)

livro_info = {'titulo': lst_livros[0].get('titulo'),'autor':lst_livros[0].get('autor')}


for livro in lst_livros:
    b1.cadastrar_novo_livro(livro)



print('Catalago')
print('-'*30)
print(b1.catalago[0].__dict__)

print('Pesquisa')
print('-'*30)
lst_result = b1.pesquisar_livros("l-0006")
print(lst_result[0].__dict__)





