# coding: utf-8
from datetime import date

class Garantia():
	def criar_termo_garantia(self):
        self.data_compra = date.today()
        self.marca = Aparelho().marca
        self.modelo = Aparelho().modelo
        self.numero_de_serie = Aparelho().numero_de_serie
        self.cliente_que comprou = Cliente().nome
        self.endereco = Cliente().endereco
        self.cliente_que_trocou = None

	

