import tkinter as tk

class LivroApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Exemplo Tkinter")

        root.geometry("400x200")
        
        # Botão para abrir a tela de Livros
        self.btn_livros = tk.Button(root, text="Livros", command=self.abrir_tela_livros)
        self.btn_membros = tk.Button(root,text="Membros",command=self.abrir_tela_membros)
        self.btn_livros.pack(pady=20)
        self.btn_membros.pack(pady=20)

    def abrir_tela_livros(self):
        # Criar a tela de Livros
        self.tela_livros = tk.Toplevel(self.root)
        self.tela_livros.title("Tela Livros")
        
        self.tela_livros.geometry("400x200")
        
        # Adicionar um label à tela de Livros
        label = tk.Label(self.tela_livros, text="Esta é a tela filha Livros")
        label.pack(pady=20)
        
    def abrir_tela_membros(self):
        # Criar a tela de Livros
        self.tela_membros = tk.Toplevel(self.root)
        self.tela_membros.title("Tela Membros")
        
        self.tela_membros.geometry("400x200")
        
        # Adicionar um label à tela de Livros
        label = tk.Label(self.tela_membros, text="Esta é a tela filha Membros")
        label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = LivroApp(root)
    root.mainloop()
