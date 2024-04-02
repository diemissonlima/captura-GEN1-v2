import requests
import pandas as pd
import sqlite3


colunas = [
    "dex", "nome", "tipo_1", "tipo_2", "exp_base"
]

valores = []

# api = f"https://pokeapi.co/api/v2/pokemon/6"
# res = requests.get(api)
# poke = res.json()
#
# print(poke['types'][1]["type"]["name"])

# for c in range(152, 251 + 1):
#     api = f"https://pokeapi.co/api/v2/pokemon/{c}"
#     res = requests.get(api)
#     poke = res.json()
#
#     dex = f'poke-{c}'
#     partes = dex.split("-")
#     if len(partes) >= 2:
#         numero = partes[1]
#         numero_formatado = f'{int(numero):03d}'
#         new_dex = f'poke-{numero_formatado}'
#     nome = f'{poke["forms"][0]["name"]}'.capitalize()
#     if len(poke['types']) == 1:
#         tipo_1 = f'{poke["types"][0]["type"]["name"]}'.capitalize()
#         tipo_2 = tipo_1
#     else:
#         tipo_2 = f'{poke["types"][1]["type"]["name"]}'.capitalize()
#
#     valores.append([new_dex, nome, tipo_1, tipo_2, poke['base_experience']])
#
#
# tabela = pd.DataFrame(columns=colunas, data=valores)
# tabela.to_excel('pokemons.xlsx', index=False)
#
# print('Dados Inseridos com sucesso')

# Conectar ao banco de dados (cria o banco de dados se ele não existir)
conexao = sqlite3.connect('pokemon - Copia.db')

# cursor pra fazer operações no banco de dados
cursor = conexao.cursor()

tabela = pd.read_excel('pokemons.xlsx')

for index, item in tabela.iterrows():
    cursor.execute(f"INSERT INTO pokemon (poke_dex, nome, tipo_1, tipo_2, exp_base)"
                   f"VALUES ('{item['dex']}', '{item['nome']}, '{item['tipo_1']}', '{item['tipo_2']}',"
                   f"'{item['exp_base']}')")
    conexao.commit()

print("Itens inseridos com sucesso")
