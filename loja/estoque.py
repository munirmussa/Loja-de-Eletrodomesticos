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

# Verifica a disponibilidade do produto
	if verificar_disponibilidade(marca,modelo) > 0:
		if verificar_disponibilidade(marca,modelo) >= quantidade:
# Loop percorrendo a lista produtos
				for y in range(len(Aparelho.aparelhos)):
# Em cada voltado loop é verificado se a quantidade ainda é maior que 0...
					if quantidade > 0:
# ...se sim ele verifica se o aparelho na posição atual da lista aparelhos corresponde ao modelo e marca desejados...
						if ((Aparelho.aparelhos[y-1].marca == marca) and (Aparelho.aparelhos[y-1].modelo == modelo)):
# ...se sim ele define os atributos "cliente_que_comprou" e "data_compra" do objeto Aparelho, o adiciona na lista
# vendidos e o remove da lista produtos
							Aparelho.aparelhos[y-1].cliente_que_comprou = Cliente(nome,cidade,bairro,rua,numero)
							Aparelho.aparelhos[y-1].garantia = Garantia(Aparelho.aparelhos[y-1].cliente_que_comprou.nome,data_compra)
							Aparelho.vendidos.append(Aparelho.aparelhos[y-1])
							Aparelho.aparelhos.remove(Aparelho.aparelhos[y-1])
							quantidade -= 1							
		else:
			return "Quantidade insuficiente no estoque"
	else:
		return "Aparelho indisponível para venda."				

def desformatar_data(data):
	data_lista = str(data).split("-")
	data_string = data_lista[2] + "/" + data_lista[1] + "/" + data_lista[0]
	return data_string
			
		
def trocar_aparelho(numero_de_serie,cliente_que_trocou,defeito):
	for aparelho in range(len(Aparelho.vendidos)):
		if Aparelho.vendidos[aparelho].numero_de_serie == numero_de_serie:
			if Aparelho.vendidos[aparelho].garantia.verificar_garantia():
				if verificar_disponibilidade(Aparelho.vendidos[aparelho].marca,Aparelho.vendidos[aparelho].modelo) > 0:
					Aparelho.vendidos[aparelho].garantia.defeito = defeito
					Aparelho.vendidos[aparelho].garantia.cliente_que_trocou = cliente_que_trocou
					Aparelho.vendidos[aparelho].garantia.data_troca = date.today()
					Aparelho.trocados.append(Aparelho.vendidos[aparelho])
					vender_aparelho(Aparelho.vendidos[aparelho].marca, Aparelho.vendidos[aparelho].modelo,1, Aparelho.vendidos[aparelho].cliente_que_comprou.nome, Aparelho.vendidos[aparelho].cliente_que_comprou.endereco['cidade'], Aparelho.vendidos[aparelho].cliente_que_comprou.endereco['bairro'], Aparelho.vendidos[aparelho].cliente_que_comprou.endereco['rua'], Aparelho.vendidos[aparelho].cliente_que_comprou.endereco['numero'], desformatar_data(Aparelho.vendidos[aparelho].garantia.data_compra))
					Aparelho.vendidos.remove(Aparelho.vendidos[aparelho])
				else:
					return "Aparelho indisponível para troca."
			else:
				return "Aparelho fora do prazo de garantia."
		else:
			return "Aparelho não encontrado!"
