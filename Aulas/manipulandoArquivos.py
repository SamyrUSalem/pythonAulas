from pathlib import Path #Estou importando o pacote Path

caminhoDoArquivo = Path("meus_dados.txt") #Esto definindo o caminho do arquivo,q no caso vai ser o diretorio atual 

dados_para_salvar = ["Pyhton", "C++", "Java"] #Os dados q serão salvos

with caminhoDoArquivo.open(mode='w') as arquivo: #Esto abrindo o arquivo em modo escrita para poder editar caso queira e o for esta sendo usado para q os dados q serão salvos, seja escrito qw nem uma lista, invez de ser um do lado do outro, o 'as' é basicamente falando q vou chamar essa linha de codigo de arquivo
    for item in dados_para_salvar:
        arquivo.write(f"{item}\n")
        
print("Dados Salvos!")

with caminhoDoArquivo.open(mode='r') as arquivo: #O arquvo sera aberto no modo 'r' q seria o de leitura para pdoer pegar osd ados que foram salvos anteriormente
    dadosLidos = arquivo.readlines() #Com o readlines, todos os dados serão lidos e armazenados em uma lista(array)
    
dadosLidos = [linha.strip() for linha in dadosLidos] # O metodo strip ira remover todos os espaçaos em brancos ou quebra de linhas  do inicio e no final de cada linha, dessa foram o texto sera 'limpo' pois pode haver espaços ou quebra de linhas desnecessarias, e o for ira percorrer cada elemento desse array

print(f"Dados lidos : {dadosLidos}")