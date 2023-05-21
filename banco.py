########## Importando SQLite ##########
import sqlite3 as lite

########## Criando Conexão ##########

con = lite.connect('dados.db')

########## Criando Tabela ##########
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(cpf INTEGER PRIMARY KEY NOT NULL, nome TEXT, sexo TEXT, idade TEXT, nasc DATE, av1 FLOAT, av2 FLOAT, media FLOAT)")