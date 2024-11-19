def cadastroClientes(nome, email, telefone):
    with open("clientes.txt", "a") as arquivo: #O "a" significa o mode q sera aberto o arquivo, no caso sera o modo de adicao
        arquivo.write(f"{nome}, {email}, {telefone}\n")
    print("Cadastro realizado!")
    
    
def listaClientes():
    try:
        with open("clientes.txt", "r") as arquivo:
            clientes= arquivo.readlines()
            if not clientes:
                print("Lista Vazia!")
            else:
                print("Clientes cadastrados: ")
                for cliente in clientes:
                    nome, email, telefone = cliente.strip().split(",")
                    print(f"Nome: {nome}, Email: {email}, Telefone: {telefone}")
    except FileNotFoundError:
        print("Nenhum cadastro feito!")
        

def salvarArquivo(dados, arquivoNome):
    with open(arquivoNome, "w") as arquivo:
        for dado in dados:
            arquivo.write(f"{dado}\n")



def lerArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, "r") as arquivo:
            return arquivo.readline()
    except FileNotFoundError:
        return []    


cadastroClientes("Opa","@hotmail.com", "12345")

cadastroClientes("Ola", "@gmail.com", "123456789")

listaClientes()