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


def registrar_captura(pokemon_selvagem, capturado, shiny):
    data_atual = dt.now()
    data = str(data_atual)
    cursor.execute(f"INSERT INTO registro_captura (data, hora, numero_dex, nome_pokemon, tipo_pokemon, capturado, "
                   f"shiny)"
                   f"VALUES ('{data[:10]}', '{data[11:19]}', '{pokemon_selvagem['id']}', '{pokemon_selvagem['nome']}',"
                   f"'{pokemon_selvagem['tipo_pokemon']}', '{capturado}', '{shiny}')")
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
                poke_selvagem["shiny_apareceu"] += 1
            else:
                print(f'\033[1;33mEncontrou um >> {poke_selvagem["nome"]} <<\033[m'.center(50))
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
            if usar_pokebola == 1:
                pokeball = inventario["pokeball"]
            elif usar_pokebola == 2:
                pokeball = inventario["greatball"]
            elif usar_pokebola == 3:
                pokeball = inventario["ultraball"]

            captura(shiny, poke_selvagem, pokeball)

            opcao = leiaInt('Voltar ao Menu Principal? [ 1 ] Sim [ 2 ] Não: ')
            if opcao == 1:
                break
        else:
            break


# função que executa a captura de um pokémon
def captura(is_shiny, poke_selvagem, pokeball):

    random_number = random.random()
    chance_captura = (poke_selvagem['catch_rate'] / 255) * pokeball['rate_captura']
    print(f'Random Number: {random_number:.2f}')
    print(f"Chance Captura: {chance_captura:.2f}")
    if pokeball["qtde"] > 0:
        pokeball['qtde'] -= 1
        print('Pokebola Lançada')

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
                registrar_captura(poke_selvagem, 'True', 'True')

            else:
                print('-=' * 20)
                poke_selvagem['copy'] += 1
                poke_selvagem['total_copy'] += 1
                print(f'\033[1;32m{poke_selvagem["nome"]} Capturado!\033[m'.center(50))
                print(f"\033[1;32mVoce tem {poke_selvagem['copy']} cópia(s) dele!\033[m".center(50))
                loot_poke_credito('cap_normal')
                ganhar_xp(poke_selvagem["exp_base"], 'normal')
                registrar_captura(poke_selvagem, 'True', 'False')

        else:
            if is_shiny != 5:
                registrar_captura(poke_selvagem, 'False', 'False')

            else:
                registrar_captura(poke_selvagem, 'False', 'True')

            for c in range(1, 6):
                print(c, end='-> ', flush=True)
                sleep(0.5)
            print()

            print('-=' * 20)
            print(f'\033[1;31m{poke_selvagem["nome"]} Fugiu!\033[m'.center(50))
            print('-=' * 20)
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
        type = poke[5]
        print(f"\033[1;32m# {dex[5:]} {name} - {type}\033[m")

    print('-=' * 20)
    print(f'\033[1;33m{qtde_capturados} / 151 Pokémon Capturados!\033[m'.center(50))


def ganhar_xp(xp_recebida, type_pokemon):
    xp = xp_recebida

    xp += xp_recebida

    if type_pokemon == 'normal':
        xp *= 1

    elif type_pokemon == 'shiny':
        xp *= 2

    elif type_pokemon == 'lendario':
        xp *= 3

    player['xp_atual']['info'] += xp

    if player['xp_atual']['info'] >= level_dict[str(player['nivel_atual']['info'])] and player['nivel_atual'][
        'info'] < 50:
        leftover = player['xp_atual']['info'] - level_dict[str(player['nivel_atual']['info'])]
        player['xp_atual']['info'] = leftover
        player['nivel_atual']['info'] += 1
        inventario['poke_creditos']['qtde'] += 300
        print(f'\033[1;32mSubiu para o nível {player["nivel_atual"]["info"]}!\033[m'.center(50))

        print(f'\033[1;32mVocê ganhou P$ 300 Poké Créditos!!!\033[m'.center(50))

    elif player['xp_atual']['info'] >= level_dict[str(player['nivel_atual']['info'])] and player['nivel_atual'][
        'info'] == 9:
        player['xp_atual']['info'] = level_dict[str(player['nivel_atual']['info'])]

    print(f'\033[1;32m>>> + {xp} XP! <<<\033[m'.center(50))
    print(f'\033[1;32mNivel: {player["nivel_atual"]["info"]}\033[m'.center(50))
    print(
        f'\033[1;32mBarra EXP: {player["xp_atual"]["info"]} / {level_dict[str(player["nivel_atual"]["info"])]}\033[m'.center(
            50))
    print('-=' * 20)


# drop de poke creditos
def loot_poke_credito(type_pokemon):
    loot = randint(35, 80)

    if type_pokemon == 'cap_normal':
        loot *= 1
    elif type_pokemon == 'evo_normal':
        loot *= 2
    elif type_pokemon == 'cap_shiny':
        loot *= 2
    elif type_pokemon == 'evo_shiny':
        loot *= 3
    elif type_pokemon == 'cap_lendario':
        loot *= 4

    inventario['poke_creditos']['qtde'] += loot

    print(f'\033[1;32m>>> + P$ {loot} Poké Créditos <<<\033[m'.center(50))


# Programa Principal
print('-=' * 20)
print('Captura Pokémon'.center(40))
print('-=' * 20)

while True:
    print('-=' * 20)
    print('Menu Principal'.center(40))
    print('-=' * 20)
    print('\033[1;31m[ 1 ] - Procurar Pokémon\n[ 2 ] - Evoluir Pokémon\n'
          '[ 3 ] - Mostrar Pokédex\n[ 4 ] - Pokémart\n'
          '[ 5 ] - Mudar Rota\n[ 6 ] - Reiniciar Jogo\n[ 7 ] - Sair do Jogo\033[m')
    print('-=' * 15)
    opcao = leiaInt('Qual sua opção? ')

    if opcao == 1:
        encontrar_pokemon()
    # elif opcao == 2:
    #     evolucao()
    elif opcao == 3:
        pokedex()
    # elif opcao == 4:
    #     pokemart()
    # elif opcao == 5:
    #     mudar_rota()
    elif opcao == 6:
        reiniciar_jogo()
        print('O jogo será fechado...')
        input('Pressione ENTER para fechar...')
        break
    elif opcao == 7:
        fim_jogo = leiaInt('Confirma? [ 1 ] Sim [ 2 ] Nao: ')
        if fim_jogo == 1:
            salvar_dados()
            conexao.close()
            break

    salvar_dados()