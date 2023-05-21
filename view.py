########## Importando SQLite ##########
import sqlite3 as lite

# CRUD

# Creat = Inserir / criar
# Ready = Acessar / mostrar
# Update = Atualizar
# Delete = Deletar / apagar

########## Criando conexão ##########
con = lite.connect('dados.db')

lista = ['05283839333', 'Joao Futi Muanda', 'masc', 123456789, "18", "19/02/1994", '10', '8', '9']

########## Inserir informações ##########
def inserir_info(i):
    with con:
          cur = con.cursor()
          query = "INSERT INTO formulario (cpf, nome, sexo, idade, nasc, av1, av2, media) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
          cur.execute(query,i)

# inserir_info(lista)

######### Acessar informações ##########
def mostrar_info():
    lista = []
    with con:
      cur = con.cursor()
      query = 'SELECT * FROM formulario'
      cur.execute(query)
      informacao = cur.fetchall()
      
      for i in informacao:
          lista.append(i)
    return lista

########## Atualizar informações ##########
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET cpf =?, nome =?, sexo=?, idade=?, nasc=?, av1=?, av2=?, media=? WHERE cpf=?"
        cur.execute(query,i)


########## Deletar informações ##########
def deletar_info(i):
    with con:
          cur = con.cursor()
          query = "DELETE From formulario WHERE cpf=?"
          cur.execute(query,i)