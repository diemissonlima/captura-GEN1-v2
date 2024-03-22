import random
from random import choice, randint, randrange
from time import sleep
from datetime import datetime as dt
import sqlite3


# Conectar ao banco de dados (cria o banco de dados se ele não existir)
conexao = sqlite3.connect('pokemon.db')

# cursor pra fazer operações no banco de dados
cursor = conexao.cursor()

# cria a tabela pokemon no banco de dados caso nao exista
cursor.execute('''CREATE TABLE IF NOT EXISTS pokemon
                             (nome TEXT, id INTEGER, copy INTEGER, total_copy INTEGER, evo TEXT, apareceu INTEGER)''')

pokemon = {}
inventario = {}
player = {}

# recuperando informações do banco de dados da tabela pokemon
cursor = conexao.execute('SELECT * FROM pokemon')
resultados = cursor.fetchall()
for j in resultados:
    num, dex, nome, tipo_pokemon, evo, lendario, apareceu, copy, total_copy, shiny_apareceu, copy_shiny, \
        total_shinycopy, exp_base, catch_rate = j
    pokemon[dex] = {
        'id': dex, 'nome': nome, 'tipo_pokemon': tipo_pokemon, 'evo': evo, 'lendario': lendario, 'apareceu': apareceu,
        'copy': copy, 'total_copy': total_copy, 'shiny_apareceu': shiny_apareceu, 'copy_shiny': copy_shiny,
        'total_shinycopy': total_shinycopy, 'exp_base': exp_base, 'catch_rate': catch_rate
    }

# recuperando informações do banco de dados da tabela inventario
cursor = conexao.execute('SELECT * FROM inventario')
item_inventario = cursor.fetchall()
for itens in item_inventario:
    nome_item, qtde, rate_captura = itens
    inventario[nome_item] = {
        'qtde': qtde, 'rate_captura': rate_captura
    }

# recuperando informações do banco de dados da tabela jogador
cursor = conexao.execute('SELECT * FROM jogador')
player_info = cursor.fetchall()
for itens in player_info:
    item, quantidade = itens
    player[item] = {
        'qtde': quantidade
    }


pokemons = [
    pokemon['poke-001'], pokemon['poke-002'], pokemon['poke-003'], pokemon['poke-004'], pokemon['poke-005'],
    pokemon['poke-006'], pokemon['poke-007'], pokemon['poke-008'], pokemon['poke-009'], pokemon['poke-010'],
    pokemon['poke-011'], pokemon['poke-012'], pokemon['poke-013'], pokemon['poke-014'], pokemon['poke-015'],
    pokemon['poke-016'], pokemon['poke-017'], pokemon['poke-018'], pokemon['poke-019'], pokemon['poke-020'],
    pokemon['poke-021'], pokemon['poke-022'], pokemon['poke-023'], pokemon['poke-024'], pokemon['poke-025'],
    pokemon['poke-026'], pokemon['poke-027'], pokemon['poke-028'], pokemon['poke-029'], pokemon['poke-030'],
    pokemon['poke-031'], pokemon['poke-032'], pokemon['poke-033'], pokemon['poke-034'], pokemon['poke-035'],
    pokemon['poke-036'], pokemon['poke-037'], pokemon['poke-038'], pokemon['poke-039'], pokemon['poke-040'],
    pokemon['poke-041'], pokemon['poke-042'], pokemon['poke-043'], pokemon['poke-044'], pokemon['poke-045'],
    pokemon['poke-046'], pokemon['poke-047'], pokemon['poke-048'], pokemon['poke-049'], pokemon['poke-050'],
    pokemon['poke-051'], pokemon['poke-052'], pokemon['poke-053'], pokemon['poke-054'], pokemon['poke-055'],
    pokemon['poke-056'], pokemon['poke-057'], pokemon['poke-058'], pokemon['poke-059'], pokemon['poke-060'],
    pokemon['poke-061'], pokemon['poke-062'], pokemon['poke-063'], pokemon['poke-064'], pokemon['poke-065'],
    pokemon['poke-066'], pokemon['poke-067'], pokemon['poke-068'], pokemon['poke-069'], pokemon['poke-070'],
    pokemon['poke-071'], pokemon['poke-072'], pokemon['poke-073'], pokemon['poke-074'], pokemon['poke-075'],
    pokemon['poke-076'], pokemon['poke-077'], pokemon['poke-078'], pokemon['poke-079'], pokemon['poke-080'],
    pokemon['poke-081'], pokemon['poke-082'], pokemon['poke-083'], pokemon['poke-084'], pokemon['poke-085'],
    pokemon['poke-086'], pokemon['poke-087'], pokemon['poke-088'], pokemon['poke-089'], pokemon['poke-090'],
    pokemon['poke-091'], pokemon['poke-092'], pokemon['poke-093'], pokemon['poke-094'], pokemon['poke-095'],
    pokemon['poke-096'], pokemon['poke-097'], pokemon['poke-098'], pokemon['poke-099'], pokemon['poke-100'],
    pokemon['poke-101'], pokemon['poke-102'], pokemon['poke-103'], pokemon['poke-104'], pokemon['poke-105'],
    pokemon['poke-106'], pokemon['poke-107'], pokemon['poke-108'], pokemon['poke-109'], pokemon['poke-110'],
    pokemon['poke-111'], pokemon['poke-112'], pokemon['poke-113'], pokemon['poke-114'], pokemon['poke-115'],
    pokemon['poke-116'], pokemon['poke-117'], pokemon['poke-118'], pokemon['poke-119'], pokemon['poke-120'],
    pokemon['poke-121'], pokemon['poke-122'], pokemon['poke-123'], pokemon['poke-124'], pokemon['poke-125'],
    pokemon['poke-126'], pokemon['poke-127'], pokemon['poke-128'], pokemon['poke-129'], pokemon['poke-130'],
    pokemon['poke-131'], pokemon['poke-132'], pokemon['poke-133'], pokemon['poke-134'], pokemon['poke-135'],
    pokemon['poke-136'], pokemon['poke-137'], pokemon['poke-138'], pokemon['poke-139'], pokemon['poke-140'],
    pokemon['poke-141'], pokemon['poke-142'], pokemon['poke-143'], pokemon['poke-144'], pokemon['poke-145'],
    pokemon['poke-146'], pokemon['poke-147'], pokemon['poke-148'], pokemon['poke-149'], pokemon['poke-150'],
    pokemon['poke-151']
]

