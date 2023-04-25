from Bots.Bot import Bot

class BotDramatico(Bot):
    def __init__(self):
        super().__init__()
        self.__comando = {"Bom dia" : "Nunca será um bom dia...", 
                          "Qual o Seu nome": "Eu já te disse meu nome, é Josemildo, você já esqueceu de mim?", 
                          "Quero um conselho" : "Desista, o mundo vai acabar mesmo, nada vale a pena..."}

    @property
    def nome(self):
        return super.nome

    @nome.setter
    def nome(nome):
        super.nome(nome)

    def apresentacao_dramatica(self):
        return "Oi... Meu nome é Josemildo. Como posso te ajudar? Não consigo te ajudar. O que queres de mim?"
    
    def executa_comando(self,cmd):
        return super.executa_comando(cmd)

    def boas_vindas_dramatica(self):
        return "Por que você me escolheu? Eu não sirvo pra nada, faço tudo errado..."

    def despedida_dramatica(self):
        return "Você já vai? Não precisa mais de mim? Então, até..."
