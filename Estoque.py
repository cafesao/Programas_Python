from random import randint
import copy
import time
import sys
import random
from datetime import datetime 
# Importando as bibliotecas.

resposta = int(1)
identificador = int(999)
produto = {}
produtos_Total = []
resposta_ID = int()
contador = 0
# Definindo as variaveis.

def vizualisarEstoque(produtos_Total, contador_Total):
    print("\n================================================================\n")
    print(f'ID: {produtos_Total[resposta_ID]["id"]}')
    print(f'Nome: {produtos_Total[resposta_ID]["nome"]}')        
    print(f'Quantos produtos foram comprados: {produtos_Total[resposta_ID]["produtos_Compra"]}')
    print(f'Quantos produtos foram vendidos: {produtos_Total[resposta_ID]["produtos_Venda"]}')
    print(f'Preço da compra: R$ {produtos_Total[resposta_ID]["preço_Compra"]}')
    print(f'Preço da venda: R$ {produtos_Total[resposta_ID]["preço_Venda"]}')
    print(f'Quantidade em estoque: {produtos_Total[resposta_ID]["quantidade"]}')
    print(f'Lucro por venda: R$ {produtos_Total[resposta_ID]["lucro"]:.2f}')
    print(f'Lucro total das vendas: R$ {produtos_Total[resposta_ID]["lucro_Total"]:.2f}')
    print(f'Lucro Real (Produto/Preço comprados - Produto/Preço vendidos): R$ {produtos_Total[resposta_ID]["lucro_Real"]:.2f}')
    print(f'Observação: {produtos_Total[resposta_ID]["obs"]}')
    print("\n================================================================\n")
# Defindo uma função que tem como objetivo mostrar o registro do estoque.

while True:
    now = datetime.now()
    now2 = int(round(now.second * now.minute))
    #Defindo o ID.
    try:

        print("""\nBem-vindo ao controle de estoque, o que você deseja? 
[1] Inserir novo produto
[2] Mostrar produto especifico pelo ID
[3] Mostrar todos os produtos
[4] Apagar todos os produtos
[0] Sair 
    """)
        resposta = int(input("\nResposta: "))
        #Pedindo para o user responder o que ele quer.

    except ValueError:
        print("\nVocê digitou algo que não podia, tente novamente.\n\n")
        continue
        #Configurando um erro, caso o valor esteja incorreto.
    while True:
        try:
            if resposta == 1:
                random.seed(now2)
                identificador = int(random.randrange(10000, 99999))
                contador += 1
                produto["id"] = identificador
                produto["nome"] = str(input("Digite o nome do produto: ")).capitalize()
                produto["produtos_Compra"] = int(input("Quantos produtos foram comprados: "))
                produto["produtos_Venda"] = int(input("Quantos produtos foram vendidos: ")) 
                produto["preço_Compra"] = float(input("Qual foi o preço de compra do produto: "))
                produto["preço_Venda"] = float(input("Qual o preço de venda do produto: "))     
                produto["quantidade"] = produto["produtos_Compra"] - produto["produtos_Venda"]
                produto["lucro"] = produto["preço_Venda"] - produto["preço_Compra"]
                produto["lucro_Total"] = produto["produtos_Venda"] * produto["lucro"] 
                produto["lucro_Real"] = (produto["produtos_Venda"] * produto["preço_Venda"]) - (produto["produtos_Compra"] * produto["preço_Compra"])
                produto["obs"] = str(input("Caso queira adicionar uma observação: "))
                produtos_Total.append(produto.copy())
                break
                #Pedindo para o user colocar os dados do produto.

            if resposta == 2:
                if contador == 0:
                    print("\nLista Vazia!\n")
                    break
                    #Mostrar caso a lista estiver vazia.

                contador2 = -1
                print("Por favor selecione qual ID deseja mostrar: \n")
                for produto_Mostrar in produtos_Total:
                    contador2 += 1
                    print(f'{contador2} = {produto_Mostrar["id"]}')
                resposta_ID = int(input("\nQual deseja: "))
                #Pede para o user colocar o numero que ele desaja para mostrar os dados sobre.

                vizualisarEstoque(produtos_Total, resposta_ID) # Chamando a função que mostra o registro.
                break
            if resposta == 3:
                if contador == 0:
                    print("\nLista Vazia!\n")
                    break
                    #Mostrar caso a lista estiver vazia.

                contador_Total = contador 
                while (contador_Total > 0):
                    contador_Total -= 1
                    vizualisarEstoque(produtos_Total, contador_Total) # Chamando a função que mostra o registro.
                break
            if resposta == 4:
                produtos_Total.clear()
                contador = 0
                print("\nApagando lista...")
                time.sleep(1)
                print("\nLista apagada!\n")
                break
                #Apaga a lista com os dados.

            if resposta == 0:
                print("\nObrigado por utilizar o sistema de estoque.")
                exit()
                #Agradecimento e saida do programa.

            else:
                print("Digito invalido, por favor tente novamente\n")
                sys.exit()
                #Mensagem de erro e saida do programa.

        except ValueError:
            print("\nVocê digitou algo que não podia, tente novamente.\n\n")
            continue
            #Mensagem de erro caso o valor esteja incorreto.

        except IndexError:
            print("Você digitou um ID que não existe\n\n")
            continue
            #Mensagem de erro caso o index esteja incorreto.
            