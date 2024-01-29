from app_classes import Livros, Membros


l1 = Livros('l001','Senhor dos aneis','J.J.Token')
l2 = Livros('l002','Robbits','j.j.token')
print(l1)

m1_livros =[l1.titulo,l2.titulo]

m1 = Membros('m001','gui',m1_livros)

print(m1)