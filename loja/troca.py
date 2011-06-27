#coding: utf-8
from garantia import Garantia
from datetime import date

    def trocar_aparelho(self):
        if Venda.verificar_garantia:
            Garantia().cliente_que_trocou = Cliente().nome
            if self.quantidade > 0:            
                self.quantidade -= 1
            else:
                return "Não há estoque suficiente."
        else:
            return "Produto fora da data de garantia."

    
