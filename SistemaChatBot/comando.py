import random as r

class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, id, msg, respostas = []):
        self._id = id
        self._msg = msg
        self._respostas = respostas

    # get id
    @property
    def id(self):
        return self._id
    
    # get mensagem
    @property
    def msg(self):
        return self._msg
    
    @property
    def respostas(self):
        return self._respostas
    
    # retorna uma resposta aleatória
    def getRandomResposta(self):
        ##print(self._respostas)
        ##qntd_comandos = len(self._respostas)
        x= r.randint(0,1)
        return self._respostas[x]

    # adiciona resposta
    def addResposta(self, resposta):
        self._respostas.append(resposta)

    # remove resposta (opcional)
    def delResposta(self, resposta):
        self._respostas.remove(resposta)