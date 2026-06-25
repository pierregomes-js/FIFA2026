from utils import *


def obter_selecao(lista):

    if len(lista) == 0:
        id_atual = 1
    else:
        id_atual = lista[-1]['id'] + 1

    nome = input('Nome: ')
    confederacao = input('Confederação: ')
    grupo = input('Grupo: ')
    ranking_fifa = obter_inteiro('Ranking FIFA: ')
    titulos = obter_inteiro('Títulos: ')


    selecao = {
    'id': id_atual ,
    'nome': nome ,
    'confederacao': confederacao,
    'grupo': grupo,
    'ranking_fifa': ranking_fifa,
    'titulos': titulos,
    }

    lista.append(selecao)

    print(f'Seleção {nome} adicionada com sucesso !')
    

def listar_selecoes(lista):
    print(f'Há {len(lista)} seleções: ')

    for dado in lista:
        print(f'Id: {dado['id']} - Nome: {dado['nome']} - Confederação: {dado['id']} - Grupo: {dado['grupo']} - Ranking FIFA: {dado['ranking_fifa']} - Títulos: {dado['titulos']}')


def buscar_selecoes(lista):
    parte_nome = input('Parte do Nome ou o nome:')
    selecao = filtrar(lista, lambda x:x if parte_nome in x['nome'] else None)

    if len(selecao) == 0:
        print('Não foi encontrado a seleção.')
    else:
        print(f'Seleção: \n{selecao[0]}')
    

def filtrar_selecoes(lista):
    atributo = lower('Grupo ou confederacao?: ')
    texto = input('Insira o texto do grupo/confederacao desejado: ')

    listar_selecoes(filtrar(lista, lambda x:x if x[atributo] == texto else None))


def mensagem_selecoes():
    return 'Ordenação: \n- ranking_fifa\n- nome\n- titulos\n: '