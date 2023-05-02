from Bots.Bot import Bot

class BotTriste_gp1(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self._comandos = {
            "Bom dia" : "Mais um dia de tristeza, bom dia.", 
            "Qual o Seu nome": f" Meu nome é {self.__nome}, apesar de niguem se importa com isso", 
            "Quero um conselho" : "Apenas fique no seu quarto chorando."
        }

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome, self):
        self.__nome = nome

    def apresentacao(self):
        return (" A cada dia a morte se aproxima...Bom dia.")

    def mostra_comandos(self):
        return ("1 - Bom dia \n2 - Qual o seu nome? \n3 - Quero um conselho \n4 - Adeus")

    def executa_comando(self, cmd):
        if cmd == "1":
            return ("Eu te respondo: Mais um dia de tristeza, bom dia.")
        elif cmd == "2":
            return (f"Eu te respondo: Meu nome é {self.__nome}, apesar de niguem se importa com isso")
        elif cmd == "3":
            return ("Eu te respondo: Apenas fique no seu quarto chorando.")
        elif cmd == "4":
            return ("Eu te respondo: Adeus...*sniff*.")

    def boas_vindas(self):
        return ("diz: Espero que você nao me abandone")

    def despedida(self):
        return (" Adeus...*sniff*.")