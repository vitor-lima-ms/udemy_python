import os
import shutil
from pathlib import Path
from zipfile import ZipFile

#Caminhos
ROOT_PATH = Path(__file__).parent
ZIP_PATH = ROOT_PATH / '14_zipfile'
COMPRESSED_PATH = ROOT_PATH / '14_zipfile.zip'
UNCOMPRESSED_PATH = ROOT_PATH / '14_zipfile_descompactado'

#Criando o diretorio da aula
ZIP_PATH.mkdir(exist_ok=True)

#Funcao para zipar os arquivos
def create_files(qtd: int, zip_dir: Path):
    for i in range(qtd): #Criando strings para serem escritas em arquivos.txt
        text = f'arquivo_{i}'

        with open(zip_dir / f'{text}.txt', 'w') as file: #Criando e escrevendo nos arquivos
            file.write(text)

create_files(10, ZIP_PATH)

#Compactando
with ZipFile(COMPRESSED_PATH, 'w') as zip:
    for root, dirs, files in os.walk(ZIP_PATH):
        for file in files: #Para escrever os arquivos na pasta compactada
            zip.write(os.path.join(root, file), file) #O segundo argumento file e para que apenas o arquivo seja zipado na pasta, e nao toda a estrutura de pastas ate o ZIP_PATH

#Lendo uma pasta compactada
with ZipFile(COMPRESSED_PATH, 'r') as zip:
    for file in zip.namelist():
        print(file)

#Descompactando
with ZipFile(COMPRESSED_PATH, 'r') as zip:
    zip.extractall(UNCOMPRESSED_PATH)