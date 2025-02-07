#Usamos a funcao open para abrir um arquivo (ele pode ou nao existir)
#Modos:
    #r (leitura)
    #w (escrita) --> Abre o arquivo e apaga tudo que tiver no arquivo para escrever do 0
    #x (criacao)
    #a (escreve no final) --> append mode --> Nao apaga nada no  arquivo
    #b (binario)
    #t (modo texto)
    #r+ ou w+ (leitura e escrita)
#Context manager --> with (abre e fecha)
#Metodos uteis
    #write e read (escrever e ler)
    #writelines (escrever varias linhas)
    #seek (move o cursor)
    #readline (ler uma linha)
    #readlines (ler varias linhas)
#Introducao ao modulo os
    #os.remove ou unlink --> Apaga o arquivo
    #os.rename --> Renomeia ou move o arquivo --> Passar o caminho antigo e o caminho novo
#Introducao ao modulo json
    #json.dump --> Gera um arquivo json
    #json.load

path = '/home/vitor/udemy_python/arquivos_criados/45_manipulacao_arquivos.txt' #Cria um arquivo na pasta que eu estou. Posso passar um caminho completo

'''file = open(path, 'w') #Nao da pra usar 'r' se o arquivo ainda nao existir

file.close() #Sempre fechar o arquivo ao final'''

#Se usarmos o with, ele ja abre e fecha

'''with open(path, 'w+') as file: #Modo escrita + leitura
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.writelines(
        ('Line 3\n', 'Line 4\n')
    )
    file.seek(0, 0) #Move o cursor para a primeira linha para permitir a leitura
    print(file.readline(), end='') #Essa leitura. Usamos o end para evitar duas quebras de linha (a que o print() da + a da string escrita no arquivo)
    for linha in file.readlines():
        print(linha.strip()) #Remover quebras de linha'''

'''with open(path, 'r') as file:
    print(file.read())'''

#Encoding --> Podemos passar como argumento para evitar erros --> Preferir utf8

#Modulo json
#json --> JavaScript object  notation
#A melhor forma de salvar dicionarios em Python é em arquivos .json
import json

'''pessoa = {
    'nome': 'Vitor',
    'sobrenome': 'Lima',
    'altura': 1.72,
    'numeros_preferidos': (17, 5, 2000),
    'dev': False,
}

with open('/home/vitor/udemy_python/arquivos_criados/dict_json.json', 'w') as file:
    json.dump(pessoa, file, indent=2) #ident para formatar melhor o arquivo''' #Converte tupla em array

#Abrindo um json

with open('/home/vitor/udemy_python/arquivos_criados/dict_json.json', 'r') as file:
    pessoa = json.load(file) #A tupla original vem como uma lista

print(pessoa)
print(type(pessoa))