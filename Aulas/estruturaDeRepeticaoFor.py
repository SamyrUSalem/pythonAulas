frutas = ["Maçã", "Banana", "Cereja"]

for fruta in frutas: #Dessa forma, a variavel fruta ira receber temporariamente os valores do array frutas em cada ciclo do for(daria para fazer algum calculo ou funcionalidade em cada um desses ciclos caso necessario), no caso no primeiro ira receber o valor mação , depois banana, etc... e printar na tela com a estrutura de repetição for, q vai iterar sobre os valores q esta no array
    print(fruta)
    
for i in range(1,11): #Com o range é possivel escolher a quantidade de vez que gostaria q o codigo seja executado, ele começa a contar a partir do 0, se eu coloco o rango apenas 5, sera contado(0,1,2,3,4) q no caso foram 5x, então da forma q coloque sera contado de 1 até 10 pq se colocasse 1,10, iria ser contado ate 9
       print(i) 

for i in range(1,11, 2):   #Dessa forma, sera contado em 2 em 2
       print(i) 
