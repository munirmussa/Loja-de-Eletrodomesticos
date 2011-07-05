#coding: utf-8

class Cliente():
    
	def __init__(self, nome, cidade, bairro, rua, numero):
		self.nome = nome
		self.endereco = {'cidade':cidade,'bairro':bairro,'rua':rua,'numero':numero}
#        self.cidade = cidade
#        self.bairro = bairro
#        self.rua = rua
#        self.numero = numero
