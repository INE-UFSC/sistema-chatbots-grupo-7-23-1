from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome, comandos = []):
        super().__init__(nome, comandos)
        super().cria_comandos(1,"Bom dia",["Que boas vindas o que não quero voce aqui"])
        super().cria_comandos(2,"Qual o Seu nome",[f"Quer que eu fale denovo? é {self._nome}"])
        super().cria_comandos(3,"Quero um conselho",["Meu conselho: vai embora"])

    @property
    def nome(self):
        return super().nome

    @nome.setter
    def nome(nome):
        super().nome(nome)

    def apresentacao(self):
        return 'Por favor não me escolha'
    
    def boas_vindas(self):
       return 'Não creio que você me escolheu'

    def despedida(self):
        return 'Finalmente vô poder voltar a dormir'
