from Bots.Bot import Bot

class BotTriste_gp4(Bot):
    def __init__(self, nome, comandos = []):
        super().__init__(nome, comandos)
        super().cria_comandos(1,"Bom dia",["Queria eu que fosse um bom dia..."])
        super().cria_comandos(2,"Qual o Seu nome",[f"Normalmente me chamam de idiota, burro... Mas meu nome verdadeiro é {self._nome}."])
        super().cria_comandos(3,"Quero um conselho",["Também estou precisando, mas até agora nada :c"])

    @property
    def nome(self):
        return super().nome

    @nome.setter
    def nome(nome):
        super().nome(nome)

    def apresentacao(self):
        return f":( Meu nome é {self._nome}, seja bem vindo, eu acho... :c"
 
        '''elif (cmd == '4'):
            print(self.nome, "diz: voce disse 'Adeus'")
            print("Eu te respondo: 'Mais um dia sozinho... Estou acostumado já :c'")'''

    def boas_vindas(self):
        return "Aleluia alguém me escolheu, não aguentava mais essa solidão..."

    def despedida(self):
        return "NAAAAAAAAAAAAAO, por favor :c "
