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

                        Entendendo os ambientes virtualizados

Venv - Ambiente Virtual Python

Oque é uma Venv?

Um Ambiente Virtual isolado

Comando para criar uma Venv:

python -m venv venv

descrição do comando:

-m indica que queremos criar um módulo de script,
 executar informações e utilizar esse script também. 
 
venv indica que queremos criar uma venv 

depois temos o nome (por padrão e boa prática mantemos o nome como Venv).

cadeia de arquivos criados:

Venv   -> Ambiente virtual isolado.
 Include -> Mantém o cabeçalho (o código C dos ambientes e módulos do projeto).
 Lib -> É responsável por armazenar todos os pacotes e dependências que instalamos no ambiente virtual.
  pip -> É responsável por fazer todas as instalações, além de outra versão do pip (À medida que instalamos módulos ou dependências, eles serão adicionados a essa pasta.)
 Scripts -> Scripts relacionados ao ambiente virtual.
  activate
  activate.bat
  activate.ps1
  deactivate.bat
 pyvenv.cfg ->  Esse arquivo, basicamente, só dará as informações do nosso ambiente virtual.

Ativando a Venv (windows):

comando:
venv/Scripts/activate.bat

Ativando a Venv (Mac or Linux):

comando:
source venv/bin/activate

Desativando a Venv (windows):

comando:
deactivate

Ativando a Venv (Mac or Linux):

comando:
deactivate

Instalação de bibliotecas e isolamento de dependências

Utilizar pip install + biblioteca desejada.
Exemplo: pip install requests (biblioteca para )

Verificar as bibliotecas instaladas: 
Comando:

pip freeze

Listando o que foi instalado:

Comando:
pip freeze > requirements.txt

Virtualenv  x   Venv

A venv é uma biblioteca integrada ao Python 3.3 e versões posteriores, 
enquanto virtualenv é uma ferramenta externa que precisa ser instalada separadamente. 
Para versões mais recentes do Python (3.5 e acima), venv é recomendada, pois oferece 
funcionalidades semelhantes às do virtualenv e está disponível de forma padrão.


Escopo de Funcionalidades:
virtualenv é conhecido por ser mais rico em funcionalidades e oferecer suporte a casos 
de uso mais avançados.

Suporte a Diferentes Interpretadores Python:
A virtualenv é mais flexível quando se trata de trabalhar com diferentes versões do Python e 
interpretadores alternativos. 
Ele pode ser utilizado para criar ambientes virtuais para várias versões do Python, 
incluindo versões mais antigas que ainda são compatíveis com o virtualenv.

Integração com Outras Linguagens:
A virtualenv é capaz de integrar-se a outras linguagens além do Python, proporcionando uma 
solução mais abrangente para projetos que envolvem múltiplas linguagens de programação. 
Isso pode ser particularmente útil em ambientes de desenvolvimento complexos.

Isolamento de Ambientes Virtuais:
Embora ambos venv e virtualenv proporcionem isolamento de ambientes virtuais, virtualenv é 
conhecido por ter recursos adicionais para lidar com situações mais complexas, garantindo uma 
separação eficiente de dependências entre diferentes projetos.

Ativação do Ambiente Virtual:
Para virtualenv, você utiliza os comandos: 

Comando (MacOS or Linux):
source <env>/bin/activate

Comando (Windows):
<env>\Scripts\activate

Para venv, você utiliza os comandos: 

Comando (MacOS or Linux):
source <env>/bin/activate

Comando (Windows):
<env>\Scripts\activate

A virtualenv oferece mais opções avançadas durante a ativação do ambiente virtual. 
Além dos comandos tradicionais, ele permite personalizações adicionais, oferecendo maior 
controle sobre o ambiente ativado.

Descontinuação do Python 2:
É importante mencionar que com o fim do suporte ao Python 2, o venv tornou-se mais viável, 
uma vez que virtualenv era frequentemente utilizado para criar ambientes virtuais para versões 
mais antigas do Python.

