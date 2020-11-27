class Livro(): # Cria a classe
    def __init__(self): # Cria o "Construtor" (Função) / Precisa ter a palavra self e o __init__
        self.titulo = 'O Monge e o Executivo' # Chamo a palavra (self) + o atributo 
        self.isbn = 9988888 # Mesma coisa
        print("Construtor chamado para criar um objeto desta classe") #Printa a mensagem quando criar a classe no obj
    def imprime(self): #Cria uma função com a palavra self
        print(f"Foi criado o livro {self.titulo} com o ISBN {self.isbn}")

livro1 = Livro() # Cria o obj e atribui a classe Livro()

print(livro1.titulo) # Printa o atributo que esta na classe Livro() / Atributo = titulo
print(livro1.isbn)   # Printa o atributo que esta na classe Livro() / Atributo = isbn

livro1.imprime()
