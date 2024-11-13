def saudacao(nome): #É possivel criar as funções atraves do def
    print(f"Ola {nome}")
    
saudacao("opa")


def soma(a, b):
    return a + b

resultado = soma(5,5)

print(resultado)


def saudacaoPersonalizada(nome):
    print(f"Oi {nome}")

usuario = input("Digite o seu nome: ")
saudacaoPersonalizada(usuario)


def verificarIdade(idade):
    if idade >=18:
        return "maior de idade"
    else:
        return "Menor de Idade"
    
userIdade = int(input("Qual seria a idade? "))

status = verificarIdade(userIdade)

print(f"Então vc é : {status}")