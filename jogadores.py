from selecoes import *
from utils import *


def obter_jogador(selecoes, jogadores):
    listar_selecoes(selecoes)

    selecao_id = obter_inteiro('Id da seleção desejada: ')

    if len(jogadores) == 0:
        id_atual = 100
    else:
        id_atual = jogadores[-1]['id'] + 1

    nome = input('Nome: ')
    posicao = input('Posicão (Goleiro/Zagueiro/Meio/Atacante): ')
    idade = obter_inteiro('Idade: ')
    gols = obter_inteiro('Gols no momento: ')

    jogador = {
    "id": id_atual,
    "nome": nome,
    "selecao_id": selecao_id,
    "posicao": posicao,
    "idade": idade,
    "gols": gols,
    }

    nome_selecao = filtrar(selecoes, lambda x:x['nome'] if x['id'] == selecao_id else None)[0]['nome']
    jogadores.append(jogador)
    print(f'[OK] Jogador {nome} cadastrado e vinculado a selecao {nome_selecao}!')


def listar_jogadores(jogadores, selecoes):
    
    print(f'Há {len(jogadores)} jogadores:')

    for dado in jogadores:
        selecao_id = dado['selecao_id']
        nome_selecao = filtrar(selecoes, lambda x:x if x['id'] == selecao_id else None)[0]['nome']
        print(f'{dado['id']} - {dado['nome']} - {nome_selecao} - {dado['posicao']} - {dado['idade']} - {dado['gols']}')


def filtrar_jogadores(lista, selecoes):
    atributo = obter_inteiro('1- Posição \n2- Faixa de idade \n3-Parte do nome da seleção\n: ')

    if atributo == 1:
        posicao = input('Posição: ')
        listar_jogadores(filtrar(lista, lambda x:x if x['posicao'] == posicao else None), selecoes)

    elif atributo == 2:
        min = obter_inteiro('Idade mínima: ')
        max = obter_inteiro('Idade Máxima: ')
        listar_jogadores(filtrar(lista, lambda x:x if min <=  x['idade'] <= max else None), selecoes)

    else:
        parte_nome = input('Parte do Nome ou o nome:')
        selecao = filtrar(selecoes, lambda x:x if parte_nome in  x['nome'] else None)

        if len(selecao) == 0:
            print('Não foi encontrado a seleção.')
        else:
            selecao_id = selecao[0]['id']
            listar_jogadores(filtrar(lista, lambda x:x if x['selecao_id'] == selecao_id else None), selecoes)


#estatistica recursos
def total_gols(lista):
    return reduce(lista, 0, lambda inicio, dado, atributo:dado[atributo] + inicio, 'gols')


def media_idade(lista):
    somatorio = reduce(lista, 0, lambda inicio, dado, atributo:dado[atributo] + inicio, 'idade')

    if len(lista) != 0:
        return somatorio / len(lista)
    else:
        return 0


def mais_2_gols(lista):
    return filtrar(lista, lambda x:x['nome'] if x['gols'] > 2 else None)
    

def obter_artilheiro(lista):
    return reduce(lista, lista[0], lambda inicio, dado, gols: dado if dado[gols] > inicio[gols] else inicio, 'gols')


def artilheiros_estatisticas(lista, selecoes):

    for selecao in selecoes:
        print(f'\n ===  Seleção {selecao['nome']} === \n')
        jogadores_selecao = filtrar(lista, lambda x:x if x['selecao_id'] == selecao['id'] else None)

        # print(f'Nome da seleção: {selecao['nome']}')
        print(f'Total de jogadores: {len(jogadores_selecao)}')
        print(f'Total de gols do elenco: {total_gols(jogadores_selecao)}')
        print(f'Média de idade: {media_idade(jogadores_selecao)}')
        print(f'Atacantes com mais de 2 gols: ')

        for dado in mais_2_gols(jogadores_selecao):
            print(f' {dado['nome']}', end=' | ')
    
    artilheiro = obter_artilheiro(lista)
    selecao_artilheiro = filtrar(selecoes, lambda x:x if x['id'] == artilheiro['selecao_id'] else None)[0]['nome']

    print(f'\n === Artilheiro da Copa: {artilheiro['nome']} ({selecao_artilheiro}) - {artilheiro['gols']} gols. === ')


#mensagem de ordenação
def mensagem_jogadores():
    return 'Ordenação: \n- gols\n- nome\n -idade\n: '