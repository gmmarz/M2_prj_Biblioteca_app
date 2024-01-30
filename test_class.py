from app_classes import Biblioteca,Livro,Membro
from db import livros

b1 = Biblioteca()
lst_livros = livros

print('ORIGINAL')
print('-'*30)

livro_info = {'titulo': lst_livros[0].get('titulo'),'autor':lst_livros[0].get('autor')}

b1.cadastrar_novo_livro(livro_info)

print('Catalago')
print('-'*30)
print(b1.catalago[0].__dict__)




