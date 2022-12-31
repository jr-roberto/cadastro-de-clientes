import banco_dados as db
import eel
import os

if 'db' not in os.listdir():
    os.mkdir('db')
    db.nova_tabela()
    print('Nova tbl_usuario iniciada')

eel.init('web')

@eel.expose
def table_user():
    table = db.carregar_tabela()
    return table

@eel.expose
def novo_cadastro(nome_usuario,senha,st='Ativo'):
    
    db.novo_usuario(nome_usuario,senha,st)

    eel.load_table()()
    
    return db.carregar_tabela()

eel.start('index.html')
