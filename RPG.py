print("Bem Vindo!") 

inventario = []

while True :
    print("\n1 - ir a cabana") #Com o '\n' sera pulado uma linha 
    print("2 - ir para a floresta") 
    print("3 - Ver Inventario") 
    print("4 - Sair") 

    escolha = int(input("Escolha uma opção: "))

    if (escolha == 1 ) :
        print("1- Pegar a espada ") 
        print("2- Ignorar a espada ")
        print("3- Voltar ")
        
        espada = int(input("Qual ira escolher ? "))
        
        if(espada ==1 ) : #Mostrando que é possível inserir condicionais dentro de condicionais
            inventario.append("Espada")
            print("Pegou a espada")
        elif(espada == 2) :
            print("Ignorou")
        elif(espada == 3) :
            print("Voltou"),
        else :
            print("Opção inválida")
    elif(escolha == 2) : #O elif é usado para poder incluir mais condições no sistema, igual como o if q tambem pode incluir uma condição no começo do sistema
        print("Você entrou na floresta")
    elif(escolha == 3) :
        print("Inventario: ")
        for item in inventario :
           print(f"Itens : {item}") #Dessa forma, usando o 'f' no começo é possivel escolher a posição da variavel q deseja colocar usando as chaves e não é necessário colcoar ',' e o nome da variavel depois
    else :
        print("Saiu")
        break