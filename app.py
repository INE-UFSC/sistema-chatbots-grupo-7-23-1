#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotDramatico import BotDramatico
from Bots.BotFeliz import BotFeliz
from Bots.BotFeliz_gp1 import BotFeliz_gp1
from Bots.BotTriste_gp1 import BotTriste_gp1
from Bots.BotZangado_gp1 import BotZangado_gp1
from Bots.BotFeliz_gp2 import BotFeliz_gp2
from Bots.BotTriste_gp4 import BotTriste_gp4
from Bots.BotZangado_gp3 import BotZangado_gp3

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Roger"), BotDramatico("Josemildo"), BotFeliz("Carlos"),BotFeliz_gp1("José"),BotZangado_gp1('João'),BotTriste_gp1("Maria"),BotFeliz_gp2('Pedro'),BotTriste_gp4('Gelson'),BotZangado_gp3('Kleber')]

sys = scb.SistemaChatBot("BoterSystem",lista_bots)
sys.inicio()
