import banco_dados as db
import eel
import os

if 'db' not in os.listdir():
    os.mkdir('db')
    db.nova_tabela()
    print('Nova tbl_usuario iniciada')

eel.init('web')

eel.start('index.hrml')
