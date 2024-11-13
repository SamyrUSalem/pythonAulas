#Exemplo de comando para instalar as bibliotecas : pip install requests

import requests #importando a biblioteca que foi instalada

import datetime #Ja vem no python essa biblioteca

import random

response = requests.get("https://leonsedov.github.io/portfolio/") #Estou puxando o codigo fonte do site

print(response.text)



now = datetime.datetime.now()

print("Data e hora : ",now)


numeroAleatorio = random.randint(1,100)

print("Numero: ",numeroAleatorio)