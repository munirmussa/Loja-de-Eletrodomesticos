# coding: utf-8
from aparelho import Aparelho
from cliente import Cliente
from datetime import date
from garantia import Garantia

# Estancia objetos na classe Aparelho e os adiciona a lista de produtos.
# Caso a quantidade seja inválida uma mensagem educada
def adicionar_aparelho(marca,modelo,quantidade):
	if quantidade > 0:
		for aparelho in range(1,quantidade+1):
			Aparelho.aparelhos.append(Aparelho(marca,modelo))
	else:
		return "Quantidade inválida,cavalo"

# Função para verificar a disponibilidade do produto dentro da função vender_aparelho
def verificar_disponibilidade(marca,modelo):
	quantidade_disponivel = 0
	for x in range(len(Aparelho.aparelhos)):
		if ((Aparelho.aparelhos[x].marca == marca) and (Aparelho.aparelhos[x].modelo == modelo)):
			quantidade_disponivel += 1
	return quantidade_disponivel

# Função que efetua a venda dos produtos.
def vender_aparelho(marca,modelo,quantidade,nome,cidade,bairro,rua,numero,data_compra):
###	quantidade_disponivel = verificar_disponibilidade(marca,modelo)
###	if quantidade_disponivel > 0 :

# Verifica a disponibilidade do produto
	if verificar_disponibilidade(marca,modelo) > 0:
		if verificar_disponibilidade(marca,modelo) >= quantidade:
# Loop percorrendo a lista produtos
				for y in range(len(Aparelho.aparelhos)):
###					quantidade_disponivel = verificar_disponibilidade(marca,modelo)
###					if ((quantidade > 0) and (quantidade_disponivel >= quantidade)):

# Em cada voltado loop é verificado se a quantidade ainda é maior que 0...
					if quantidade > 0:
# ...se sim ele verifica se o aparelho na posição atual da lista aparelhos corresponde ao modelo e marca desejados...
						if ((Aparelho.aparelhos[y-1].marca == marca) and (Aparelho.aparelhos[y-1].modelo == modelo)):
# ...se sim ele define os atributos "cliente_que_comprou" e "data_compra" do objeto Aparelho, o adiciona na lista
# vendidos e o remove da lista produtos
							Aparelho.aparelhos[y-1].cliente_que_comprou = Cliente(nome,cidade,bairro,rua,numero)
							Aparelho.aparelhos[y-1].garantia = Garantia(Aparelho.aparelhos[y-1].cliente_que_comprou.nome,data_compra)
#							Aparelho.aparelhos[y-1].data_compra = date.today()
							Aparelho.vendidos.append(Aparelho.aparelhos[y-1])
							Aparelho.aparelhos.remove(Aparelho.aparelhos[y-1])
							quantidade -= 1							
		else:
			return "Quantidade insuficiente no estoque"
	else:
		return "Produto em falta"				
			
		
	def trocar_aparelho(self):
		if verificar_garantia:
			
			if self.quantidade > 0:            
				self.quantidade -= 1
			else:
				return "Não há estoque suficiente."
		else:
			return "Produto fora da data de garantia."

	def verificar_garantia(self):
		
		data_garantia_ano = self.
		data_garantia = self.data_garantia_ano, self.data_garantia.month, self.data_garantia.day)
		if date.today() <= self.data_garantia:
			return True
		else:
			return False
