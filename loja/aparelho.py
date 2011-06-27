#coding: utf-8
from garantia import Garantia

class Aparelho():
    
    numero_de_serie = 1
    aparelhos = []

    def __init__(self, marca, modelo, quantidade):
        self.marca = marca
        self.modelo = modelo
        self.numero_de_serie = Aparelho.numero_de_serie
        for aparelho in (0, quantidade):   
            Aparelho(self.marca,self.modelo,1)
            self.estoque(self)
        
        numero_de_serie += 1 

    def estoque(self):
        self.aparelhos.append(self)

    def verificar_quantidade(self):
        resultado = ""
        for x in range(0, len(Storage.aparelhos)):
            resultado = resultado + Aparelho.aparelhos[x].marca + Aparelho.aparelhos[x].modelo + Aparelho.aparelhos[x].numero_de_serie))
        return resultado

