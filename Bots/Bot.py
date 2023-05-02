##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome):
        self._nome = nome
        self._comandos = {}
    
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
        for key in sorted(self._comandos.keys()):
            s += f'{i} - {key}\n'
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
        return [kv[1] for kv in sorted(self._comandos.items(), key=lambda kv: kv[0])][cmd_i-1]

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass
