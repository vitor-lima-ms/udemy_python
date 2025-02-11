#Sao variaveis referentes ao sistema operacional --> Temos ambientes locais, de teste e de producao --> Impossivel colocar de forma hard coded informacoes como usuario e senha, uma vez que o sistema sera usado em diferentes ambientes --> Sempre em letras maiusculas
#Para criar variaveis de ambiente temporarias sem utilizar Python:
    #Windows: $env:VARIAVEL="VALOR" | dir env:
    #Mac e Linux: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
#Utilizando Python
    #Para obter o valor das variaveis de ambiente
        #os.getenv ou os.environ['VARIAVEL']
    #Para configurar variaveis de ambiente
        #os.environ['VARIAVEL'] = 'valor'
        #Ou utilizando python-dotenv e o arquivo .env
            #Lembrar que sempre precisamos criar um .env-example

'''import os

print(os.getenv('SENHA')) #Tenho que criar a variavel de ambiente com o ambiente virtual ativado e nao posso matar o terminal, pq ela e temporaria'''

from dotenv import load_dotenv
import os

load_dotenv() #Temos que criar um arquivo .env na raiz do projeto para dps executar essa funcao --> Devemos adicionar .env no gitignore para que esse arquivo nao vai para o github --> Ele contem informacoes de acesso a base de dados etc.
print(os.getenv('DB_PASSWORD'))

'''NUNCA MANDAR O MEU .ENV PRA UM REPOSITORIO. ENVIAR UM .ENV-EXAMPLE'''