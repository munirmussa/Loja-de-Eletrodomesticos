import unittest
from should_dsl import should
from loja_de_eletrodomesticos import Aparelho

class TestAparelho(unittest.TestCase):

    def test_definir_aparelho(self):
        ar_condicionado = Aparelho("Gree", "Ar condicionado", 12345)
        ar_condicionado.marca |should| equal_to("Gree")
        ar_condicionado.modelo |should| equal_to("Ar condicionado")
        ar_condicionado.numero_de_serie |should| equal_to(12345)


if __name__=="__main__":
    unittest.main()
