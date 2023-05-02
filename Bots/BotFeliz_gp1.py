from Bots.Bot import Bot

class BotFeliz_gp1(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self._comandos = {
            "Bom dia" : " BOM DIA MEU CONSAGRADO!! ", 
            "Qual o Seu nome": f" MEU NOME É {self.__nome}, BONITO NÃO? XD", 
            "Quero um conselho" : "VIVA UM DIA DE CADA VEZ, A VIDA É BELA, CARPE DIEM!!!"
        }

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome, self):
        self.__nome = nome

    def apresentacao(self):
        return("Mensagem de apresentação: Bom dia meu raio de sol XD")
 
    def mostra_comandos(self):
        return("1 - Bom dia \n2 - Qual o seu nome? \n3 - Quero um conselho \n4 - Adeus")
    def executa_comando(self,cmd):
        if cmd == "1":
            return("Eu te respondo: BOM DIA MEU CONSAGRADO!!")
        elif cmd == "2":
            return(f"Eu te respondo: MEU NOME É {self.__nome}, BONITO NÃO? XD")
        elif cmd == "3":
            return("Eu te respondo: VIVA UM DIA DE CADA VEZ, A VIDA É BELA, CARPE DIEM!!! XD")
        elif cmd == "4":
            return("Eu te respondo: ADEUS MEU REI, TENHA UM ÓTIMO DIA, ATÉ UMA PŔOXIMA!! XD")

    def boas_vindas(self):
        return("UHUUUUL, VOCÊ ME ESCOLHEU!!! XD")

    def despedida(self):
        return("ADEUS MEU REI, TENHA UM ÓTIMO DIA, ATÉ UMA PŔOXIMA!! XD")
