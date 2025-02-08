#Polimorfismo e um principio que permite que classes derivadas de uma mesma superclasse tenham metodos iguais (mesma assinatura) mas comportamentos diferentes
#Assinatura do metodo (definicao academica) --> Mesmo nome e quantidade de parametros --> return nao faz parte da assinatura
#Assinatura do metodo (opniao do prof) --> Mesmo nome, quantidade de parametros e return
    #SO'L'ID --> Principios da POO
        #L --> Principio da substituicao de Liskov
            #Objetos de uma superclasse devem ser substituiveis por objetos de uma subclasse sem quebrar a aplicacao
            #Sobrecarga de metodos (overload) = Python nao suporta
            #Sobreposicao de metodos (override) = Python suporta

from abc import ABC, abstractmethod

class Notifications(ABC): #Notificacao, na vida real, e uma coisa de certa forma abstrata. Logo, no nosso programa, vamos modela-la assim
    def __init__(self, msg):
        self.msg = msg
    
    @abstractmethod
    def send(self) -> bool: #Apenas uma forma de comunicar o tipo que sera retornado
        ...

class Email(Notifications):
    def send(self):
        print('Enviando E-mail:', self.msg)
        return True #Temos que colocar um retorno desse tipo para respeitar o principio de Liskov --> Na classe abstrata, informamos que o metodo send retorna um bool

class SMS(Notifications):
    def send(self):
        print('Enviando SMS:', self.msg)
        return True

email_ntf = Email('Test')
sms_ntf = SMS('Test')

'''email_ntf.send()
sms_ntf.send()'''

#O que foi feito acima e quase um polimorfismo. Agora vamos realmente fazer um polimorfismo

def send_notifications(notification: Notifications): #Uma notacao para informar que o tipo recebido pela funcao deve ser da classe Notifications
    notification_sent = notification.send()

    if notification_sent:
        print('Notificação enviada.')
    else:
        print('Notificação não enviada.')

send_notifications(email_ntf) #Aqui esta o polimorfismo --> Podemos passar tanto objetos da classe Email quanto da classe SMS
send_notifications(sms_ntf)