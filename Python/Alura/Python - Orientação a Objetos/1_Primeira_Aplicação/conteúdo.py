'''Tipos de nomenclatura'''

'''
~ Camel Case ~

Começar com a primeira letra minuscula e a 
primeira letra de cada nova palavra subsequente maiúscula.

Exemplo:
coisasParaFazer


~ Pascal Case ~ (Upper Camel Case ou Capital Case)

Combina palavras colocando todas com a primeira letra maiúscula.

Exemplo:
CoisasParaFazer


~ Snake Case ~ (Underscore Case)

Utilizamos underline no lugar do espaço para separar as palavras. 
Quando o snake case está em caixa alta, ele é chamado de 
“screaming snake case”:

Exemplo:
Underscore Case
coisas_para_fazer

Screaming snake case
COISAS_PARA_FAZER


~ Kebab Case ~

Utiliza o traço para combinar as palavras. 
Quando o kebab case está em caixa alta, ele é chamado de 
“screaming kebab case”:

Exemplo:
Underscore Case
coisas-para-fazer

Screaming snake case
COISAS-PARA-FAZER


Convenções JavaScript

* camelCase: variáveis, constantes, funções e métodos;
* PascalCase: classes.

Exemplo:

class ClienteBanco {  
    constructor(primeiroNome, cpf) { 
      this.primeiroNome = primeiroNome;
      this.cpf = cpf;
    }

  exibirPrimeiroNome(){
     console.log(this.primeiroNome);
    }
}

  var clienteUm = new ClienteBanco('Maria', 150);
  var clienteDois = new ClienteBanco('João', 70);


Convenções Python

* snake_case: variáveis, funções e métodos;
* PascalCase: classes;
* SCREAMING_SNAKE_CASE: constantes.

Exemplo:

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

        def exibir_primeiro_nome(self):
        print(self.nome)

        pessoa_um = Pessoa('Alice', '123456789')

        
Convenções GO  (GoLang - Linguagem do Google)

* PascalCase: classes e módulos;
* snake_case: métodos, variáveis, nomear arquivos e diretórios;
* SCREAMING_SNAKE_CASE: constantes.

Exemplo:

package nome

type ExportedStruct {
    unexportedField string
}


Convenções Ruby (Ruby on Rails)
(programação dinâmica e orientada a objetos)

PascalCase: classes e módulos;
snake_case: métodos, variáveis, nomear arquivos e diretórios;
SCREAMING_SNAKE_CASE: constantes.

Exemplo:

class Pessoa

    def initialize(primeiro_nome, cpf)    
        @primeiro_nome = primeiro_nome
        @cpf = cpf
    end

    def exibe_primeiro_nome
        @primeiro_nome
    end
end

pessoa_um = Pessoa.new('Alice', 123456789)


Resumo:

Convenção	                      Exemplo
Camel case	              >>      primeiroNomePessoa
Pascal case	              >>      PrimeiroNomePessoa
Snake case	              >>      primeiro_nome_pessoa
Screaming snake case	  >>      PRIMEIRO_NOME_PESSOA
Kebab case	              >>      primeiro-nome-pessoa
Screaming kebab case	  >>      PRIMEIRO-NOME-PESSOA


FUNÇÃO MATCH

usamos "blocos de case" para substituir a variável "opção_escolhida"

match expressão:
    case padrão_1:
        # Código a ser executado se expressão corresponder a padrão_1
    case padrão_2:
        # Código a ser executado se expressão corresponder a padrão_2
    # ... outros casos ...
    case _:
        # Código a ser executado se nenhum dos padrões anteriores corresponder. Isso é útil para tratar casos não específicos.

Vantagens da Instrução match	
Lidar com condições complexas e múltiplos padrões de maneira mais intuitiva.	
Sintaxe concisa melhora a legibilidade do código, especialmente em casos complexos.	
Permite desestruturação direta, evitando repetição excessiva de variáveis.	
Adiciona expressividade ao código, especialmente em situações de correspondência de padrões.	


Vantagens da Estrutura if
Implementação clássica e amplamente conhecida.
Amplamente suportada em todas as versões do Python.
Estrutura simples e direta para lógica condicional básica.
Pode ser mais intuitiva para devs familiarizados com estruturas de controle convencionais.        

'''