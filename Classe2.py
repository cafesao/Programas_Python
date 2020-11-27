class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Você adicionou o Livro")
    def imprimir(self, titulo, isbn):
        print(f"Foi criado o livro {self.titulo} com o ISBN {self.isbn}")

titulo = str(input("Digite o nome do livro: "))
isbn = int(input("Digite o codigo ISBN: "))
livro1 = Livro(titulo, isbn)
livro1.imprimir(titulo, isbn)