from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao, tipo, tamanho):
        super().__init__(nome, preco) #herdeiro
        self.descricao = descricao
        self.tipo = tipo
        self.tamanho = tamanho

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15)

#nome: herdado de ItemCardapio.
#preco: herdado de ItemCardapio.
#descricao: específico da classe Sobremesa.
#tipo: específico da classe Sobremesa.
#tamanho: específico da classe Sobremesa.