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
		self.garantia = None
		self.numero_de_serie = Aparelho.contador
		Aparelho.contador += 1

	def quantidade_estoque(self):
		return len(Aparelho.aparelhos)

	def relacao_trocados(self):
		defeituosos = []
		for aparelho in range(len(Aparelho.trocados)):
			defeituosos.append([Aparelho.trocados[aparelho].marca,Aparelho.trocados[aparelho].modelo,Aparelho.trocados[aparelho].garantia.cliente_que_trocou,Aparelho.trocados[aparelho].garantia.data_troca,Aparelho.trocados[aparelho].garantia.defeito])
		return defeituosos

	def relacao_clientes_com_produtos_sem_defeito(self):
		clientes_com_produtos_sem_defeito = []
		for aparelho in range(len(Aparelho.vendidos)):
			clientes_com_produtos_sem_defeito.append(Aparelho.vendidos[aparelho].garantia.cliente_que_comprou)
			return clientes_com_produtos_sem_defeito

