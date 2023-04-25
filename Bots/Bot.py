##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome):
        self._nome = nome
        self._comandos = {}

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def mostra_comandos(self):
        s = ''
        for i, key in enumerate(sorted(self._comandos.keys())):
            s += f'{i+1} - {key}\n'

        return s

    @abstractmethod
    def apresentacao(self):
        pass

    def executa_comando(self,cmd):
        if cmd <= 0 or cmd > len(a):
            return self.despedida()
        return sorted(self._commandos.keys())[cmd-1]

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass
