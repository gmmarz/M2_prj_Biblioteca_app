from app_classes import Biblioteca,Livro,Membro
from db import livros, membros

def pegar_emprestado(bibli_obj:Biblioteca):
    membro_id = input("Digite id do membro:")
    livro_id = input('Digite id do livro: ')
    
    for index, membro in enumerate(bibli_obj.membros):
        if membro.id == membro_id:
            membro_atual = bibli_obj.membros[index]
            break
    for index, livro in enumerate(bibli_obj.catalago):
        if livro_id == livro.id:
            livro_atual = bibli_obj.catalago[index]
            break
    bibli_obj.emprestar_livro(membro_atual,livro_atual)
        
            

def func_tests(biblioteca_obj:Biblioteca):
    flg_app = True
    while flg_app:
        print('-'*30)
        print('1:Adicionar membro\n2:Listar livros\n3:Listar membros\n4:Emprestar\n5:Sair')
        try:
            op = int(input("Digite uma opção: "))
            match op:
                case 1:
                    pass
                case 2:
                    biblioteca_obj.listar_livros()
                case 3:
                    biblioteca_obj.listar_membros()
                case 4:
                    pegar_emprestado(biblioteca_obj)
                case 5:
                    break
        except ValueError:
            print("Digite apenas umas das opções")

def main():
    b1 = Biblioteca()
    lst_livros = livros
    lst_membros = membros
    
    for livro in lst_livros:
        b1.cadastrar_novo_livro(livro)

    for membro in lst_membros:
        b1.cadastrar_novo_membro(membro)

    func_tests(b1)


if __name__ == '__main__':
    main()









# b1 = Biblioteca()
# lst_livros = livros

# print('ORIGINAL')
# print('-'*30)

# livro_info = {'titulo': lst_livros[0].get('titulo'),'autor':lst_livros[0].get('autor')}


# for livro in lst_livros:
#     b1.cadastrar_novo_livro(livro)



# print('Catalago')
# print('-'*30)
# print(b1.catalago[0].__dict__)

# print('Pesquisa')
# print('-'*30)
# lst_result = b1.pesquisar_livros("l-0006")
# print(lst_result[0].__dict__)