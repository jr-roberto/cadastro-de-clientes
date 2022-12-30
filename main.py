import pandas as pd

def nova_tabela():
    nome_campo = ['nome_usuario','tipo_usuario','login','password']

    tbl_usuario = {}
    for campo in nome_campo:
        tbl_usuario.update({campo:[]})
    
    atualiza_tabela(my_table=tbl_usuario)

def atualiza_tabela(my_table):
    to_csv = pd.DataFrame(data=my_table)
    to_csv.to_csv('db/tbl_usuario.csv',sep=';',encoding='ISO-8859-1',index=False)

def carregar_tabela():
    nome_tabela='db/tbl_usuario.csv'

    tabela = pd.read_csv(nome_tabela,sep=';',encoding='ISO-8859-1')
    

    return tabela.to_dict('split')

def novo_usuario(nome_usuario,tipo_usuario,usuario,password):

    df = carregar_tabela()
    
    tabela = {}
    for col in df.columns:
        tabela.update({col:list(df[col])})
    
    tabela['nome_usuario'].append(nome_usuario)
    tabela['tipo_usuario'].append(tipo_usuario)
    tabela['login'].append(usuario)
    tabela['password'].append(password)

    atualiza_tabela(my_table=tabela)

if __name__ == '__main__':
    print(carregar_tabela())
