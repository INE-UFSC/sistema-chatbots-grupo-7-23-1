from Bots.Bot import Bot

class BotZangado_gp3(Bot):
    def __init__(self, nome, comandos = []):
        super().__init__(nome, comandos)
        super().cria_comandos(1,"Por que vocẽ é bravo assim?",["Como assim bravo?! Eu estou completamente calmo!"])
        super().cria_comandos(2,"O que você gosta de fazer?",[f"Há uma série de coisas que gosto de fazer. Entretanto, falar com você com certeza não é uma delas!"])
        super().cria_comandos(3,"Não fale assim comigo!",["Eu falo do jeito que eu quiser!"])

    def apresentacao(self):
        return f"Mau dia! Eu sou o {self.nome}, quem ousa me incomdodar!?"

    def boas_vindas(self):
        return "Diga logo o que você quer!"

    def despedida(self):
        return "Até que enfim vou embora!"
