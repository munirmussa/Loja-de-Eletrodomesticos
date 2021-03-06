# coding: utf-8
from aparelho import Aparelho
from cliente import Cliente
from datetime import date

class Garantia():

	def __init__(self,cliente_que_comprou,data_compra):
		self.cliente_que_comprou = cliente_que_comprou
		self.cliente_que_trocou = None
		self.data_compra = self.formatar_data(data_compra)
		self.data_troca = None
		self.defeito = None

	def formatar_data(self,data_compra):
		lista_data = data_compra.split("/")
		data_formatada = date(int(lista_data[2]),int(lista_data[1]),int(lista_data[0]))
		return data_formatada

	def verificar_garantia(self):		
		data_garantia_ano = self.data_compra.year + 1
		data_garantia = date(data_garantia_ano, self.data_compra.month, self.data_compra.day)
		if date.today() <= data_garantia:
			return True
		else:
			return False
