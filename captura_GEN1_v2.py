import random
from random import choice, randint
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
    pokemon['poke-151']
]

rotas = {
    'rota_1': [], 'rota_2': [], 'rota_3': [], 'rota_4': [], 'rota_5': [],
    'rota_6': [], 'rota_7': [], 'rota_8': [], 'rota_9': [], 'rota_10': [],
    'rota_11': [], 'rota_12': [], 'rota_13': [], 'rota_14': [], 'rota_15': []
}

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

# lista com a evolucao dos pokemon capturados a partir da lista pokes
evolucoes = [
    pokemon['poke-002'], pokemon['poke-003'], pokemon['poke-005'], pokemon['poke-006'], pokemon['poke-008'],
    pokemon['poke-009'], pokemon['poke-001'], pokemon['poke-011'], pokemon['poke-012'], pokemon['poke-014'],
    pokemon['poke-015'], pokemon['poke-017'], pokemon['poke-018'], pokemon['poke-020'], pokemon['poke-022'],
    pokemon['poke-024'], pokemon['poke-026'], pokemon['poke-028'], pokemon['poke-030'], pokemon['poke-031'],
    pokemon['poke-033'], pokemon['poke-034'], pokemon['poke-036'], pokemon['poke-038'], pokemon['poke-040'],
    pokemon['poke-042'], pokemon['poke-044'], pokemon['poke-045'], pokemon['poke-047'], pokemon['poke-049'],
    pokemon['poke-051'], pokemon['poke-053'], pokemon['poke-055'], pokemon['poke-057'], pokemon['poke-059'],
    pokemon['poke-061'], pokemon['poke-062'], pokemon['poke-064'], pokemon['poke-065'], pokemon['poke-067'],
    pokemon['poke-068'], pokemon['poke-070'], pokemon['poke-071'], pokemon['poke-073'], pokemon['poke-075'],
    pokemon['poke-076'], pokemon['poke-078'], pokemon['poke-080'], pokemon['poke-082'], pokemon['poke-085'],
    pokemon['poke-087'], pokemon['poke-089'], pokemon['poke-091'], pokemon['poke-093'], pokemon['poke-094'],
    pokemon['poke-097'], pokemon['poke-099'], pokemon['poke-101'], pokemon['poke-103'], pokemon['poke-110'],
    pokemon['poke-112'], pokemon['poke-117'], pokemon['poke-119'], pokemon['poke-121'], pokemon['poke-130'],
    pokemon['poke-134'], pokemon['poke-025'], pokemon['poke-136'], pokemon['poke-135'], pokemon['poke-139'],
    pokemon['poke-141'], pokemon['poke-148'], pokemon['poke-149']
]

# lista dos pokemon lendario que sao adicionados a lista pokes apos atender uma condição
lendarios = [
    pokemon['poke-144'], pokemon['poke-145'], pokemon['poke-146'], pokemon['poke-150'], pokemon['poke-151']
]

level_dict = {
    '1': 400, '2': 440, '3': 484, '4': 532, '5': 585, '6': 644, '7': 708, '8': 779, '9': 857, '10': 943,
    '11': 1037, '12': 1141, '13': 1255, '14': 1380, '15': 1518, '16': 1670, '17': 1837, '18': 2021, '19': 2223,
    '20': 2446, '21': 2690, '22': 2960, '23': 3256, '24': 3581, '25': 3993, '26': 4392, '27': 4831, '28': 5314,
    '29': 5846, '30': 6430, '31': 7073, '32': 7780, '33': 8558, '34': 9414, '35': 10355, '36': 11390, '37': 12529,
    '38': 13782, '39': 15161, '40': 16677, '41': 18344, '42': 20179, '43': 22197, '44': 24416, '45': 26858,
    '46': 29544, '47': 32498, '48': 35748, '49': 39323, '50': 43256
}


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


