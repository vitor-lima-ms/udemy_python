#Modulo que fornece funcoes para interagir com o sistema operacional
    #os.path --> Contem funcoes para trabalhar com caminhos de arquivos
    #os.lisdir() --> Pode ser usada para listar os arquivos em um diretorio
    #os.system() --> Permite executar comandos do sistema operacional a partir do codigo Python

'''import os

os.system('clear') #Limpar o terminal

print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)'''

#os.path
'''##Funciona independentemente do sistema operacional
##os.path.join --> Junta strings em um unico caminho --> os.path.join('pasta1', 'pasta2', 'arquivo.txt') --> pasta1/pasta2/arquivo.txt
##os.path.split --> Divide um caminho em uma tupla (diretorio arquivo) --> os.path.split(pasta1/pasta2/arquivo.txt) --> ('pasta1/pasta2', 'arquivo.txt')
##os.path.exists --> Verifica se um caminho especificado existe
##O os.path so trabalha com caminho de arquivos e nao faz nenhuma operacao de entrada/saida com arquivos em si

import os

path = os.path.join('/home/vitor', 'arquivo.txt')
print(path)

directory, file = os.path.split(path)
print(directory, '\t', file)

file_path, file_extension = os.path.splitext(path)
print(file_path, '\t', file_extension)

print(os.path.exists(directory))

print(os.path.abspath('.')) #Camiminho absoluto
print(os.path.basename('/home/vitor/udemy_python')) #Parte final do caminho
print(os.path.dirname('/home/vitor/udemy_python/README.md')) #Diretorio'''

#os.listdir
'''import os

path = '/home/vitor/udemy_python'

print(os.listdir(path))

for item in os.listdir(path): #Nao faz recursao --> So busca um nivel
    item_full_path  = os.path.join(path, item)
    print(item_full_path)
    #continue
    
    if not os.path.isdir(item_full_path):
        continue

    for file in os.listdir(item_full_path):
        print('\t', file)'''

#os.walk
##E uma funcao que permite percorrer uma estrutura de diretorios de maneira recursiva
##Gera uma sequencia de tuplas, onde cada tupla possui tres elementos: o diretorio atual (root), uma lista de subdiretorios (dirs) e uma lista de arquivos do diretorio (files)

'''import os

path = os.path.join('/home', 'vitor', 'udemy_python', 'poo')

count = 0
for root, dirs, files in os.walk(path):
    count += 1
    print(count, root)

    for dir_ in dirs:
        print('\t', count, dir_)

    for file_ in files:
        print('\t\t', count, file_)'''


#os.unlink --> Remove arquivos

#os.path.getsize e os.stat --> Dados de arquivos

'''import os

path = os.path.join('/home', 'vitor', 'udemy_python', 'conceitos')

count = 0
for root, dirs, files in os.walk(path):
    count += 1
    print(count, root)

    for dir_ in dirs:
        print('\t', count, dir_)

    for file_ in files:
        full_path = os.path.join(root, file_)
        #stats = os.stats(full_path) #Outra forma de fazer
        #size = stat.st_size
        size = os.path.getsize(full_path)
        print('\t\t', count, file_, size) #Retorna o tamanho em bytes'''

#os + shutil --> Mover, copiar e apagar arquivos
##Mover/renomear --> shutil.move
##Mover/renomear --> os.rename
##Copiar --> shutil.copy
##Apagar --> os.unlink
##Apagar diretorio recursivamente --> shutil.rmtree

import os
import shutil

#Copiar e mover/renomear
HOME = os.path.expanduser('~') #Retorna a home do usuario
DESKTOP = os.path.join(HOME, '/Desktop')
FOLDER = os.path.join(HOME, 'snap')
COPY_FOLDER = os.path.join(HOME, 'copy_folder')

'''os.makedirs(COPY_FOLDER, exist_ok=True) #Criando a pasta para onde serao copiados os arquivos

for root, dirs, files in os.walk(FOLDER):
    for dir in dirs:
        new_dir_path = os.path.join(root.replace(FOLDER, COPY_FOLDER), dir)

        if '.' not in new_dir_path: #So para nao criar pastas ocultas
            os.makedirs(new_dir_path, exist_ok=True)
    
    for file in files:
        if '.' not in root:
            file_path = os.path.join(root, file) #So para nao criar pastas ocultas
            new_file_path = os.path.join(root.replace(FOLDER, COPY_FOLDER), file) #O replace permite que a estrutura de sub-diretorios seja mantida
            shutil.copy(file_path, new_file_path)'''

##Copiar de uma maneira mais facil mas sem poder alterar coisas no meio do caminho
#shutil.rmtree(COPY_FOLDER, ignore_errors=True)
#shutil.copytree(FOLDER, COPY_FOLDER)

#shutil.move(COPY_FOLDER, '/home/vitor/Desktop') #Mover

#shutil.move('/home/vitor/Desktop/copy_folder', '/home/vitor/Desktop/copy_folder' + 'renamed') #Renomeando

#shutil.rmtree('/home/vitor/Desktop/copy_folderrenamed', ignore_errors=False)