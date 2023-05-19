########## Importando SQLite ##########
import sqlite3 as lite

# CRUD

# Creat = Inserir / criar
# Ready = Acessar / mostrar
# Update = Atualizar
# Delete = Deletar / apagar

########## Criando conexão ##########
con = lite.connect('dados.db')

lista = ['Joao Futi Muanda', 'joao@mail.com', 123456789, "18/19/2010", "Normal", 'gostaria de o consultar pessoalmente']

########## Inserir informações ##########
def inserir_info(i):
    with con:
          cur = con.cursor()
          query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
          cur.execute(query,i)

inserir_info(lista)

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
        query = "UPDATE formulario SET nome =?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query,i)


########## Deletar informações ##########
def deletar_info(i):
    with con:
          cur = con.cursor()
          query = "DELETE From formulario WHERE id=?"
          cur.execute(query,i)