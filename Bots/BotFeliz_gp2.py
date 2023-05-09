from Bots.Bot import Bot


class BotFeliz_gp2(Bot):
    def __init__(self, nome, comandos = []):
        super().__init__(nome, comandos)
        super().cria_comandos(1,"Bom dia",["Como posso ajudá-lo?"])
        super().cria_comandos(2,"Qual o Seu nome",[f"Meu nome é {self._nome}."])
        super().cria_comandos(3,"Quero um conselho",["Não tenha medo de ser você mesmo e vá em busca dos seus sonhos."])

    def apresentacao(self):
        return f"Olá, sou o {self._nome} e te amo!!!"
            
    def boas_vindas(self):
        return f"Olá, pessoa maravilhosa. Estou muito feliz que você me escolheu."

    def despedida(self):
        return f"Foi um prazer ajudar!"