# funcao que salva os dados no banco de dados
def salvar_dados():
    # atualiza as informações dos pokemon no banco de dados
    for p in pokemon.values():
        cursor.execute(f"UPDATE pokemon SET copy = {p['copy']}, apareceu = {p['apareceu']}, "
                       f"total_copy = {p['total_copy']}, shiny_apareceu = {p['shiny_apareceu']}, "
                       f"copy_shiny = {p['copy_shiny']}, total_shinycopy = {p['total_shinycopy']} "
                       f"WHERE nome = '{p['nome']}'")
        conexao.commit()

    cursor.execute(f"UPDATE jogador SET quantidade = {player['turno']['info']} WHERE item = 'turno'")
    cursor.execute(f"UPDATE jogador SET quantidade = {player['nivel_atual']['info']} WHERE item = 'nivel_atual'")
    cursor.execute(f"UPDATE jogador SET quantidade = {player['xp_atual']['info']} WHERE item = 'xp_atual'")

    cursor.execute(f"UPDATE inventario SET quantidade = {inventario['pokeball']['qtde']} WHERE item = 'pokeball'")
    cursor.execute(f"UPDATE inventario SET quantidade = {inventario['greatball']['qtde']} WHERE item = 'greatball'")
    cursor.execute(f"UPDATE inventario SET quantidade = {inventario['ultraball']['qtde']} WHERE item = 'ultraball'")
    cursor.execute(f"UPDATE inventario SET quantidade = {inventario['masterball']['qtde']} WHERE item = 'masterball'")
    cursor.execute(
        f"UPDATE inventario SET quantidade = {inventario['poke_creditos']['qtde']} WHERE item = 'poke_creditos'")


# reinicia o jogo com os valores padrao de cada coluna
def reiniciar_jogo():
    cursor.execute(f"UPDATE pokemon SET copy = {0}, apareceu = {0}, total_copy = {0}, "
                   f"shiny_apareceu = {0}, copy_shiny = {0}, total_shinycopy = {0}")

    cursor.execute(f"UPDATE inventario SET quantidade = {10} WHERE item = 'pokeball'")
    cursor.execute(f"UPDATE inventario SET quantidade = {0} WHERE item = 'greatball'")
    cursor.execute(f"UPDATE inventario SET quantidade = {0} WHERE item = 'ultraball'")
    cursor.execute(f"UPDATE inventario SET quantidade = {0} WHERE item = 'masterball'")
    cursor.execute(f"UPDATE inventario SET quantidade = {0} WHERE item = 'poke_creditos'")

    cursor.execute(f"UPDATE jogador SET quantidade = {0} WHERE item = 'turno'")
    cursor.execute(f"UPDATE jogador SET quantidade = {1} WHERE item = 'nivel_atual'")
    cursor.execute(f"UPDATE jogador SET quantidade = {0} WHERE item = 'xp_atual'")

    cursor.execute(f"DELETE from registro_captura WHERE id_log > 0")

    cursor.execute(f"UPDATE sqlite_sequence set seq = {0} WHERE name = 'registro_captura'")

    conexao.commit()


def registrar_captura(pokemon_selvagem, capturado, shiny, pokebola_usada):
    data_atual = dt.now()
    data = str(data_atual)
    cursor.execute(f"INSERT INTO registro_captura (data, hora, numero_dex, nome_pokemon, tipo_1, tipo_2, "
                   f"capturado, shiny, pokebola_usada)"
                   f"VALUES ('{data[:10]}', '{data[11:19]}', '{pokemon_selvagem['id']}', '{pokemon_selvagem['nome']}',"
                   f"'{pokemon_selvagem['tipo_1']}', '{pokemon_selvagem['tipo_2']}', '{capturado}', '{shiny}', "
                   f"'{pokebola_usada}')")
    conexao.commit()


