#Com os arrays é possível armazenar varios valores dentro de uma variavel, como strings, numeros, booleanos, float, etc...

frutas = ["Maçã", "Banana", "Cereja"] # acontagem começa a partir do 0, maçã =0 , banana= 1 e cereja = 2

print(frutas[0]) #Estou printando o primeiro item do array, no caso maçã

frutas[1] = 'Laranja' #Dessa forma, estou alterando o valor que esta no indice 1(seria a Banana), e agora o valor sera Laranja

frutas.append('Uva') #Dessa forma, sera incluido um valor no array, nesse caso o valor Uva sera incluido no final do array

frutas.remove("Laranja")#Com isso, estou removendo um valor especifico do array

print(frutas)

numeros = [1,2,3,4,5]

mista = [1, "banana", 3.5,True]



while True :
    fruta = input("Digite uma fruta ou sair: ")
    if(fruta.lower() == 'sair') : #A função lower é para deixar o texto em minusculo, caso o usuario queira sair e digite sair, o codigo sera interrompido usando o break
        break
     
    frutas.append(fruta) #Caso o usuario digite uma fruta ou algo q não seja sair, sera armazenado na variavel fruta e enviado para o array frutas
    
print("Lista de Frutas : ") 
for fruta in frutas : #Estou listando os valores que o array frutas possue
    print(fruta)