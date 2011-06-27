#coding: utf-8
import unittest
from datetime import date
from should_dsl import should
from garantia import Garantia
from troca import Troca

class TestTroca(unittest.TestCase):
    def test_trocar_aparelho(self):
        ar_condicionado = Aparelho("Gree", "Ar condicionado", 12345, 5)
        ar_condicionado.trocar_aparelho()
        ar_condicionado.quantidade |should| equal_to(4)
        

if __name__=="__main__":
    unittest.main()