# função que gera encontros com pokémons aleatórios
def encontrar_pokemon():
    while True:
        capturados_rota = 0
        for j in rota_atual:
            if j['total_copy'] > 0 or j['total_shinycopy'] > 0:
                capturados_rota += 1

        player['turno']['info'] += 1
        shiny = randint(1, 10)
        print('-=' * 20)
        print(f'>>> Mapa Atual: {mapa_atual} <<<'.center(40))
        print(f'Pokemons Capturados na {mapa_atual}: {capturados_rota} / {len(rota_atual)}'.center(40))
        print('-=' * 20)
        input(f'{player["turno"]["info"]}º Turno - Pressione ENTER para começar!')
        print('Um Pokémon selvagem apareceu!')
        sleep(3)
        poke_selvagem = choice(rota_atual)

        if poke_selvagem['lendario'] == 'True':
            print('Encontrou um Pokémon LENDÁRIO', end=' ')
            if shiny == 5:
                print(f'SHINY!!!', end='')
                print()
                poke_selvagem["shiny_apareceu"] += 1
            else:
                poke_selvagem["apareceu"] += 1
            print('\nPokémons Lendário só podem ser capturados com Master Ball')
            print(f'\033[1;33m>> {poke_selvagem["nome"]} << apareceu!\033[m')
            print('-=' * 20)
        else:
            print('-=' * 20)
            if shiny == 5:
                print(f'\033[1;33mEncontrou um >> {poke_selvagem["nome"]} SHINY!!! <<\033[m'.center(50))
                if poke_selvagem['tipo_2'] == poke_selvagem['tipo_1']:
                    print(f'\033[1;33mTipo: {poke_selvagem["tipo_1"]}\033[m'.center(50))
                else:
                    print(f'\033[1;33mTipo: {poke_selvagem["tipo_1"]}/{poke_selvagem["tipo_2"]}\033[m'.center(50))
                poke_selvagem["shiny_apareceu"] += 1
            else:
                print(f'\033[1;33mEncontrou um >> {poke_selvagem["nome"]} <<\033[m'.center(50))
                if poke_selvagem['tipo_2'] == poke_selvagem['tipo_1']:
                    print(f'\033[1;33mTipo: {poke_selvagem["tipo_1"]}\033[m'.center(50))
                else:
                    print(f'\033[1;33mTipo: {poke_selvagem["tipo_1"]}/{poke_selvagem["tipo_2"]}\033[m'.center(50))
                poke_selvagem["apareceu"] += 1

        if poke_selvagem['total_copy'] > 0 or poke_selvagem['total_shinycopy'] > 0:
            print(f'\033[1;32m>> Você ja capturou este Pokémon! <<\033[m\n'
                  f'>> Versão Normal apareceu {poke_selvagem["apareceu"]}x e capturou {poke_selvagem["copy"]}x <<\n'
                  f'>> Versão Shiny apareceu {poke_selvagem["shiny_apareceu"]}x e capturou {poke_selvagem["copy_shiny"]}x <<')
        else:
            print(f'\033[1;321m>> Ainda falta capturar este Pokémon! <<\033[m\n'
                  f'>> Versão Normal apareceu: {poke_selvagem["apareceu"]}x <<\n'
                  f'>> Versão Shiny apareceu: {poke_selvagem["shiny_apareceu"]}x <<')

        opcao = leiaInt('Deseja capturá-lo? [ 1 ] Sim [ 2 ] Nao: ')
        if opcao == 1:
            print(f'\033[1;31m[ 1 ] Pokébola: {inventario["pokeball"]["qtde"]:>5}\n'
                  f'[ 2 ] Great Ball: {inventario["greatball"]["qtde"]:>3}\n'
                  f'[ 3 ] Ultra Ball: {inventario["ultraball"]["qtde"]:>3}\033[m')
            usar_pokebola = leiaInt('Qual Pokébola usar?  ')
            match usar_pokebola:
                case 1:
                    pokeball = inventario["pokeball"]
                case 2:
                    pokeball = inventario["greatball"]
                case 3:
                    pokeball = inventario["ultraball"]

            captura(shiny, poke_selvagem, pokeball)

            opcao = leiaInt('Voltar ao Menu Principal? [ 1 ] Sim [ 2 ] Não: ')
            if opcao == 1:
                break


