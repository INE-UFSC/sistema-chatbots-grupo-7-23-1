import random as r

class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, id, msg, respostas = []):
        self.__id = id
        self.__msg = msg
        self.__respostas = respostas

    # get id
    @property
    def id(self):
        return self.__id
    
    # get mensagem
    @property
    def msg(self):
        return self.__msg
    
    # retorna uma resposta aleatória
    def getRandomResposta(self):
        qntd_comandos = len(self.__respostas)
        x= r.randint(0,qntd_comandos-1)
        return self.__respostas[x]

    # adiciona resposta
    def addResposta(self, resposta):
        self.__respostas.append(resposta)

    # remove resposta (opcional)
    def delResposta(self, resposta):
        self.__respostas.remove(resposta)