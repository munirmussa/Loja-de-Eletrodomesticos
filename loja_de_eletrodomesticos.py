#coding: utf-8
from datetime import date

class Aparelho():
    
    def __init__(self, marca, modelo, numero_de_serie):
        self.marca = marca
        self.modelo = modelo
        self.numero_de_serie = numero_de_serie