# função que executa a captura de um pokémon
def captura(is_shiny, poke_selvagem, pokeball):
    while True:
        random_number = random.random()
        chance_captura = ((poke_selvagem['catch_rate'] / 255) * pokeball['rate_captura'])
        # print(f'Random Number: {random_number:.2f}')
        # print(f"Chance Captura: {chance_captura:.2f}")
        if pokeball["qtde"] > 0:
            print(f'Voce joga a {pokeball["nome_item"]}!!!')

            if random_number <= chance_captura or random_number >= 1:

                for c in range(1, 6):
                    print(c, end='-> ', flush=True)
                    sleep(0.5)
                print()

                if is_shiny == 5:
                    print('-=' * 20)
                    poke_selvagem["copy_shiny"] += 1
                    poke_selvagem["total_shinycopy"] += 1
                    print(f"\033[1;32m{poke_selvagem['nome']} SHINY capturado!\033[m".center(50))
                    print(f"\033[1;32mVocê tem {poke_selvagem['copy_shiny']} cópia(s) SHINY!\033[m".center(50))
                    loot_poke_credito('cap_shiny')
                    ganhar_xp(poke_selvagem["exp_base"], 'shiny')
                    registrar_captura(poke_selvagem, 'True', 'True', pokeball['nome_item'])

                else:
                    print('-=' * 20)
                    poke_selvagem['copy'] += 1
                    poke_selvagem['total_copy'] += 1
                    print(f'\033[1;32m{poke_selvagem["nome"]} Capturado!\033[m'.center(50))
                    print(f"\033[1;32mVoce tem {poke_selvagem['copy']} cópia(s) dele!\033[m".center(50))
                    loot_poke_credito('cap_normal')
                    ganhar_xp(poke_selvagem["exp_base"], 'normal')
                    registrar_captura(poke_selvagem, 'True', 'False', pokeball['nome_item'])

                break

            else:
                if is_shiny != 5:
                    registrar_captura(poke_selvagem, 'False', 'False', pokeball['nome_item'])

                else:
                    registrar_captura(poke_selvagem, 'False', 'True', pokeball['nome_item'])

                for c in range(1, 6):
                    print(c, end='-> ', flush=True)
                    sleep(0.5)
                print()
                print('-=' * 20)
                print(f'\033[1;31m Que pena :-(, {poke_selvagem["nome"]} escapou!\033[m'.center(50))
                print('-=' * 20)

            pokeball['qtde'] -= 1

            retry = leiaInt('Tentar a captura novamente? [ 1 ] Sim [ 2 ] Nao: ')
            if retry == 1:
                print(f'\033[1;31m[ 1 ] Pokébola: {inventario["pokeball"]["qtde"]:>5}\n'
                      f'[ 2 ] Great Ball: {inventario["greatball"]["qtde"]:>3}\n'
                      f'[ 3 ] Ultra Ball: {inventario["ultraball"]["qtde"]:>3}\033[m')
                opcao = leiaInt('Escolha a Pokebola: ')
                match opcao:
                    case 1:
                        pokeball = inventario['pokeball']
                    case 2:
                        pokeball = inventario['greatball']
                    case 3:
                        pokeball = inventario['ultraball']
            elif retry == 2:
                break

        else:
            print("Voce nao tem pokebolas suficiente!")


def pokedex():
    opcao = leiaInt('Selecione a pokedex! [ 1 ] Normal [ 2 ] Shiny: ')
    print('-=' * 20)
    if opcao == 1:
        cursor = conexao.execute("SELECT * FROM registro_captura WHERE capturado = 'True' AND shiny = 'False' "
                                 "GROUP BY nome_pokemon ORDER BY numero_dex")
        count = conexao.execute("SELECT COUNT(DISTINCT nome_pokemon) FROM registro_captura where capturado = 'True' "
                                "AND shiny = 'False'")
        capturados = count.fetchall()
        qtde_capturados = capturados[0][0]
        print('Pokedéx Normal'.center(40))
        print('-=' * 20)
    elif opcao == 2:
        cursor = conexao.execute("select * from registro_captura where capturado = 'True' and shiny = 'True' "
                                 "group by nome_pokemon order by numero_dex")
        count = conexao.execute("select count(distinct nome_pokemon) from registro_captura where capturado = 'True' "
                                "and shiny = 'True'")
        capturados = count.fetchall()
        qtde_capturados = capturados[0][0]
        print('Pokedéx Shiny'.center(40))
        print('-=' * 20)

    itens_dex = cursor.fetchall()
    for poke in itens_dex:
        dex = poke[3]
        name = poke[4]
        type_1 = poke[5]
        type_2 = poke[6]
        if type_1 == type_2:
            print(f"\033[1;32m# {dex[5:]} {name} - {type_1}\033[m")
        else:
            print(f"\033[1;32m# {dex[5:]} {name} - {type_1}/{type_2}\033[m")

    print('-=' * 20)
    print(f'\033[1;33m{qtde_capturados} / 151 Pokémon Capturados!\033[m'.center(50))


