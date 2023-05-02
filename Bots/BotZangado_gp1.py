from Bots.Bot import Bot

class BotZangado_gp1(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self._comandos = {
            "Bom dia" : " BOM DIA PRA QUEM SEU ENERGUMENO? ", 
            "Qual o Seu nome": f"MEU NOME É {self.__nome}, SEU CABEÇA DE TABACO", 
            "Quero um conselho" : "NÃO ME ENCHE O SACO E O DE OUTROS Q TA SUAVE"
        }

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome, self):
        self.__nome = nome

    def apresentacao(self):
        return (f"EAE SEU VERME, EU SOU O {self.__nome}")
 
    def mostra_comandos(self):
        return("1 - Bom dia \n2 - Qual o seu nome? \n3 - Quero um conselho \n4 - Adeus")
    
    def executa_comando(self,cmd): 
        if cmd == "1":
            return("Eu te respondo: BOM DIA PRA QUEM SEU ENERGUMENO?")
        elif cmd == "2":
            return(f"Eu te respondo: MEU NOME É {self.__nome}, SEU CABEÇA DE TABACO")
        elif cmd == "3":
            return("Eu te respondo: NÃO ME ENCHE O SACO E O DE OUTROS Q TA SUAVE")
        elif cmd == "4":
            return("Eu te respondo: FALOU SEU IDIOTA, NÃO VOLTA MAIS TAMBÉM")

    def boas_vindas(self):
        return("PORRA! NÃO ACREDITO Q TU ME ESCOLHEU")

    def despedida(self):
        return("FALOU SEU IDIOTA, NÃO VOLTA MAIS TAMBÉM")