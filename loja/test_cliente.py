#coding: utf-8
import unittest
from should_dsl import should
from cliente import Cliente

class TestCliente(unittest.TestCase):

	def test_definir_cliente(self):
		cliente1 = Cliente("Antonio", "Campos", "Centro", "João Pessoa", "200")
		cliente1.nome |should| equal_to("Antonio")
		cliente1.endereco['cidade'] |should| equal_to("Campos")
		cliente1.endereco['bairro'] |should| equal_to("Centro")
		cliente1.endereco['rua'] |should| equal_to("João Pessoa")
		cliente1.endereco['numero'] |should| equal_to("200")



if __name__=="__main__":
    unittest.main()
