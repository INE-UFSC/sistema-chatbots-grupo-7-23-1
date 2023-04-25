#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotDramatico import BotDramatico
from Bots.BotFeliz import BotFeliz

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Roger"), BotDramatico("Josemildo"), BotFeliz("Carlos")]

sys = scb.SistemaChatBot("BoterSystem",lista_bots)
sys.inicio()
