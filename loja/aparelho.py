#coding: utf-8
from garantia import Garantia
from datetime import date

class Aparelho():
    
    def __init__(self, marca, modelo, numero_de_serie, quantidade):
        self.marca = marca
        self.modelo = modelo
        self.numero_de_serie = numero_de_serie
        self.quantidade = quantidade

    def vender_aparelho(self):
        if self.quantidade > 0:
            Garantia().criar_termo_garantia()
            self.quantidade -= 1
        else:
            return "Não há estoque suficiente."

    def trocar_aparelho(self):
        if Garantia().data_validade_garantia > date.today():
            Garantia().cliente_que_trocou = Cliente().nome
            if self.quantidade > 0:            
                self.quantidade -= 1
            else:
                return "Não há estoque suficiente."
        else:
            return "Produto fora da data de garantia."

