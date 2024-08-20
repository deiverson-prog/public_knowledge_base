'''FastAPI é um framework moderno e rápido para construir APIs web com Python. Com o ele, você pode criar uma variedade de aplicativos e serviços, especialmente focados em APIs. Ao desenvolver aplicações web utilizando o framework FastAPI, é comum interagir com serviços externos por meio de requisições HTTP.

Vamos definir um endpoint simples que retorna uma saudação quando acessado?'''

from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação!
    '''
    return {'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes  
    
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })

        return {'Restaurante':restaurante,'Cardapio':dados_restaurante}        
    else: 
        return {'Erro':f'{response.status_code} - {response.text}'}
