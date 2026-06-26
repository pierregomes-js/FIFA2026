import os

def obter_inteiro_or_none(texto):
    valor = input(texto)

    try:
        valor_valido = int(valor)
        return valor_valido
    except:
        return None


def obter_inteiro(texto):
    valor = obter_inteiro_or_none(texto)

    while valor == None:
        print('Valor inválido. Digite novamente')
        valor = obter_inteiro_or_none(texto)

    return valor


def obter_bool(texto):
    valor = input(texto)
    valor = valor.upper()

    if valor == 'SIM':
        return True
    else:
        return False
    

def filtrar(lista, condicao):
    nova_lista = []
    for dict in lista:
        if condicao(dict):
            nova_lista.append(dict)

    return nova_lista


def reduce(lista, inicio, op, atributo):
    valor_inicial = inicio
    for dict in lista:
        valor_inicial = op(valor_inicial, dict, atributo)

    return valor_inicial


def limpar_tela():
    os.system('cls')


def ordenar(lista, mensagem):
    
    atributo = input(mensagem)
    asc_desc = obter_bool('Decrescente? (sim/não): ')

    return sorted(lista, key=lambda x:x[atributo] , reverse=asc_desc)


def lower(texto):
    mensagem = input(texto)

    return mensagem.lower()