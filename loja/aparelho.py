#coding: utf-8
#from garantia import Garantia
from datetime import date

class Aparelho():

    contador = 1
    aparelhos = []
    vendidos = []

    def __init__(self, marca, modelo):   
		self.marca = marca
		self.modelo = modelo
#		self.numero_de_serie = Aparelho.numero_de_serie
#		self.cliente_que_comprou = None
#		self.cliente_que_trocou = None
#		self.data_compra = None
#		self.defeito = None
		self.termo_garantia = None
		self.numero_de_serie = Aparelho.contador
		Aparelho.contador += 1
#		self.aparelhos.append(self)

#		if	quantidade > 0:
#			for aparelho in range(quantidade):
#				self.aparelhos.append(self)
#				self.numero_de_serie = Aparelho.contador
#				Aparelho.contador += 1
            

        
#        Aparelho.numero_de_serie += 1 

#    def estoque(self):
 #       self.aparelhos.append(self)

#	def estoque(self,aparelho):
#		self.aparelhos.append(aparelho)


#    def vender_aparelho(self, marca, modelo, quantidade, cliente):
#		if (len(Aparelho.aparelhos)) == 1:
#			quantidade_produtos = 1
#		else:
#			quantidade_produtos = len(Aparelho.aparelhos) - 1
#
#		for y in range(0, len(Aparelho.aparelhos)):
#			if (Aparelho.aparelhos[y].marca == marca):
#				for x in range(0, quantidade):
#					Aparelho.aparelhos[y].cliente_que_comprou = cliente
#					Aparelho.aparelhos[y].data_compra = date.today()
#					self.vendidos.append(Aparelho.aparelhos[y])
#					Aparelho.aparelhos[y].remove()
#			else:
#				return "Não há estoque suficiente."

    def trocar_aparelho(self):
        if Venda.verificar_garantia:
            Garantia().cliente_que_trocou = Cliente().nome
            if self.quantidade > 0:            
                self.quantidade -= 1
            else:
                return "Não há estoque suficiente."
        else:
            return "Produto fora da data de garantia."

    def verificar_quantidade(self):
        resultado = ""
        for x in range(0, len(Aparelho.aparelhos)):
            resultado = resultado + Aparelho.aparelhos[x].marca + Aparelho.aparelhos[x].modelo + Aparelho.aparelhos[x].numero_de_serie
        return resultado

