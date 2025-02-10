#Usamos a pathlib para trabalhar com caminhos, pastas e arquivos de forma que um codigo funcione em Windows, Mac e Linux
#Evita o hard coding
from pathlib import Path

project_path = Path() #Caminho relativo do projeto
project_path.absolute() #Caminho absoluto do projeto

file_path = Path(__file__) #Caminho absoluto do arquivo 07_pathlib.py

parent_folder = file_path.parent #Pasta na qual o arquivo 07_pathlib.py está

parent_parent_folder = parent_folder.parent #Pasta acima da qual o arquivo 07_pathlib.py está

new_file_path = parent_folder / '07_pathlib.txt' #Podemos criar o caminho para uma pasta tambem --> Basta nao passar uma extensao de arquivo na str

home = Path.home() #Obtem a home do sistema

new_file = (parent_folder / '07_pathlib.txt') 
new_file.touch() #Cria esse arquivo
new_file.write_text('Hello World!') #Escreve no arquivo
print(new_file.read_text()) #Exibe o conteudo do arquivo
new_file.unlink() #Apaga o arquivo