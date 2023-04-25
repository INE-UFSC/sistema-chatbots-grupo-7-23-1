from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self._comandos={   
            "Boas vindas": "Que boas vindas o que não quero voce aqui",
            "Qual o seu nome": f"Quer que eu fale denovo? é {self._nome}",
            "Quero um conselho": "Meu conselho: vai embora",
        }

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
