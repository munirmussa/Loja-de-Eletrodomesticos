#coding: utf-8
#from garantia import Garantia
from datetime import date

class Aparelho():

    contador = 1
    aparelhos = []
    vendidos = []
    trocados = []

    def __init__(self, marca, modelo):   
		self.marca = marca
		self.modelo = modelo
#		self.numero_de_serie = Aparelho.numero_de_serie
#		self.cliente_que_comprou = None
#		self.cliente_que_trocou = None
#		self.data_compra = None
#		self.defeito = None
		self.garantia = None
		self.numero_de_serie = Aparelho.contador
		Aparelho.contador += 1

    def quantidade_estoque(self):
        return len(Aparelho.aparelhos)

	def relacao_trocados(self):
		return Aparelho.trocados

