from Bots.Bot import Bot

class BotDramatico(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self._comandos = {
            "Bom dia" : "Nunca será um bom dia...", 
            "Qual o Seu nome": f"Eu já te disse meu nome, é {self._nome}, você já esqueceu de mim?", 
            "Quero um conselho" : "Desista, o mundo vai acabar mesmo, nada vale a pena..."
        }

    @property
    def nome(self):
        return super().nome

    @nome.setter
    def nome(nome):
        super().nome(nome)

    def apresentacao(self):
        return f"Oi... Meu nome é {self._nome}. Como posso te ajudar? Não consigo te ajudar. O que queres de mim?"

    def boas_vindas(self):
        return "Por que você me escolheu? Eu não sirvo pra nada, faço tudo errado..."

    def despedida(self):
        return "Você já vai? Não precisa mais de mim? Então, até..."

