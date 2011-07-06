#coding: utf-8
import unittest
from datetime import date
from should_dsl import should
from garantia import Garantia
from cliente import Cliente


class TestGarantia(unittest.TestCase):
    def test_criar_termo_garantia(self):
		cliente1 = Cliente("Antonio", "Campos", "Centro", "João Pessoa", "200")
		garantia1 = Garantia(cliente1.nome,"29/06/1990")
		garantia1.cliente_que_comprou |should| equal_to("Antonio")
		garantia1.data_compra |should| equal_to(date(1990,06,29))

    def test_verificar_garantia(self):
		cliente2 = Cliente("Antonio", "Campos", "Centro", "João Pessoa", "200")
		garantia2 = Garantia(cliente2.nome,"29/06/1990")
		garantia2.verificar_garantia() |should| equal_to(False)		
        
		cliente3 = Cliente("Saulo", "Chaves", "Martins Lage", "Trav. Miessy", "13")
		garantia3 = Garantia(cliente3.nome,"29/06/2011")
		garantia3.verificar_garantia() |should| equal_to(True)		

if __name__=="__main__":
    unittest.main()
