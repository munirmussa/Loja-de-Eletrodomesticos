# coding: utf-8
from aparelho import Aparelho
from cliente import Cliente
from datetime import date

class Garantia():

	def criar_termo_garantia(self):
        self.data_compra = date.today()
        self.marca = Aparelho().marca
        self.modelo = Aparelho().modelo
        self.numero_de_serie = Aparelho().numero_de_serie
        self.cliente_que comprou = Cliente().nome
        self.cidade = Cliente().cidade
        self.bairro = Cliente().bairro
        self.rua = Cliente().rua
        self.numero = Cliente().numero
        self.cliente_que_trocou = None
