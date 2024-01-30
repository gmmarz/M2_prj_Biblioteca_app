from db import livros,membros
from cls_utilidades import Utilidades
# l1 = Livros('l001','Senhor dos aneis','J.J.Token')
# l2 = Livros('l002','Robbits','j.j.token')
# print(l1)

# m1_livros =[l1.titulo,l2.titulo]

# m1 = Membros('m001','gui',m1_livros)

# print(m1)

util = Utilidades()

lst_livros = list(livros)


print(lst_livros)

print('-'*30)
print("Ultimo id do livro")
print(util.get_last_id(lst_livros))

print('O próximo id será')
print(util.get_next_id(lst_livros))

print('Verificando logica localizer string')
print(util.check_string_in_dict('HARRY Potter cmo','titulo',lst_livros))


# caso não poder ter mais de um livro com mesmo nome:
#     livro_existe = util.check_string_in_dict(livro_info.get('titulo'),'titulo',self.catalago)
#     if livro_existe:
#         return (True,'Livro já existe na base')





