#coding: utf-8
from garantia import Garantia

class Aparelho():
    
    numero_de_serie = 0

    def __init__(self, marca, modelo, quantidade):
        self.marca = marca
        self.modelo = modelo
        self.quantidade = quantidade
        numero_de_serie += 1

