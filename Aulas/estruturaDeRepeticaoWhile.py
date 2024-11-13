contador = 1

# while (contador <= 5) : #O while ira executar a função repetidas vezes enquanto a condição for verdadeira, nesse caso enquanto a variavel contador for menor ou igual a 5 sera executada, mas quando for maior q 5 o codigo ira parar de repetir
#     print(contador)
#     contador += 1
    
    
senha_correta = '12345'
    
tentativa = ''
    
print("Tente colocar a sua senha!")
    
while (tentativa != senha_correta) : #O sinal de '!=' significa diferente, enquanto a variavel tentativa for diferente q a variavel senha_correta o codigo ser executado repetidas vezes
        tentativa = input("Senha: ")
        if(tentativa != senha_correta) :
            print("Senha esta incorreta")
            
print("Senha Correta!")