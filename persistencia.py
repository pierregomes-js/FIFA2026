
def carregar_selecoes(caminho):
    selecoes = []
    arquivo = open(caminho)
    linhas = arquivo.readlines()


    for linha in linhas:
        dado = linha.strip().split(';')
        selecao = {
    "id": int(dado[0]),
    "nome": dado[1],
    "confederacao": dado[2],
    "grupo": dado[3],
    "ranking_fifa": int(dado[4]),
    "titulos": int(dado[5]),
    }
        selecoes.append(selecao)

    arquivo.close()

    return selecoes

    
def salvar_selecoes(lista, caminho):
    linhas = []

    for dado in lista:
        linhas.append(str(dado['id'])  + ';' + dado['nome'] + ';' + dado['confederacao']+ ';' + str(dado['grupo']) + ';' + str(dado['ranking_fifa']) + ';' +  str(dado['titulos']) + '\n' )

    arquivo = open(caminho, 'w')
    arquivo.writelines(linhas)
    arquivo.close()


def carregar_jogadores(caminho):
    jogadores = []
    arquivo = open(caminho)
    linhas = arquivo.readlines()

    for linha in linhas:

        dado = linha.strip().split(';')

        jogador = {
    "id": int(dado[0]),
    "nome": dado[1],
    "selecao_id": int(dado[2]),
    "posicao": dado[3],
    "idade": int(dado[4]),
    "gols": int(dado[5]),
    }
        
        jogadores.append(jogador)

    arquivo.close()
    return jogadores

    
def salvar_jogadores(lista, caminho):
    linhas = []

    for dado in lista:
        linhas.append(str(dado['id'])  + ';' + dado['nome'] + ';' + str(dado['selecao_id'])+ ';' + dado['posicao'] + ';' + str(dado['idade']) + ';' +  str(dado['gols']) + '\n' )

    arquivo = open(caminho, 'w')
    arquivo.writelines(linhas)
    arquivo.close()



def carregar_partidas(caminho):
    partidas = []
    arquivo = open(caminho)
    linhas = arquivo.readlines()

    for linha in linhas:

        dado = linha.strip().split(';')

        partida = {
    "id": int(dado[0]),
    "selecao_casa_id": int(dado[1]),
    "selecao_fora_id": int(dado[2]),
    "gols_casa": int(dado[3]),
    "gols_fora": int(dado[4]),
    "fase": dado[5],
    }
        
        partidas.append(partida)


    arquivo.close()

    return partidas

    
def salvar_partidas(lista, caminho):
    linhas = []

    for dado in lista:
        linhas.append(str(dado['id'])  + ';' + str(dado['selecao_casa_id']) + ';' + str(dado['selecao_fora_id'])+ ';' + str(dado['gols_casa']) + ';' + str(dado['gols_fora']) + ';' +  dado['fase'] + '\n' )

    arquivo = open(caminho, 'w')
    arquivo.writelines(linhas)
    arquivo.close()