rotas = {
    'rota_1': [], 'rota_2': [], 'rota_3': [], 'rota_4': [], 'rota_5': [],
    'rota_6': [], 'rota_7': [], 'rota_8': [], 'rota_9': [], 'rota_10': []
}

index = 1
while len(pokemons) != 0:
    random_poke = choice(pokemons)
    rotas[f'rota_{index}'].append(random_poke)
    pokemons.remove(random_poke)
    index += 1
    if index > 10:
        index = 1

for j in rotas.values():
    print(j[1])


# for j in range(1, 10 + 1):
#     random_poke = choice(pokemons)
#     rotas['rota_1'].append(random_poke)
#     pokemons.remove(random_poke)
#
# for i in rotas['rota_1']:
#     print(i['id'], i['nome'])


rotas2 = {
    'rota_1': [
        pokemon['poke-086'], pokemon['poke-013'], pokemon['poke-039'], pokemon['poke-016'], pokemon['poke-046'],
        pokemon['poke-063'], pokemon['poke-021'], pokemon['poke-102']
    ],
    'rota_2': [
        pokemon['poke-092'], pokemon['poke-056'], pokemon['poke-131'], pokemon['poke-140'], pokemon['poke-079'],
        pokemon['poke-001'], pokemon['poke-027']
    ],
    'rota_3': [
        pokemon['poke-120'], pokemon['poke-100'], pokemon['poke-090'], pokemon['poke-025'], pokemon['poke-106'],
        pokemon['poke-032'], pokemon['poke-088']
    ],
    'rota_4': [
        pokemon['poke-118'], pokemon['poke-128'], pokemon['poke-054'], pokemon['poke-029'], pokemon['poke-043'],
        pokemon['poke-019'], pokemon['poke-114']
    ],
    'rota_5': [
        pokemon['poke-096'], pokemon['poke-010'], pokemon['poke-127'], pokemon['poke-004'], pokemon['poke-147'],
        pokemon['poke-041'], pokemon['poke-060']
    ],
    'rota_6': [
        pokemon['poke-052'], pokemon['poke-124'], pokemon['poke-095'], pokemon['poke-143'], pokemon['poke-081'],
        pokemon['poke-023'], pokemon['poke-132']
    ],
    'rota_7': [
        pokemon['poke-129'], pokemon['poke-137'], pokemon['poke-142'], pokemon['poke-126'], pokemon['poke-083'],
        pokemon['poke-050'], pokemon['poke-123']
    ],
    'rota_8': [
        pokemon['poke-058'], pokemon['poke-066'], pokemon['poke-113'], pokemon['poke-035'], pokemon['poke-115'],
        pokemon['poke-138'], pokemon['poke-048']
    ],
    'rota_9': [
        pokemon['poke-072'], pokemon['poke-122'], pokemon['poke-074'], pokemon['poke-104'], pokemon['poke-077'],
        pokemon['poke-037'], pokemon['poke-116']
    ],
    'rota_10': [
        pokemon['poke-007'], pokemon['poke-069'], pokemon['poke-084'], pokemon['poke-098'], pokemon['poke-017'],
        pokemon['poke-108'], pokemon['poke-125']
    ]
}
