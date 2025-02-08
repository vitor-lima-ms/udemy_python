#Abstracao --> Mais um pilar da POO

from pathlib import Path
LOG_FILE_PATH = Path(__file__).parent / 'log_file.txt' #Caminho absoluto da pasta onde esta modulo log.py --> Nesse caso o modulo Path entende que a / antes do nome do arquivo siginifica uma concatenacao

#Logs sao exemplos de classes mixins

class Log: #Generico --> Abstracao
    def _log(self, msg): #Assinatura do metodo --> Nome do metodo, parametros e tipos que ele recebe e todo retorno que ele tem
        raise NotImplementedError('Não use a classe Log diretamente.') #Isso e a abstracao --> Nao queremos que uma pessoa utilize essa classe diretamente
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        self._log(f'Success: {msg}')

class LogFileMixin(Log): #Subclasse para adicionar funcionalidades na heranca multipla --> Nao faz parte da familia dos objetos nas quais ela sera implementada
    def _log(self, msg): #Estamos sobrepondo um metodo, mas a assinatura dele tem que se manter identica --> Precisamos defini-lo nas classes filhas pois na classe mae ele nao faz nada alem de levantar um erro
        formated_msg = f'{msg} ({self.__class__.__name__})' #A mesma msg que sai no print deve ser salva no arquivo do log
        print(f'Salvando arquivo log_file.txt:', formated_msg)
        with open(f'{LOG_FILE_PATH}', 'a') as file:
            file.write(f'{formated_msg}\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})') #Mostra que foi essa subclasse que utilizou determinado metodo

if __name__ =='__main__': #So pra testar diretamente o Log no modulo log
    lp = LogPrintMixin()
    lp.log_error('AnythingE')
    lp.log_success('AnythingS')

    lf = LogFileMixin()
    lf.log_error('AnythingE')
    lf.log_success('AnythingS')
