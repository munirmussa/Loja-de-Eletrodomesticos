import unittest
from should_dsl import should
from aparelho import Aparelho

class TestAparelho(unittest.TestCase):

    def test_definir_aparelho(self):
        ar_condicionado = Aparelho("Gree", "Ar condicionado", 12345, 5)
        ar_condicionado.marca |should| equal_to("Gree")
        ar_condicionado.modelo |should| equal_to("Ar condicionado")
        ar_condicionado.numero_de_serie |should| equal_to(12345)
        ar_condicionado.quantidade |should| equal_to(5)

    def test_vender_aparelho(self):
        ar_condicionado = Aparelho("Gree", "Ar condicionado", 12345, 5)
        ar_condicionado.vender_aparelho()
        ar_condicionado.quantidade |should| equal_to(4)

    def test_trocar_aparelho(self):
        ar_condicionado = Aparelho("Gree", "Ar condicionado", 12345, 5)
        ar_condicionado.trocar_aparelho()
        ar_condicionado.quantidade |should| equal_to(4)

if __name__=="__main__":
    unittest.main()
