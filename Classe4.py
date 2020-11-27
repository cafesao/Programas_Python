class Livro():
    def __init__ (self, titulo, autor, paginas):
        self.titulo = titulo  
        self.autor = autor
        self.paginas = paginas
        print("O livro foi criado.")
    def __str__ (self):
        return(f"\nTitulo: {self.titulo} \nAutor: {self.autor} \nNumero de Paginas: {self.paginas}\n")

titulo = str(input("Digite o nome do livro: "))
autor = str(input("Digite o nome do autor: "))
paginas = int(input("Digite o numero de paginas: "))
livro1 = Livro(titulo, autor, paginas)
print()
print(livro1)