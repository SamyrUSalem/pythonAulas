from pathlib import Path

caminhaDoCliente = Path("clientesBiblioteca.txt")

caminhoDoLivro = Path("livroClientes.txt")

try: #O sistema ira tentar executar o codigo q esta no try, mas caso haja algume error o except sera acionado e o codigo de tratamento de error sera executado
    with caminhaDoCliente.open() as arquivo:
        linhas = arquivo.readlines()
        numeroCartao = len(linhas) + 1 #caso ja exista um arquvio e com clientes nele, sera gerado um novo numero o len(linnhas) ira pegar o totald e linhas e depois somar com 1, dessa forma sera criado um novo numero de cartao
except FileNotFoundError:
    numeroCartao = 1 #Caso não exista um arquivo, sera criado com o numero 1
    
    
nome = input("Digite seu Nome: ")
telefone = input("digite seu Telefone: ")

with caminhaDoCliente.open(mode='a') as arquivo: #Dessa forma, o arquivo sera aberto no modo de adição,e ira acrescentar os valores abaixo
    arquivo.write(f"{nome}, {telefone}, {numeroCartao}\n")
    
print(f"Cliente cadastrado com sucesso! Numero de cartão : {numeroCartao}")


numeroCartao= int(input("Digite o nuemro do Cartão: "))
livros = input("Digite os livros(separados por virgula): ")

with caminhoDoLivro.open(mode='a') as arquivo: #É feito um arquivo onde tem o numero do cartao do cliente e os livros q foram usados
    arquivo.write(f"{numeroCartao}, {livros}\n")
    
print("Livros adicionados!")


numeroCartao = int(input("Digite o numero do cartao : "))

try:
    with caminhoDoLivro.open() as arquivo:
        linhas = arquivo.readlines()
        encontrou = False #Sera utilizada para indicar se algum registro foi encontrado
        for linha in linhas:
            numCartao, livros = linha.strip().split(',',1) #O método split ira dividir a string em um array, o separador sera uma virgula, e sera feita no maximo uma divisão a primeira parte antes da virgula sera numCartao e tudo q vem depois sera do livros
            if(int(numCartao) == numeroCartao):
                print(f"Livros utilizados: {livros}")
                encontrou = True
        if (not encontrou): #Verifica se a variavel 'encontrou' ainda é False
            print("Nenhum Livro encontrado")
except FileNotFoundError:
    print("Nenhum Registro")

