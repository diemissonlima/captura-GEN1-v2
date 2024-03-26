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
    num, dex, nome, tipo_1, tipo_2, evo, lendario, apareceu, copy, total_copy, shiny_apareceu, copy_shiny, \
        total_shinycopy, exp_base, catch_rate = j
    pokemon[dex] = {
        'id': dex, 'nome': nome, 'tipo_1': tipo_1, 'tipo_2': tipo_2, 'evo': evo, 'lendario': lendario,
        'apareceu': apareceu, 'copy': copy, 'total_copy': total_copy, 'shiny_apareceu': shiny_apareceu,
        'copy_shiny': copy_shiny, 'total_shinycopy': total_shinycopy, 'exp_base': exp_base, 'catch_rate': catch_rate
    }

# recuperando informações do banco de dados da tabela inventario
cursor = conexao.execute('SELECT * FROM inventario')
item_inventario = cursor.fetchall()
for itens in item_inventario:
    nome_item, qtde, rate_captura, preco_compra, preco_venda = itens
    inventario[nome_item] = {
        'nome_item': nome_item.capitalize(), 'qtde': qtde, 'rate_captura': rate_captura, 'preco_compra': preco_compra,
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


# função pra validar as opções do usuário, nao deixando ele digitar nada diferente de um numero inteiro
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO, digite uma opção válida!')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


def pokemart():
    print('Bemvindo ao Pokémart')
    while True:
        opcao = leiaInt('O que você deseja? [ 1 ] Comprar [ 2 ] Vender [ 3 ] Sair: ')
        if opcao == 1:
            print('Itens Disponíveis:')
            print(f'1 - PokeBall P$ 50\n2 - GreatBall P$ 120\n'
                  f'3 - UltraBall P$ 200\n4 - MasterBall P$ 1500')
            compra = leiaInt("O que deseja comprar? ")
            match compra:
                case 1:
                    item_target = inventario['pokeball']
                case 2:
                    item_target = inventario['greatball']
                case 3:
                    item_target = inventario['ultraball']
                case 4:
                    item_target = inventario['masterball']

            print(f"PokéCréditos Disponíveis: P$ {inventario['poke_creditos']['qtde']}")
            qtde_compra = leiaInt("Digite a quantidade desejada: ")
            valor_compra = int(qtde_compra * item_target['preco_compra'])

            if valor_compra > inventario['poke_creditos']['qtde']:
                print('-=' * 20)
                print('\033[1;31mPoké Creditos insuficientes\033[m'.center(40))
                print('-=' * 20)
            else:
                inventario['poke_creditos']['qtde'] -= valor_compra
                item_target['qtde'] += qtde_compra
                print('-=' * 20)
                print(f'\033[1;32m{item_target["nome_item"]} Comprada: {qtde_compra}\nValor Compra: P$ {valor_compra}\n'
                      f'Poké Créditos Restantes: P$ {inventario["poke_creditos"]["qtde"]}\033[m')
                print('-=' * 20)

        elif opcao == 2:
            break

        elif opcao == 3:
            break


pokemart()
