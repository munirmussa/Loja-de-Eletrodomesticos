#coding: utf-8
import unittest
from datetime import date
from should_dsl import should
from garantia import Garantia

class TestGarantia(unittest.TestCase):
    def test_criar_termo_garantia(self):
        garantia1 = Garantia()
        garantia1.criar_termo_garantia()
        garantia1.data_compra |should| equal_to(date.today())
        garantia1.data_validade_garantia |should| equal_to(date(2012,06,16))
        garantia1.marca |should| equal_to("Gree")
        garantia1.modelo |should| equal_to("Ar condicionado")
        garantia1.numero_de_serie |should| equal_to(12345)
        garantia1.cliente_que_comprou |should| equal_to("Antonio")
        garantia1.cidade |should| equal_to("Campos")
        garantia1.bairro |should| equal_to("Centro")
        garantia1.rua |should| equal_to("João Pessoa")
        garantia1.numero |should| equal_to(200)
        garantia1.cliente_que_trocou |should| equal_to(None)
        

if __name__=="__main__":
    unittest.main()
