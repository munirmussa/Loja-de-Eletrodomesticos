#coding: utf-8
import unittest
from should_dsl import should
from estoque import adicionar_aparelho , vender_aparelho , verificar_disponibilidade , trocar_aparelho
from aparelho import Aparelho
from cliente import Cliente


class TestEstoque(unittest.TestCase):

	def test_adicionar_aparelho(self):
# Adicionando  5 aparelhos do mesmo tipo e modelo eles são adicionados à lista de aparelhos
# e cada um assume um número de série individual
		adicionar_aparelho("Gree", "Ar condicionado", 5)
		adicionar_aparelho("Microboard", "Notebook", 2)
		Aparelho.aparelhos[0].marca |should| equal_to("Gree")
		Aparelho.aparelhos[0].modelo |should| equal_to("Ar condicionado")
		Aparelho.aparelhos[0].numero_de_serie |should| equal_to(1)
		Aparelho.aparelhos[1].marca |should| equal_to("Gree")
		Aparelho.aparelhos[1].modelo |should| equal_to("Ar condicionado")
		Aparelho.aparelhos[1].numero_de_serie |should| equal_to(2)
		Aparelho.aparelhos[2].marca |should| equal_to("Gree")
		Aparelho.aparelhos[2].modelo |should| equal_to("Ar condicionado")
		Aparelho.aparelhos[2].numero_de_serie |should| equal_to(3)
		Aparelho.aparelhos[3].marca |should| equal_to("Gree")
		Aparelho.aparelhos[3].modelo |should| equal_to("Ar condicionado")
		Aparelho.aparelhos[3].numero_de_serie |should| equal_to(4)
		Aparelho.aparelhos[4].marca |should| equal_to("Gree")
		Aparelho.aparelhos[4].modelo |should| equal_to("Ar condicionado")
		Aparelho.aparelhos[4].numero_de_serie |should| equal_to(5)
		Aparelho.aparelhos[5].marca |should| equal_to("Microboard")
		Aparelho.aparelhos[5].modelo |should| equal_to("Notebook")
		Aparelho.aparelhos[5].numero_de_serie |should| equal_to(6)
		Aparelho.aparelhos[6].marca |should| equal_to("Microboard")
		Aparelho.aparelhos[6].modelo |should| equal_to("Notebook")
		Aparelho.aparelhos[6].numero_de_serie |should| equal_to(7)
		len(Aparelho.aparelhos) |should| equal_to(7)



	def test_vender_aparelho(self):
# Vendendo um Ar Condicionado Gree ele é removido da lista de aparelhos e colocado na lista de vendidos
		Aparelho.vendidos = []
		Aparelho.aparelhos = []
		Aparelho.contador = 1
		adicionar_aparelho("Gree", "Ar condicionado", 5)
		adicionar_aparelho("Microboard", "Notebook", 2)
		vender_aparelho("Gree","Ar condicionado",1,"Saulo","Campos","Matins Lage","Trav. Miessy","13","29/06/2011")
		len(Aparelho.vendidos) |should| equal_to(1)
		len(Aparelho.aparelhos) |should| equal_to(6)
# Tentado efetuar uma venda de uma quantidade maior que a disponível do mesmo profuto e retornada uma mensagem de erro e
# as listas de aparelhos e vendidos continuam intactas
		vender_aparelho("Gree","Ar condicionado",50,"Saulo","Campos","Matins Lage","Trav. Miessy","13","29/06/2011") |should| equal_to("Quantidade insuficiente no estoque")
		len(Aparelho.vendidos) |should| equal_to(1)
		len(Aparelho.aparelhos) |should| equal_to(6)

# Vendendo os últimos produtos em estoque a lista aparelhos fica sem o Ar Condicionado Gree...
		vender_aparelho("Gree","Ar condicionado",2,"Saulo","Campos","Matins Lage","Trav. Miessy","13","29/06/2011")
		len(Aparelho.vendidos) |should| equal_to(3)
		len(Aparelho.aparelhos) |should| equal_to(4)

		vender_aparelho("Gree","Ar condicionado",1,"Saulo","Campos","Matins Lage","Trav. Miessy","13","29/06/2011")
		len(Aparelho.vendidos) |should| equal_to(4)
		len(Aparelho.aparelhos) |should| equal_to(3)

		vender_aparelho("Gree","Ar condicionado",1,"Saulo","Campos","Matins Lage","Trav. Miessy","13","29/06/2011")
		len(Aparelho.vendidos) |should| equal_to(5)
		len(Aparelho.aparelhos) |should| equal_to(2)
		
