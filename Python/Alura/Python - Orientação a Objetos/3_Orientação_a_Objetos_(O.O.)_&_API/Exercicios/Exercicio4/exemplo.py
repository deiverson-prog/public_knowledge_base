'''Ao lidar com APIs e dados externos, é uma prática valiosa salvar e organizar esses dados para facilitar futuras análises ou utilizações. Existe uma biblioteca em Python chamada requests, que é uma biblioteca popular para fazer requisições HTTP. Ela simplifica o processo de enviar solicitações, seja para obter informações de uma API, interagir com serviços web ou realizar outras operações que envolvam comunicação via HTTP.

Faça uma requisição à API de restaurantes utilizando a biblioteca requests.'''

import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}

    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
    
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

else:
    print(f'O erro foi {response.status_code}')

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
