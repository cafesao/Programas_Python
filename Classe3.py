class Circulo():
    pi = 3.14

    def __init__(self, raio = 2):
        self.raio = raio
        print("\nCirculo criado!\n")
    def adicionarRaio(self, novo_raio):
        self.raio = novo_raio
    def verRaio(self):
        return self.raio
    def calcularArea(self):
        return (self.raio * self.raio) * Circulo.pi

verificador = int(0)
print("\nBem vindo ao criador de circulo!\n")
while True:
    print("""Veja as opções abaixo e selecione qual deseja:\n 
[1] Criar o Circulo
[2] Adicionar um novo raio ao circulo
[3] Ver o raio do circulo
[4] Calcular Area do Circulo
[0] Sair""")
    resposta = int(input("\nOpção: "))
    while True:
        if resposta == 1:
            if verificador == 1:
                print("Circulo ja criado!\n")
                break
            resposta_if = str(input("Deseja adicionar o raio ou não? (Padrão do raio = 2): ")).split()[0].upper()
            verificador = 1
            if resposta_if == 'S':
                raio = int(input("Digite o valor do raio: "))
                circulo1 = Circulo(raio)
                break
            else:
                circulo1 = Circulo()
                break
        if resposta == 2:
            raio = int(input("Digite o valor do raio: "))
            circulo1.adicionarRaio(raio)
            print("\nRaio adicionado!\n")
            break
        if resposta == 3:
            print(f"\nRaio: {circulo1.verRaio()}\n")
            break
        if resposta == 4:
            print(f"Área: {circulo1.calcularArea()}\n")
            break
        if resposta == 0:
            print("Obrigado por utilizar o programa.")
            exit()