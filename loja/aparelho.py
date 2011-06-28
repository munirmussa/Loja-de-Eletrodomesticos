#coding: utf-8
#from garantia import Garantia

class Aparelho():
    
    numero_de_serie = 1
    aparelhos = []
    vendidos = []

    def __init__(self, marca, modelo, quantidade):
        if quantidade == 1:        
            self.marca = marca
            self.modelo = modelo
            self.numero_de_serie = Aparelho.numero_de_serie
            self.cliente_que_comprou = None
            self.cliente_que_trocou = None
            self.data_compra = None
            self.defeito = None
        else:
            for aparelho in (0, quantidade):   
                Aparelho(marca,modelo,1)
                self.estoque(self)
        
        Aparelho.numero_de_serie += 1 

    def estoque(self):
        self.aparelhos.append(self)

    def vender_aparelho(self, marca, modelo, quantidade, cliente):
        if (len(Aparelho.aparelhos)) == 1:
            quantidade_produtos = 1
        else:
            quantidade_produtos = len(Aparelho.aparelhos) - 1

        for y in range(0, len(Aparelho.aparelhos)):
            if (Aparelho.aparelhos[y].marca == marca):
                for x in range(0, quantidade):
                    Aparelho.aparelhos[y].cliente_que_comprou = cliente
                    Aparelho.aparelhos[y].data_compra = date.today()
                    self.vendidos.append(Aparelho.aparelhos[y])
                    Aparelho.aparelhos[y].remove()
            else:
                return "Não há estoque suficiente."

    def trocar_aparelho(self):
        if Venda.verificar_garantia:
            Garantia().cliente_que_trocou = Cliente().nome
            if self.quantidade > 0:            
                self.quantidade -= 1
            else:
                return "Não há estoque suficiente."
        else:
            return "Produto fora da data de garantia."

    def verificar_garantia(self):
        data_garantia_ano = self.data_compra.year + 1
        data_garantia = date(self.data_garantia_ano, self.data_garantia.month, self.data_garantia.day)
        if date.today() <= self.data_garantia:
            return True
        else:
            return False

    def verificar_quantidade(self):
        resultado = ""
        for x in range(0, len(Aparelho.aparelhos)):
            resultado = resultado + Aparelho.aparelhos[x].marca + Aparelho.aparelhos[x].modelo + Aparelho.aparelhos[x].numero_de_serie
        return resultado

