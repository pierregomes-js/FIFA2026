from selecoes import *
from jogadores import *
from utils import *


def obter_partida(selecoes, partidas):
    listar_selecoes(selecoes)

    selecao_casa_id = obter_inteiro('Id da seleção de casa: ')
    selecao_fora_id = obter_inteiro('Id da seleção de fora: ')

    if len(partidas) == 0:
        id_atual = 5000
    else:
        id_atual = partidas[-1]['id'] + 1

    gols_casa = obter_inteiro('Gols de casa: ')
    gols_fora = obter_inteiro('Gols de fora: ')
    fase = lower('Fase(grupos, segunda rodada, oitavas, quartas, semi, final): ')

    partida = {
    "id": id_atual,
    "selecao_casa_id": selecao_casa_id,
    "selecao_fora_id": selecao_fora_id,
    "gols_casa": gols_casa,
    "gols_fora": gols_fora,
    "fase": fase,
    }

    partidas.append(partida)
    print('Partida adicionada com sucesso !')


def listar_partidas(lista, selecoes):
    print(f'Há {len(lista)} Partidas:')

    for dado in lista:
        selecao_casa = filtrar(selecoes, lambda x:dado['selecao_casa_id'] == x['id'])[0]
        selecao_fora = filtrar(selecoes, lambda x:dado['selecao_fora_id'] == x['id'])[0]


        print(f'{selecao_casa['nome']}  {dado['gols_casa']} x {dado['gols_fora']} {selecao_fora['nome']}  ({dado['fase']})')


def filtrar_partidas(lista, selecoes):
    fase = input(f'Fase (grupos, oitavas, segunda rodada, oitavas, quartas, semi, final): ')
    listar_partidas(filtrar(lista, lambda x:x['fase'] == fase), selecoes)

#relacionamento
def partidas_selecoes(selecoes):
    lista = []

    for selecao in selecoes:

        nome = selecao['nome']
        id = selecao['id']
        grupo = selecao['grupo']

        item = {
        'pontos' : 0,
        'nome' : nome,
        'id' : id,
        'grupo' : grupo,
        'vitoria' : 0,
        'empate' : 0,
        'derrota' : 0,
        'gols_partida' : 0,
        'gols_contra' : 0,
        'gols_pro' : 0,
        'saldo' : 0
        }

        lista.append(item)

    return lista


def distribuicao_gols(partida, item, s1, s2):
    
    if partida[s1] == partida[s2]:

        item['gols_pro'] += partida[s1]
        item['gols_contra'] += partida[s2]
        item['empate'] += 1

    elif partida[s1] > partida[s2]:
                
        item['gols_pro'] += partida[s1]
        item['gols_contra'] += partida[s2]
        item['vitoria'] += 1

    else:
        item['gols_pro'] += partida[s1]
        item['gols_contra'] += partida[s2]
        item['derrota'] += 1


#relacionamento + distribucao + lista de grupos + classificacao
def calcular_estatisticas(partidas, selecoes):

    lista = partidas_selecoes(selecoes)

    for partida in partidas:

        selecao_casa = filtrar(lista, lambda x:x if x['id'] == partida['selecao_casa_id'] else None)[0]
        selecao_fora = filtrar(lista, lambda x:x if x['id'] == partida['selecao_fora_id'] else None)[0]


        distribuicao_gols(partida, selecao_casa, 'gols_casa', 'gols_fora')
        distribuicao_gols(partida, selecao_fora, 'gols_fora', 'gols_casa')


    for item in lista:
        item['saldo'] = item['gols_pro'] - item['gols_contra']
        item['pontos'] = item['gols_pro'] + item['saldo']

    classificacao(lista)


#lista generada de letras até M
def lista_grupos():

    lista = []

    for i in range(65, 77):
        lista.append(chr(i))

    return lista


def classificacao(lista):

    grupos = lista_grupos()
    
    lista_ordenada = sorted(lista, key=lambda x:x['pontos'], reverse=True)
    posicao = 1
    
    for grupo in grupos:

        selecoes_grupo = filtrar(lista_ordenada, lambda x:x if x['grupo'] == grupo else None)
        if len(selecoes_grupo) == 0:
            continue
            
        print(f'--- CLASSIFICACAO - GRUPO {grupo} ---')
        print('Pos - Selecao   -    P    V    E    D    GP    GC    SG')

        for selecao in selecoes_grupo:
            print(f'{posicao} | {selecao['nome']}  |   ({selecao['pontos']})  |   {selecao['vitoria']}  |   {selecao['empate']}  |   {selecao['derrota']}  |   {selecao['gols_pro']}  |   {selecao['gols_contra']}  |   {selecao['saldo']}')
    
            posicao += 1
        
        posicao = 1

        print('(P=Pontos, V/E/D=Vitorias/Empates/Derrotas, GP/GC=Gols Pro/Contra, SG=Saldo)')

        