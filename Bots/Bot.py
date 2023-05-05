##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r
from SistemaChatBot.comando import Comando

class Bot(ABC):

    def __init__(self, nome, comandos  = []):
        self._nome = nome
        self._comandos = comandos
    
    def comandos_len(self):
        return len(self._comandos)
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def mostra_comandos(self):
        s = ''
        i = 1
        for key in self._comandos:
            s += f'{i} - {key.msg}\n'
            i += 1
        s += f'{i} - Adeus\n'

        return s

    @abstractmethod
    def apresentacao(self):
        pass

    def executa_comando(self,cmd):
        cmd_i = int(cmd)
        if cmd_i <= 0 or cmd_i > len(self._comandos):
            return self.despedida()
        for i in range(len(self._comandos)):
            if cmd_i == self._comandos[i].id:
                return Comando.getRandomResposta(self._comandos[i])
    
    def cria_comandos(self,id,msg,respostas : list()):
        self._comandos.append(Comando(id,msg,respostas))
    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass
