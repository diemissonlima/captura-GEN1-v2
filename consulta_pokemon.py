import requests
import pandas as pd
import sqlite3


colunas = [
    "dex", "nome", "tipo_1", "tipo_2", "exp_base", "peso"
]

valores = []

# api = f"https://pokeapi.co/api/v2/pokemon/143"
# res = requests.get(api)
# poke = res.json()
#
# print(poke['types'][0]['type']['name'])
# print(poke['weight'] / 10, 'KG')

for c in range(1, 251 + 1):
    api = f"https://pokeapi.co/api/v2/pokemon/{c}"
    res = requests.get(api)
    poke = res.json()

    tipo_1 = ''
    tipo_2 = ''
    dex = f'poke-{c}'
    partes = dex.split("-")
    if len(partes) >= 2:
        numero = partes[1]
        numero_formatado = f'{int(numero):03d}'
        new_dex = f'poke-{numero_formatado}'
    nome = f'{poke["forms"][0]["name"]}'.capitalize()
    if len(poke['types']) == 2:
        tipo_1 = f'{poke["types"][0]["type"]["name"]}'.capitalize()
        tipo_2 = f'{poke["types"][1]["type"]["name"]}'.capitalize()
    else:
        tipo_1 = f'{poke["types"][0]["type"]["name"]}'.capitalize()
        tipo_2 = tipo_1
    peso = poke['weight'] / 10

    valores.append([new_dex, nome, tipo_1, tipo_2, poke['base_experience'], peso])


tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel('pokemons.xlsx', index=False)

print('Excel criado com sucesso')

# # Conectar ao banco de dados (cria o banco de dados se ele não existir)
# conexao = sqlite3.connect('pokemon - Copia.db')
#
# # cursor pra fazer operações no banco de dados
# cursor = conexao.cursor()
#
# tabela = pd.read_excel('pokemons.xlsx')
#
# for index, item in tabela.iterrows():
#     cursor.execute(f"INSERT INTO pokemon (poke_dex, nome, tipo_1, tipo_2, evo, lendario, exp_base, catch_rate)"
#                    f"VALUES ('{item['dex']}', '{item['nome']}', '{item['tipo_1']}', '{item['tipo_2']}',"
#                    f"'{item['evo']}', '{item['lendario']}', '{item['exp_base']}', '{item['catch_rate']}')")
#     conexao.commit()
#
# print("Itens inseridos com sucesso")
