import random
from random import choice, randint
from time import sleep
from datetime import datetime as dt
import sqlite3

# Conectar ao banco de dados (cria o banco de dados se ele não existir)
conexao = sqlite3.connect('pokemon testes.db')

# cursor pra fazer operações no banco de dados
cursor = conexao.cursor()

pokemon = {}
inventario = {}
player = {}
rotas = {
    'rota_1': [], 'rota_2': [], 'rota_3': [], 'rota_4': [], 'rota_5': [],
    'rota_6': [], 'rota_7': [], 'rota_8': [], 'rota_9': [], 'rota_10': [],
    'rota_11': [], 'rota_12': [], 'rota_13': [], 'rota_14': [], 'rota_15': []
}
level_dict = {
    '1': 400, '2': 440, '3': 484, '4': 532, '5': 585, '6': 644, '7': 708, '8': 779, '9': 857, '10': 943,
    '11': 1037, '12': 1141, '13': 1255, '14': 1380, '15': 1518, '16': 1670, '17': 1837, '18': 2021, '19': 2223,
    '20': 2446, '21': 2690, '22': 2960, '23': 3256, '24': 3581, '25': 3993, '26': 4392, '27': 4831, '28': 5314,
    '29': 5846, '30': 6430, '31': 7073, '32': 7780, '33': 8558, '34': 9414, '35': 10355, '36': 11390, '37': 12529,
    '38': 13782, '39': 15161, '40': 16677, '41': 18344, '42': 20179, '43': 22197, '44': 24416, '45': 26858,
    '46': 29544, '47': 32498, '48': 35748, '49': 39323, '50': 43256
}

# recuperando informações do banco de dados da tabela pokemon
cursor = conexao.execute('SELECT * FROM pokemon')
resultados = cursor.fetchall()
for j in resultados:
    num, dex, nome, tipo_1, tipo_2, evo, lendario, apareceu, copy, total_copy, shiny_apareceu, copy_shiny, \
        total_shinycopy, exp_base, catch_rate, peso = j
    pokemon[dex] = {
        'id': dex, 'nome': nome, 'tipo_1': tipo_1, 'tipo_2': tipo_2, 'evo': evo, 'lendario': lendario,
        'apareceu': apareceu, 'copy': copy, 'total_copy': total_copy, 'shiny_apareceu': shiny_apareceu,
        'copy_shiny': copy_shiny, 'total_shinycopy': total_shinycopy, 'exp_base': exp_base, 'catch_rate': catch_rate,
        'peso': peso
    }

# recuperando informações do banco de dados da tabela inventario
cursor = conexao.execute('SELECT * FROM inventario')
item_inventario = cursor.fetchall()
for itens in item_inventario:
    id_item, nome_item, tipo_item, qtde, rate_captura, rate_bonus, preco_compra, preco_venda = itens
    inventario[nome_item] = {
        'id': id_item, 'nome_item': nome_item.title(), 'tipo_item': tipo_item, 'qtde': qtde,
        'rate_captura': rate_captura, 'rate_bonus': rate_bonus, 'preco_compra': preco_compra,
        'preco_venda': preco_venda
    }

# recuperando informações do banco de dados da tabela jogador
cursor = conexao.execute('SELECT * FROM jogador')
player_info = cursor.fetchall()
for itens in player_info:
    item, quantidade = itens
    player[item] = {
        'info': quantidade
    }

