#coding: utf-8
from garantia import Garantia
from datetime import date

    def __init__(self, cliente_que_comprou):
        self.cliente_que_comprou = cliente_que_comprou
        self.produtos = []

    def vender_aparelho(self):
        if self.quantidade > 0:
            Garantia().criar_termo_garantia()
            self.quantidade -= 1

        self.vendidos.append({'cliente_que_comprou': self.cliente_que_comprou,
                               'data_compra': date.today()})
            
        else:
            return "Não há estoque suficiente."

    def verificar_garantia(self):
        data_garantia_ano = self.data_compra.year + 1
        data_garantia = date(self.data_garantia_ano, self.data_garantia.month, self.data_garantia.day)
        if date.today() <= self.data_garantia:
            return True
        else:
            return False
