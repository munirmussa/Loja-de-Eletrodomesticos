#coding: utf-8
import unittest
from datetime import date
from should_dsl import should
from garantia import Garantia
from venda import Venda

class TestVenda(unittest.TestCase):
    def test_vender_aparelho(self):
        ar_condicionado = Aparelho("Gree", "Ar condicionado", 12345, 5)
        ar_condicionado.vender_aparelho()
        ar_condicionado.quantidade |should| equal_to(4)
        

if __name__=="__main__":
    unittest.main()
