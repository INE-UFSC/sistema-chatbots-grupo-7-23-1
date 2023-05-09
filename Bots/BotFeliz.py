from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome, comandos = []):
        super().__init__(nome, comandos)
        super().cria_comandos(1,"Bom dia",["Bom diaaaaa!!!! Tudo bem? ","buenas","opa"])
        super().cria_comandos(2,"Qual o Seu nome",[f"Meu nome é {self._nome}, muito prazer, espero poder ajudar!"])
        super().cria_comandos(3,"Quero um conselho",["Gentileza gera gentileza!!"])
        super().cria_comandos(4,"Vamo faze um churrasco",["Bora"])

    @property
    def nome(self):
        return super().nome

    @nome.setter
    def nome(nome):
        super().nome(nome)

    def apresentacao(self):
        return f"Oiii! Meu nome é {self._nome}. Como posso te ajudar?"

    def boas_vindas(self):
        return "Ebaaa!!! Fico mais feliz por ter me escolhido!!"

    def despedida(self):
        return "Você já vai? Espero ter ajudado da melhor forma. Adeus..."

