#E um tipo de relacao onde os objetos estao ligados dentro do sistema
#Essa e a relacao mais comum entre objetos e tem subconjuntos como agregacao e composicao
#Geralmente, temos uma associacao quando um objeto tem um atributo que referencia outro objeto
#A associacao nao especifica como um objeto controla o ciclo de vida de outro objeto

class Writer:
    def __init__(self, name):
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool
    
    @tool.setter
    def tool(self, value):
        self._tool = value


class WriterTools:
    def __init__(self, name):
        self.name = name
    
    def write(self):
        return f'{self.name} esta escrevendo.'
    
writer = Writer('Vitor')
pen = WriterTools('Caneta BIC')

writer.tool = pen #Associacao de classes --> write e da classe Writer mas seu atributo tool e da classe WriterTools

'''print(pen.write()) #A caneta ainda pode ser usada sozinha pois a associacao e uma conexao fraca
print(writer.tool.write()) #Retorna o mesmo que o print acima --> writer.tool.write() = pen.write()'''

type_writer = WriterTools('Maquina de escrever')
writer.tool = type_writer #Podemos mudar a ferramenta durante o codigo