# # lista de pokemon que é usada como base pra adicionar pokemon ja capturados na lista de capturados quando recuperar
# # os dados a partir do banco de dados, nela vai todos os pokemons
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
    pokemon['poke-151'], pokemon['poke-152'], pokemon['poke-153'], pokemon['poke-154'], pokemon['poke-155'],
    pokemon['poke-156'], pokemon['poke-157'], pokemon['poke-158'], pokemon['poke-159'], pokemon['poke-160'],
    pokemon['poke-161'], pokemon['poke-162'], pokemon['poke-163'], pokemon['poke-164'], pokemon['poke-165'],
    pokemon['poke-166'], pokemon['poke-167'], pokemon['poke-168'], pokemon['poke-169'], pokemon['poke-170'],
    pokemon['poke-171'], pokemon['poke-172'], pokemon['poke-173'], pokemon['poke-174'], pokemon['poke-175'],
    pokemon['poke-176'], pokemon['poke-177'], pokemon['poke-178'], pokemon['poke-179'], pokemon['poke-180'],
    pokemon['poke-181'], pokemon['poke-182'], pokemon['poke-183'], pokemon['poke-184'], pokemon['poke-185'],
    pokemon['poke-186'], pokemon['poke-187'], pokemon['poke-188'], pokemon['poke-189'], pokemon['poke-190'],
    pokemon['poke-191'], pokemon['poke-192'], pokemon['poke-193'], pokemon['poke-194'], pokemon['poke-195'],
    pokemon['poke-196'], pokemon['poke-197'], pokemon['poke-198'], pokemon['poke-199'], pokemon['poke-200'],
    pokemon['poke-201'], pokemon['poke-202'], pokemon['poke-203'], pokemon['poke-204'], pokemon['poke-205'],
    pokemon['poke-206'], pokemon['poke-207'], pokemon['poke-208'], pokemon['poke-209'], pokemon['poke-210'],
    pokemon['poke-211'], pokemon['poke-212'], pokemon['poke-213'], pokemon['poke-214'], pokemon['poke-215'],
    pokemon['poke-216'], pokemon['poke-217'], pokemon['poke-218'], pokemon['poke-219'], pokemon['poke-220'],
    pokemon['poke-221'], pokemon['poke-222'], pokemon['poke-223'], pokemon['poke-224'], pokemon['poke-225'],
    pokemon['poke-226'], pokemon['poke-227'], pokemon['poke-228'], pokemon['poke-229'], pokemon['poke-230'],
    pokemon['poke-231'], pokemon['poke-232'], pokemon['poke-233'], pokemon['poke-234'], pokemon['poke-235'],
    pokemon['poke-236'], pokemon['poke-237'], pokemon['poke-238'], pokemon['poke-239'], pokemon['poke-240'],
    pokemon['poke-241'], pokemon['poke-242'], pokemon['poke-243'], pokemon['poke-244'], pokemon['poke-245'],
    pokemon['poke-246'], pokemon['poke-247'], pokemon['poke-248'], pokemon['poke-249'], pokemon['poke-250'],
    pokemon['poke-251']
]
drop_list = [
    inventario['pokeball'], inventario['greatball'], inventario['ultraball'], inventario['masterball'],
    inventario['pokeball fire'], inventario['pokeball water'], inventario['pokeball grass'],
    inventario['pokeball bug'], inventario['pokeball poison'], inventario['pokeball eletric'],
    inventario['pokeball ground'], inventario['pokeball fighting'], inventario['pokeball psychic'],
    inventario['pokeball rock'], inventario['pokeball ghost'], inventario['pokeball ice'],
    inventario['pokeball dragon'], inventario['pokeball flying'], inventario['pokeball fairy'],
    inventario['pokeball dark'], inventario['pokeball steel'],
    inventario['balm mushroom'], inventario['big nugget'], inventario['big pearl'], inventario['black flute'],
    inventario['blue flute'], inventario['comet shard'], inventario['nugget'], inventario['pearl string'],
    inventario['pretty feather'], inventario['rare bone'], inventario['red flute'], inventario['relic band'],
    inventario['relic cooper'], inventario['relic cooper'], inventario['relic crown'], inventario['relic gold'],
    inventario['relic silver'], inventario['relic statue'], inventario['stardust'], inventario['yellow flute'],
    inventario['white flute']
]
rota = [
    rotas['rota_1'], rotas['rota_2'], rotas['rota_3'], rotas['rota_4'], rotas['rota_5'],
    rotas['rota_6'], rotas['rota_7'], rotas['rota_8'], rotas['rota_9'], rotas['rota_10'],
    rotas['rota_11'], rotas['rota_12'], rotas['rota_13'], rotas['rota_14'], rotas['rota_15']
]

index = 1
while len(pokemons) != 0:
    random_poke = choice(pokemons)
    rotas[f'rota_{index}'].append(random_poke)
    pokemons.remove(random_poke)
    index += 1
    if index > 15:
        index = 1

rota_atual = rotas['rota_1']
mapa_atual = 'Rota 1'


def drop_itens():
    random_number = randint(36, 36)
    item_dropado = drop_list[random_number]
    print(item_dropado['nome_item'])


drop_itens()
