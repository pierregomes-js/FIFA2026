from selecoes import *
from utils import *
from jogadores import *
from partidas import *
from persistencia import *


def main():

    selecoes = carregar_selecoes('selecoes.txt')
    jogadores = carregar_jogadores('jogadores.txt')
    partidas = carregar_partidas('partidas.txt')


    menu = f'''
=== ⚽ COPA MANAGER 2026 — FIFA ⚽ ===

============================================================
Status: {len(selecoes)} selecoes | {len(jogadores)} jogadores | {len(partidas)} partidas cadastradas

--- SELECOES ---
1 - Cadastrar Seleção
2 - Listar Seleções
3 - Buscar por parte do Nome ou Nome
4 - Filtrar por Grupo ou confederação

--- JOGADORES ---
5 - Cadastrar Jogador
6 - Listar e Ordenar Jogadores
7 - Filtrar Jogadores
8 - Artilheiros e Estatística

--- PARTIDAS ---
9- Cadastrar Partida
10 - Listar Partidas
11 - Filtrar partidas por fase
12 - Classificação dos grupos

--- SISTEMA ---
0 - Salvar 

============================================================
Escolha uma opcao:
    '''

    opcao = obter_inteiro(menu)
    limpar_tela()

    while opcao != 0:
        if opcao == 1:
            obter_selecao(selecoes)
        elif opcao == 2:
            listar_selecoes(ordenar(selecoes, mensagem_selecoes()))
        elif opcao == 3:
            buscar_selecoes(selecoes)
        elif opcao == 4:
            filtrar_selecoes(selecoes)


        elif opcao == 5:
            obter_jogador(selecoes, jogadores)
        elif opcao == 6:
            listar_jogadores(ordenar(jogadores, mensagem_jogadores()), selecoes)
        elif opcao == 7:
            filtrar_jogadores(jogadores, selecoes)
        elif opcao == 8:
            artilheiros_estatisticas(jogadores, selecoes)


        elif opcao == 9:
            obter_partida(selecoes, partidas)
        elif opcao == 10:
            listar_partidas(partidas, selecoes)
        elif opcao == 11:
            filtrar_partidas(partidas, selecoes)
        elif opcao == 12:
            calcular_estatisticas(partidas, selecoes)


        input('> ')

        opcao = obter_inteiro(menu)
        limpar_tela()
        



    salvar_selecoes(selecoes, 'selecoes.txt')
    salvar_jogadores(jogadores, 'jogadores.txt')
    salvar_partidas(partidas, 'partidas.txt')

main()