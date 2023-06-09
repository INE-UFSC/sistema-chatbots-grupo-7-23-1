from Bots.Bot import Bot
import sys


class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        try:
            for bot in lista_bots:
                if not isinstance(bot, Bot):
                    raise TypeError("A lista deve conter apenas objetos da classe Bot.")
        except TypeError as err:
            print(f"\nErro: {err}\n")
            self.__lista_bots = []
        else:
            self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print('Olá, esse é o sistema de chatbots da empresa {}'.format(self.__empresa))
        print()
        pass
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print('Os chat bots disponíveis no momento são:')
        for i, bot in enumerate(self.__lista_bots):
            print('Bot: {} - Mensagem de apresentação: {}'.format(bot.nome, bot.apresentacao()))
        print()
        pass
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        while True:
            try:
                selecionado = False
                escolha = input('Digite o nome do chat bot desejado: ')
                for bot in self.__lista_bots:
                    if escolha.lower() == bot.nome.lower():
                        self.__bot = bot
                        selecionado = True
                        print(f'--> {self.__bot.nome} diz: {bot.boas_vindas()}')
                        break
                if not selecionado:
                    print('Bot não encontrado.')
                else:
                    break
            except KeyboardInterrupt:
                print('\nPrograma encerrado pelo usuário.')
                sys.exit(0)

    def mostra_comandos_bot(self):
        try:
            print(Bot.mostra_comandos(self.__bot))
        except AttributeError:
            print("\nBot não encontrado.\n")
        pass
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        try:
            texto = input('Digite o comando desejado (ou -1 para fechar o programa): ')
            cmd = int(texto)
            if cmd == -1 or cmd == self.__bot.comandos_len()+1:
                print(f'--> {self.__bot.nome} diz: {Bot.executa_comando(self.__bot, cmd)}')
                return True
            elif cmd < -1 or cmd > self.__bot.comandos_len()+1:
                print('\nComando não encontrado.\n')
            else:
                print(f'--> {self.__bot.nome} diz: {Bot.executa_comando(self.__bot, cmd)}')
        except (ValueError, TypeError) as err:
            print(f"\nErro: Entrada inválida\n")
        except AttributeError:
            print("\nErro: Bot não encontrado\n")
        except KeyboardInterrupt:
            print("\nPrograma encerrado pelo usuário.\n")
            return True
        return False

        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        try:
            self.boas_vindas()
            self.mostra_menu()
            self.escolhe_bot()
            while True:
                self.mostra_comandos_bot()
                if self.le_envia_comando():
                    break
        except KeyboardInterrupt:
            print('\nPrograma encerrado pelo usuário.\n')
        pass
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