def pokemart():
    print('Bemvindo ao Pokémart')
    while True:
        opcao = leiaInt('O que você deseja? [ 1 ] Comprar [ 2 ] Vender [ 3 ] Sair: ')
        if opcao == 1:
            print(f"PokéCréditos Disponíveis: P$ {inventario['poke_creditos']['qtde']}")
            print('Itens Disponíveis:')
            print(f'1 - {inventario["pokeball"]["nome_item"]}   P$ {int(inventario["pokeball"]["preco_compra"])}\n'
                  f'2 - {inventario["greatball"]["nome_item"]}  P$ {int(inventario["greatball"]["preco_compra"])}\n'
                  f'3 - {inventario["ultraball"]["nome_item"]}  P$ {int(inventario["ultraball"]["preco_compra"])}\n'
                  f'4 - {inventario["masterball"]["nome_item"]} P$ {int(inventario["masterball"]["preco_compra"])}')
            compra = leiaInt("O que deseja comprar? ")
            match compra:
                case 1:
                    item_compra = inventario['pokeball']
                case 2:
                    item_compra = inventario['greatball']
                case 3:
                    item_compra = inventario['ultraball']
                case 4:
                    item_compra = inventario['masterball']

            qtde_compra = leiaInt("Digite a quantidade desejada: ")
            valor_compra = int(qtde_compra * item_compra['preco_compra'])

            if valor_compra > inventario['poke_creditos']['qtde']:
                print('-=' * 20)
                print('\033[1;31mPoké Creditos insuficientes\033[m'.center(40))
                print('-=' * 20)
            else:
                inventario['poke_creditos']['qtde'] -= valor_compra
                item_compra['qtde'] += qtde_compra
                print('-=' * 20)
                print(
                    f'\033[1;32mVocê comprou {qtde_compra} {item_compra["nome_item"]}(s)\nValor Compra: P$ {valor_compra}\n'
                    f'Poké Créditos Restantes: P$ {inventario["poke_creditos"]["qtde"]}\033[m')
                print('-=' * 20)

        elif opcao == 2:
            break

        elif opcao == 3:
            break


def ganhar_xp(xp_recebida, type_pokemon):
    xp = xp_recebida

    xp += xp_recebida

    match type_pokemon:
        case 'normal':
            xp *= 1
        case 'shiny':
            xp *= 2
        case 'lendario':
            xp *= 3

    player['xp_atual']['info'] += xp

    print(f'\033[1;32m>>> + {xp} XP! <<<\033[m'.center(50))

    if player['xp_atual']['info'] >= level_dict[str(player['nivel_atual']['info'])] and player['nivel_atual'][
        'info'] < 50:
        leftover = player['xp_atual']['info'] - level_dict[str(player['nivel_atual']['info'])]
        player['xp_atual']['info'] = leftover
        player['nivel_atual']['info'] += 1
        inventario['poke_creditos']['qtde'] += 300
        inventario['pokeball']['qtde'] += 5

        print('-=' * 20)
        print(f'\033[1;32mSubiu para o nível {player["nivel_atual"]["info"]}!\033[m'.center(50))
        print(f'\033[1;32m Bônus de +P$ 300 Poké Créditos!\033[m'.center(50))
        print(f'\033[1;32m Bônus de +5 Pokeball!\033[m'.center(50))
        print('-=' * 20)

    elif player['xp_atual']['info'] >= level_dict[str(player['nivel_atual']['info'])] and player['nivel_atual'][
        'info'] == 9:
        player['xp_atual']['info'] = level_dict[str(player['nivel_atual']['info'])]

    print(f'\033[1;32mNivel: {player["nivel_atual"]["info"]}\033[m'.center(50))
    print(
        f'\033[1;32mBarra EXP: {player["xp_atual"]["info"]} / {level_dict[str(player["nivel_atual"]["info"])]}\033[m'.center(
            50))
    print('-=' * 20)


# drop de poke creditos
def loot_poke_credito(type_pokemon):
    loot = randint(35, 80)

    match type_pokemon:
        case 'cap_normal':
            loot *= 1
        case 'evo_normal':
            loot *= 2
        case 'cap_shiny':
            loot *= 2
        case 'evo_shiny':
            loot *= 3
        case 'cap-lendario':
            loot *= 4

    inventario['poke_creditos']['qtde'] += loot

    print(f'\033[1;32m>>> + P$ {loot} Poké Créditos <<<\033[m'.center(50))


# Programa Principal
while True:
    print('-=' * 20)
    print('Menu Principal'.center(40))
    print('-=' * 20)
    print('\033[1;31m[ 1 ] - Procurar Pokémon\n[ 2 ] - Pokedéx\n'
          '[ 3 ] - Pokémart\n[ 4 ] - Reiniciar Jogo\n[ 5 ] - Sair do Jogo\033[m')
    print('-=' * 15)
    opcao = leiaInt('Qual sua opção? ')

    match opcao:
        case 1:
            encontrar_pokemon()
        # elif opcao == 2:
        #     evolucao()
        case 2:
            pokedex()
        case 3:
            pokemart()
        # elif opcao == 5:
        #     mudar_rota()
        case 4:
            reiniciar_jogo()
            print('O jogo será fechado...')
            input('Pressione ENTER para fechar...')
            break
        case 5:
            fim_jogo = leiaInt('Confirma? [ 1 ] Sim [ 2 ] Nao: ')
            if fim_jogo == 1:
                salvar_dados()
                conexao.close()
                break

    salvar_dados()
