#coding: utf-8
import unittest
from should_dsl import should
from estoque import adicionar_aparelho , vender_aparelho , verificar_disponibilidade
from aparelho import Aparelho



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
		print len(Aparelho.aparelhos)



	def test_vender_aparelho(self):
# Vendendo um Ar Condicionado Gree ele é removido da lista de aparelhos e colocado na lista de vendidos
		vender_aparelho("Gree","Ar condicionado",1)
		len(Aparelho.vendidos) |should| equal_to(1)
		len(Aparelho.aparelhos) |should| equal_to(6)
# Tentado efetuar uma venda de uma quantidade maior que a disponível do mesmo profuto e retornada uma mensagem de erro e
# as listas de aparelhos e vendidos continuam intactas
		vender_aparelho("Gree","Ar condicionado",50) |should| equal_to("Quantidade insuficiente no estoque")
		len(Aparelho.vendidos) |should| equal_to(1)
		len(Aparelho.aparelhos) |should| equal_to(6)

# Vendendo os últimos produtos em estoque a lista aparelhos fica sem o Ar Condicionado Gree...
		vender_aparelho("Gree","Ar condicionado",2)
		len(Aparelho.vendidos) |should| equal_to(3)
		len(Aparelho.aparelhos) |should| equal_to(4)

		vender_aparelho("Gree","Ar condicionado",1)
		len(Aparelho.vendidos) |should| equal_to(4)
		len(Aparelho.aparelhos) |should| equal_to(3)

		vender_aparelho("Gree","Ar condicionado",1)
		len(Aparelho.vendidos) |should| equal_to(5)
		len(Aparelho.aparelhos) |should| equal_to(2)

# ...logo, ao tentar vender mais produtos do mesmo ocorre a mensagem de erro
		vender_aparelho("Gree","Ar condicionado",2) |should| equal_to("Produto em falta")
		len(Aparelho.vendidos) |should| equal_to(5)
		len(Aparelho.aparelhos) |should| equal_to(2)
		Aparelho.aparelhos[0].marca |should| equal_to("Microboard")
		Aparelho.aparelhos[0].modelo |should| equal_to("Notebook")
		Aparelho.aparelhos[0].numero_de_serie |should| equal_to(6)
		Aparelho.aparelhos[1].marca |should| equal_to("Microboard")
		Aparelho.aparelhos[1].modelo |should| equal_to("Notebook")
		Aparelho.aparelhos[1].numero_de_serie |should| equal_to(7)



#        len(Aparelho.aparelhos) |should| equal_to(4)
#		Aparelho.vendidos[0].marca |should| equal_to("Gree")
#		vender_aparelho("Gree","Ar Condicionado",80) |should| equal_to("Quantidade insuficiente no estoque")
#		vender_aparelho("Gree","Ar Condicionado",80) |should| equal_to(aaa)
#		aaaaaa |should| equal_to(555)
#		len(Aparelho.vendidos) |should| equal_to(1)


#        len(Aparelho.aparelhos) |should| equal_to(4)

# ---- (Linha abaixo) "quantidade" não é atributo de Aparelho. Teste inválido
#        ar_condicionado.quantidade |should| equal_to(1)

#    def test_vender_aparelho(self):
 #       cliente1 = Cliente("Antonio", "Campos", "Centro", "João Pessoa", 200)
  #      ar_condicionado = Aparelho("Gree", "Ar condicionado", 1)
   #     ar_condicionado.vender_aparelho("Gree", "Ar condicionado", 1, cliente1)
    #    ar_condicionado.vendidos |should| have(1)

    #def test_trocar_aparelho(self):
     #   ar_condicionado = Aparelho("Gree", "Ar condicionado", 12345, 5)
      #  ar_condicionado.trocar_aparelho()
       # ar_condicionado.quantidade |should| equal_to(4)

if __name__=="__main__":
    unittest.main()
