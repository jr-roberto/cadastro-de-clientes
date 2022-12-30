import pandas as pd
import numpy as np

# NOVA TABELA NO SISTEMA
def nova_tabela():
    nome_campo = ['id','nome_usuario','senha','permissao']
    
    tabela = {}
    for campo in nome_campo:
        tabela.update({campo:[]})
    
    atualiza_tabela(my_table=tabela)

# CARREGA UMA TABELA EXISTENTE
def carregar_tabela():
    df = pd.read_csv('db/tbl_usuario.csv',sep=';',encoding='ISO-8859-1').to_dict('split')

    columns = df['columns']
    data = df['data']

    return {"thead":columns,"tbody":data}

# ATUALIZAR TABELA
def atualiza_tabela(my_table):
    df = pd.DataFrame(data=my_table)
    df.to_csv('db/tbl_usuario.csv',sep=';',index=False,encoding='ISO-8859-1')

# CADASTRA UM NOVO USUARIO NA TABELA - [tbl_usuario.csv]
def novo_usuario(nome_usuario,senha,per):
    table = carregar_tabela()

    thead = table['thead']
    tbody = table['tbody']

    id = len(tbody) + 1

    new_row = [id,nome_usuario,senha,per]

    tbody.append(new_row)

    my_table = pd.DataFrame(np.array(tbody),columns=thead)

    atualiza_tabela(my_table=my_table)

    return my_table

# CONSULTAR USUARIO
def consulta(id):
    table = carregar_tabela()

    tbody = table['tbody']

    result = 'Id nao encontrado!'
    for row in tbody:
        if row[0] == id:
            result = row
            break
        
    return result

# EXCLUIR USUARIO


# DEV
if __name__ == '__main__':
    print(consulta(0))
