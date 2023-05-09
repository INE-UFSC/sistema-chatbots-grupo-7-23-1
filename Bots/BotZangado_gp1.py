from Bots.Bot import Bot

class BotZangado_gp1(Bot):
    def __init__(self, nome, comandos = []):
        super().__init__(nome, comandos)
        super().cria_comandos(1,"Bom dia",["BOM DIA PRA QUEM SEU ENERGÚMENO?"])
        super().cria_comandos(2,"Qual o Seu nome",[f"MEU NOME É {self._nome.upper()}, SEU CABEÇA DE TABACO!"])
        super().cria_comandos(3,"Quero um conselho",["NÃO ME ENCHE O SACO E O DE OUTROS QUE TA SUAVE!"])

    @property
    def nome(self):
        return super().nome

    @nome.setter
    def nome(nome):
        super().nome(nome)

    def apresentacao(self):
        return (f"EAE SEU VERME, EU SOU O {self._nome.upper()}!")

    def boas_vindas(self):
        return("PORRA! NÃO ACREDITO QUE TU ME ESCOLHEU!")

    def despedida(self):
        return("FALOU SEU IDIOTA, NÃO VOLTA MAIS TAMBÉM!")
