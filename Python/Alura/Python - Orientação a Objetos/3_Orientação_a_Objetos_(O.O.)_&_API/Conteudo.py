'''                    Herança

Ao utilizar a Função super(). ela permite que tenha acesso as informações 
de outras Classes existentes.

Exemplo: super().__init__(nome, preço)

Função isinstance essa função retornará verdadeiro se o argumento for 
uma instancia ou uma classe derivada de outra função.

Exemplo: def adicionar_prato_no_cardapio(self, prato):
            self._cardapio.append(prato)   #função de adicionar pratos ao cardapio

         def adicionar_bebida_no_cardapio(self, bebida):
            self._cardapio.append(bebida)   #função de adicionar bebidas ao cardapio
   
    def adicionar_no_cardapio(self,item):
        if isinstance(item, itemCardapio):
                self._cardapio.append(item)  
     
    #retornará verdadeiro se o argumento for uma instancia ou 
     uma classe derivada do cardapio.


























'''