Se você está usando Python 3.3 ou uma versão mais recente, o uso de venv é recomendado 
por ser uma solução integrada. No entanto, se você precisa de funcionalidades avançadas 
ou está trabalhando com versões mais antigas do Python, o virtualenv pode ser uma escolha 
mais apropriada.

                        O que é API?
Protocolo HTTP 
É uma forma de compartilhar recursos e informações de hipertexto. Uma das formas que temos 
para utilizar essa comunicação é através de uma API.

API, requisição e resposta

Application Programming Interface (API)

É uma interface de programação de aplicativos usada no desenvolvimento web e de software. Permite que diferentes aplicativos interajam por meio de solicitações e compartilhem dados de forma segura e eficiente. Uma API inclui regras e protocolos que ajudam a usar as funções de um aplicativo dentro do outro. Graças às APIs, você pode fazer compras online, assistir a vídeos incorporados e usar dados de GPS para criar uma rota de corrida.

Os termos request (requisição) e response (resposta), que são muito importantes para a 
carreira de back-end.

O servidor recebe uma requisição, processa essa requisição e 
devolve uma resposta com os dados que queremos.


Arquivo JSON  (link: https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json)

Requisição

Importamos a biblioteca requests para poder acessar uma variável em JSON pela URL como 'strings'.
No requests existe uma função chamada get() Dentro dos parênteses, vamos colocar a url.
Portanto, a variável response vai receber requests.get(url). 

O que significa esse GET?
O GET é um verbo do HTTP onde solicitamos um recurso.

https://guilhermeonrails simboliza um endpoint(Uma rede é composta por um grupo de dispositivos que trocam dados)

Todas as vezes que fazemos uma requisição, temos um intervalo (range) de números com os quais podemos saber se deu certo, se deu errado e o que deu de errado nessa solicitação.

Exemplo de URL correta: (link: https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json)
status code <Response [200]>

Exemplo de URL incorreta: (link: https://guilhermeonrails.github.io/api-restaurante/restaurantes.json)
status code <Response [404]>

Em PY temos vários frameworks do Python. No caso, temos, por exemplo, o Django, o Flask e o FastAPI.

                        Usando o FastAPI


TIPOS DE FRAMEWORKS

Flask: Simplicidade e Flexibilidade

Flask é conhecido por sua simplicidade e facilidade de uso. É uma escolha popular para projetos menores ou para desenvolvedores que preferem ter mais controle sobre os componentes que utilizam. Com Flask, você pode rapidamente criar uma API básica com poucas linhas de código, sendo uma excelente opção para prototipagem rápida, como mostrado no código a seguir:

from flask import Flask

app = Flask(__name__)

@app.route('/api')
def ola_mundo():
    return 'Olá Mundo!'

if __name__ == '__main__':
    app.run()


Django: Estrutura Poderosa e Convenções Batteries-Included

O Django é uma escolha robusta para projetos mais complexos e de maior escala. Ele fornece uma estrutura completa que inclui um sistema de administração, ORM (Object-Relational Mapping) e muitos outros recursos. Apesar de ser um framework mais pesado em comparação com Flask, o Django oferece uma solução abrangente para desenvolvimento web. Um exemplo de como criar uma API simples em Django está no código a seguir:

from django.http import JsonResponse
from django.views import View

class MinhaAPI(View):
    def get(self, request):
        return JsonResponse({'message': 'Olá mundo!'})


FastAPI: Alta Performance e Documentação Automática

Como vimos, FastAPI é uma escolha moderna, otimizada para alta performance e fácil utilização. Ele utiliza a tipagem de dados do Python 3.7+ para oferecer uma documentação automática excepcional, facilitando a compreensão e utilização da API.

from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def ola_mundo():
    return {"message": "Olá Mundo!"}

Cada framework tem seus pontos fortes, e a seleção depende das necessidades particulares das pessoas desenvolvedoras e do contexto do projeto.

'''