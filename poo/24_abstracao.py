#Abstract Base Class (ABCs)
    #ABCs sao usadas como contratos para a definicao de novas classes
    #Elas podem forcar outras classes a criarem metodos concretos
    #Tambem podem ter metodos concretos por elas mesmas --> Metodos que tem corpo
    #@abstractmethods sao metodos que nao tem corpo
    #As regras para classes abstratas com metodos abstratos e que elas nao podem ser instanciadas diretamente
    #Metodos abstratos devem ser implementados nas subclasses
    #Uma classe abstrata em Python tem sua metaclasse sendo ABCMeta
    #E possivel criar @property, @setter, @classmethod, @staticmethod e @method como abstratos --> Para isso, devemos utilizar @abstractmethod como decorator mais interno