import pandas as pd
import numpy as np

# NOVA TABELA NO SISTEMA
def nova_tabela():
    nome_campo = ['nome_usuario','senha','situacao']
    
    tabela = {}
    for campo in nome_campo:
        tabela.update({campo:[]})
    
    to_csv = pd.DataFrame(data=tabela)
    to_csv.to_csv('db/tbl_usuario.csv',sep=';',encoding='ISO-8859-1',index_label='id')

# CARREGA UMA TABELA EXISTENTE
def carregar_tabela():
    'return = { "thead" : columns , "tbody" : data }'
    df = pd.read_csv('db/tbl_usuario.csv',sep=';',encoding='ISO-8859-1').to_dict('split')

    columns = df['columns']
    data = df['data']

    return {"thead":columns,"tbody":data}

# ATUALIZAR TABELA
def atualiza_tabela(my_table):
    #df = pd.DataFrame(data=my_table)
    my_table.to_csv('db/tbl_usuario.csv',sep=';',index=False,encoding='ISO-8859-1')

# MY_TABLE - INSTANCIA
def my_table(thead,tbody):
    table = pd.DataFrame(np.array(tbody),columns=thead)
    return table

# CADASTRA UM NOVO USUARIO NA TABELA - [tbl_usuario.csv]
def novo_usuario(nome_usuario,senha,st):
    table = carregar_tabela()

    thead = table['thead']
    tbody = table['tbody']

    id = len(tbody) + 1

    new_row = [id,nome_usuario,senha,st]
 
    tbody.append(new_row)

    table = my_table(thead=thead,tbody=tbody)

    atualiza_tabela(my_table=table)

    return my_table

# CONSULTAR USUARIO
def consulta(id):
    table = carregar_tabela()

    tbody = table['tbody']

    result = 'Id nao encontrado!'
    index_row_table = 0
    for row in tbody:
        if row[0] == id:
            result = [index_row_table,row]
            break

        index_row_table += 1
        
    return result

# ATIVAR/DESATIVAR - USUARIO
def alterar_situacao(id):
    registro = consulta(id)

    if registro != 'Id nao encontrado!':
        table = carregar_tabela()
        thead = table['thead']
        tbody = table['tbody']

        tbody_row = tbody[registro[0]]
        
        print(tbody_row)

        if tbody_row[3] == 'Ativo':
            tbody_row[3] = 'Inativo'
        else:
            tbody_row[3] = 'Ativo'
        
        print(tbody_row)

        tbody.pop(registro[0])
        tbody.append(tbody_row)

        table = my_table(thead=thead,tbody=tbody)
        atualiza_tabela(table)


# DEV
if __name__ == '__main__':
    alterar_situacao(3)
