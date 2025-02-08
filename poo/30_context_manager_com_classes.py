#Podemos implementar nossos proprios protocolos apenas implementando os dunder methods que o Python vai usar
#Isso e chamado de Duck typing --> Um conceito relacionado com tipagem dinamica, onde o Python nao esta interessado no tipo, mas se alguns metodos existem no seu objeto para que ele funcione de forma adequada
#Para criar um context manager, os metodos __enter__ e __exit__ devem ser implementados
    #O metodo __exit__ recebera a classe de excecao, a excecao e o traceback. Se ele retornar True, excecoes no with serao suprimidas
#O context manager pode ser utilizado para coisas duais como abrir e fechar --> e.g., conectar/desconectar
from pathlib import Path
FILE_PATH = Path(__file__).parent / '30_file.txt'

class MyContextManager:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None
    
    def __enter__(self):
        print('Abrindo arquivo.')
        self._file = open(self.file_path, self.mode)
        return self._file
    
    def __exit__(self, class_excpt, exception_, traceback_):
       print('Fechando o arquivo.')
       self._file.close()
       exception_.add_note('Minha nota.') #Uso mais interessante dos recursos da excecao


       #return True #Significa que o erro foi tratado --> O erro nao vai aparecer na tela
    
with MyContextManager(FILE_PATH, 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n', 'Erro proposital.')
    file.write('Linha 3\n')
    print('Dentro.', file)