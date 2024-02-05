from cls_database import IAcessoBase, BibliotecaTinyDb

bibli_db = BibliotecaTinyDb('biblioteca1_db')

membro = {
    'nome':'Gui',
    'hist_emprestimo': []
}

bibli_db.inserir_dados('membros',membro)