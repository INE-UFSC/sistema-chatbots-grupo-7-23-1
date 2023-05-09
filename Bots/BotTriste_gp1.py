from Bots.Bot import Bot

class BotTriste_gp1(Bot):
    def __init__(self, nome, comandos = []):
        super().__init__(nome, comandos)
        super().cria_comandos(1,"Bom dia",["Mais um dia de tristeza, bom dia."])
        super().cria_comandos(2,"Qual o Seu nome",[f" Meu nome é {self._nome}, apesar de niguem se importa com isso."])
        super().cria_comandos(3,"Quero um conselho",["Apenas fique no seu quarto chorando."])

    @property
    def nome(self):
        return super().nome

    @nome.setter
    def nome(nome):
        super().nome(nome)

    def apresentacao(self):
        return (" A cada dia a morte se aproxima...Bom dia.")

    def boas_vindas(self):
        return ("Espero que você nao me abandone...")

    def despedida(self):
        return (" Adeus...*sniff*.")