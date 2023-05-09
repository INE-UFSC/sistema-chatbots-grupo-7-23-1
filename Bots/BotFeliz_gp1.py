from Bots.Bot import Bot

class BotFeliz_gp1(Bot):
    def __init__(self, nome, comandos = []):
        super().__init__(nome, comandos)
        super().cria_comandos(1,"Bom dia",["BOM DIA MEU CONSAGRADO!!"])
        super().cria_comandos(2,"Qual o Seu nome",[f" MEU NOME É {self._nome.upper()}, BONITO NÃO? XD"])
        super().cria_comandos(3,"Quero um conselho",["VIVA UM DIA DE CADA VEZ, A VIDA É BELA, CARPE DIEM!!!"])

    @property
    def nome(self):
        return super().nome

    @nome.setter
    def nome(nome, self):
        super().nome(nome)

    def apresentacao(self):
        return("Mensagem de apresentação: Bom dia meu raio de sol XD")

    def boas_vindas(self):
        return("UHUUUUL, VOCÊ ME ESCOLHEU!!! XD")

    def despedida(self):
        return("ADEUS MEU REI, TENHA UM ÓTIMO DIA, ATÉ UMA PŔOXIMA!! XD")
