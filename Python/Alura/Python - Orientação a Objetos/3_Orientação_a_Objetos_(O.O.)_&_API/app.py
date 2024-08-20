import requests
import json

url  = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
'''O GET é um verbo do HTTP onde solicitamos um recurso.
   Quando acessamos esse endpoint, não esperamos uma página bonita, toda estilizada com CSS. Esperamos dados. Para conseguir solicitar esses dados, geralmente utilizamos o verbo GET.'''

print(response)
'''Quando se obtém um response [200] significa que a solicitação foi atendida com sucesso.'''

'''Exemplo de URL correta: '''

if response.status_code == 200:  #utilizando a função status_code para identificar a númeração correspontente
    dados_json = response.json() #utilizando .json() importamos o tipo de arquivo para Json.
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
    with open(nome_do_arquivo,'w') as arquivo_restaurante: #with open, permite manipular os arquivos também dentro da aplicação. #utilizamos também o "w" com abreviação da funação write(escrever)
        json.dump(dados,arquivo_restaurante,indent=4) #após importar a biblioteca Json, usamos a função dump(singular)
        #utilizamos 3 paramentos, os 'dados' recebidos do for, o nome do arquivo tratado 'arquivo_restaurante' e uma identação para organização 'indent=4'
        
'''Exemplo de URL incorreta:'''
# url = 'https://guilhermeonrails.github.io/api-restaurante/restaurantes.json'
# response = requests.get(url)
# print(response)
'''<Response [404]>'''