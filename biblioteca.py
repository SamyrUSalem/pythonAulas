from pathlib import Path

caminhoDoArquivo = Path("clientes_biblioteca.txt")

nome = input("Digite seu nome : ")
telefone = input("Digite o Telefone : ")
numeroDoCartao = input("Digite o numero do cartao : ")

with caminhoDoArquivo.open(mode="a") as arquivo: #No mod'a' o arquivo será criado no modo adição, então sera possivele screver algo no final do arquivo mas sem apagar oq tem anteriormente
    arquivo.write(f"{nome}, {telefone}, {numeroDoCartao}\n")
    

print("Cadastrado!")