# ...logo, ao tentar vender mais produtos do mesmo ocorre a mensagem de erro
		vender_aparelho("Gree","Ar condicionado",2,"Saulo","Campos","Matins Lage","Trav. Miessy","13","29/06/2011") |should| equal_to("Produto em falta")
		len(Aparelho.vendidos) |should| equal_to(5)
		len(Aparelho.aparelhos) |should| equal_to(2)
		Aparelho.aparelhos[0].marca |should| equal_to("Microboard")
		Aparelho.aparelhos[0].modelo |should| equal_to("Notebook")
		Aparelho.aparelhos[0].numero_de_serie |should| equal_to(6)
		Aparelho.aparelhos[1].marca |should| equal_to("Microboard")
		Aparelho.aparelhos[1].modelo |should| equal_to("Notebook")
		Aparelho.aparelhos[1].numero_de_serie |should| equal_to(7)

	def test_trocar_aparelho(self):
		Aparelho.vendidos = []
		Aparelho.aparelhos = []
		Aparelho.trocados = []
		Aparelho.contador = 1
		adicionar_aparelho("Gree", "Ar condicionado", 5)
		adicionar_aparelho("Microboard", "Notebook", 2)
		vender_aparelho("Gree","Ar condicionado",1,"Saulo","Campos","Matins Lage","Trav. Miessy","13","29/06/2011")
		len(Aparelho.vendidos) |should| equal_to(1)
		len(Aparelho.aparelhos) |should| equal_to(6)
		trocar_aparelho(1,"Saulo","Não gela")
		len(Aparelho.vendidos) |should| equal_to(1) 
		len(Aparelho.trocados) |should| equal_to(1)
		len(Aparelho.aparelhos) |should| equal_to(5)
# testando trocar um aparelho que não existe
		trocar_aparelho(8,"Munir","Não troca temperatura") |should| equal_to("Aparelho não encontrado!")
		len(Aparelho.aparelhos) |should| equal_to(5)
# testando trocar aparelho fora do prazo de garantia
		vender_aparelho("Microboard","Notebook",1,"Saulo","Campos","Matins Lage","Trav. Miessy","13","29/06/2010")
		len(Aparelho.vendidos) |should| equal_to(2)
		len(Aparelho.aparelhos) |should| equal_to(4)
		#print Aparelho.vendidos[0].numero_de_serie
		#print Aparelho.vendidos[1].numero_de_serie
		#print Aparelho.vendidos[1].marca
		trocar_aparelho(7,"Saulo","Não liga") |should| equal_to("Aparelho fora do prazo de garantia.")
		len(Aparelho.aparelhos) |should| equal_to(4)

	def test_quantidade_estoque(self):
		Aparelho.vendidos = []
		Aparelho.aparelhos = []
		Aparelho.contador = 1
		adicionar_aparelho("Gree", "Ar condicionado", 5)
		Aparelho.aparelhos[0].quantidade_estoque() |should| equal_to(5)

	def test_relacao_trocados(self):
		Aparelho.vendidos = []
		Aparelho.aparelhos = []
		Aparelho.trocados = []
		Aparelho.contador = 1
		adicionar_aparelho("Gree", "Ar condicionado", 5)
		vender_aparelho("Gree","Ar condicionado",1,"Saulo","Campos","Matins Lage","Trav. Miessy","13","29/06/2011")
		trocar_aparelho(5,"Saulo","Não gela")	
		Aparelho.trocados[0].marca |should| equal_to("Gree")
		Aparelho.trocados[0].modelo |should| equal_to("Ar condicionado")
		Aparelho.trocados[0].garantia.cliente_que_trocou |should| equal_to("Saulo")
		Aparelho.trocados[0].garantia.defeito |should| equal_to("Não gela")

if __name__=="__main__":
    unittest.main()
