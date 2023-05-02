from Bots.Bot import Bot


class BotFeliz_gp2(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self._comandos = {
            "Bom dia" : " Como posso ajudá-lo? ", 
            "Qual o Seu nome": f"Meu nome é {self.nome}", 
            "Quero um conselho" : "Não tenha medo de ser você mesmo e vá em busca dos seus sonhos."
        }

    def apresentacao(self):
        print(f"Olá, sou o {self.nome} e te amo!!!")

    def mostra_comandos(self):
        print("1 - Boas vindas.")
        print("2 - Qual o seu nome?")
        print("3 - Quero um conselho.")
        print("4 - Adeus.")
        
    
    def executa_comando(self,cmd):
        if cmd == '1':
            print("")
            print("--> Como posso ajudá-lo?")
            print("")
        elif cmd == '2':
            print("")
            print(f"--> Meu nome é {self.nome}.")
            print("")
        elif cmd == '3':
            print("")
            print("--> Não tenha medo de ser você mesmo e vá em busca dos seus sonhos.")
            print("")
        elif cmd == '4':
            self.despedida()
            return False
        return True

            

    def boas_vindas(self):
        print()
        print(f"--> Olá, pessoa maravilhosa. Estou muito feliz que você me escolheu.")
        print()

    def despedida(self):
        print()
        print(f"--> Foi um prazer ajudar")
        print()