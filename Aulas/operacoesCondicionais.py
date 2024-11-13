senha = int(input("Digite a Senha: "))

verifique = int(input("Repita a Senha: "))

if (senha == verifique) : #Estou realizando uma verificação usando o if else, quando coloco '==' estou verificando se a senha é igual ao verifique, ai coloco os dois pontos e depois insiro oq quero q aconteça caso seja, ou oq oquero q aconteça caso n seja usando o else
    print("Senha correta")
    
else :
    print("Senha incorreta")
    
    
    
print("Bem Vindo!") 
print("1 - ir a cabana") 
print("2 - ir para a floresta") 
print("3 - Sair") 

escolha = int(input("Escolha uma opção: "))

if (escolha == 1 ) :
    print("1- Pegar a espada ") 
    print("2- Ignorar a espada ")
    print("3- Voltar ")
    
    espada = int(input("Qual ira escolher ? "))
    
    if(espada ==1 ) : #Mostrando que é possível inserir condicionais dentro de condicionais
        print("Pegou a espada")
    elif(espada == 2) :
        print("Ignorou")
    elif(espada == 3) :
        print("Voltou"),
    else :
        print("Opção inválida")
elif(escolha == 2) : #O elif é usado para poder incluir mais condições no sistema, igual como o if q tambem pode incluir uma condição no começo do sistema
    print("Você entrou na floresta")
else :
    print("Saiu")