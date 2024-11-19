# A biblioteca Pandas é uma das ferramentas mais populares e poderosas para análise e manipulação de dados

import pandas as pd

data = {
    'Nome': ["Jota", "Neide", 'Lua'],
    'Idade': [20, 18, 31],
    'Cidade': ["Manaus", "São Paulo", "Rio de Janeiro"]
}

df = pd.DataFrame(data)  # DataFrame é uma estrutura de dados Bidimensional (igual a uma tabela) com linhas e colunas

print(df)

nomes = df['Nome']  # Dessa forma, estou buscando a coluna Nome
print("\nColuna Nome:\n", nomes)

primeiraLinha = df.iloc[0]  # Dessa maneira, estou buscando a primeira linha que está na tabela
print("\nPrimeira linha:\n", primeiraLinha)

df.to_csv("clientes.csv", index=False) # Estou criando o arquivo CSV com os dados anteriores

print("\nArquivo 'clientes.csv' criado.")

df_csv = pd.read_csv("clientes.csv") # Estou lendo os dados do arquivo CSV

print("\nCSV:\n", df_csv)

cidades = df['Cidade'] # Selecionando a coluna Cidade

print("\nCidades:\n", cidades)

filtro = df_csv[df_csv['Idade'] > 30] # Estou filtrando os clientes com idade maior que 30
print("\nClientes com idade maior que 30:\n", filtro)
