#coding: utf-8
import unittest
from should_dsl import should
from aparelho import Aparelho

class TestAparelho(unittest.TestCase):

    def test_definir_aparelho(self):
        ar_condicionado = Aparelho("Gree", "Ar condicionado")
        ar_condicionado.marca |should| equal_to("Gree")
        ar_condicionado.modelo |should| equal_to("Ar condicionado")

if __name__=="__main__":
    unittest.main()

