#Abstract Base Class (ABCs)
    #ABCs sao usadas como contratos para a definicao de novas classes
    #Elas podem forcar outras classes a criarem metodos concretos
    #Tambem podem ter metodos concretos por elas mesmas --> Metodos que tem corpo
    #@abstractmethods sao metodos que nao tem corpo
    #As regras para classes abstratas com metodos abstratos e que elas nao podem ser instanciadas diretamente
    #Metodos abstratos devem ser implementados nas subclasses
    #Uma classe abstrata em Python tem sua metaclasse sendo ABCMeta
    #E possivel criar @property, @setter, @classmethod, @staticmethod e @method como abstratos --> Para isso, devemos utilizar @abstractmethod como o decorator mais interno

from pathlib import Path
from abc import ABC, abstractmethod
LOG_FILE_PATH = Path(__file__).parent / 'log_file.txt'

class Log(ABC): #Para uma classe ser abstrata, uma das formas e herdar de ABC. Eu tambem poderia importar ABCMeta e herda-la em log --> Log(metaclass=ABCMeta) --> Alem disso, precisa ter pelo menos um metodo abstrato
    @abstractmethod
    def _log(self, msg): #O metodo abstrato DEVE ser implementado nas classes criadas a partir da classe abstrata
        ...
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        self._log(f'Success: {msg}')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

