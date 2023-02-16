import pandas as pd
import sqlite3
from sqlite3 import Error

db = 'items.db'
#conexao geral
def connection():
    try:
        sqlite3.connect(db)
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)
    return conn 

#retorna todos os valores da coluna
def showValues():
    conn = connection()
    cursor = conn.cursor() 
    data = cursor.execute(r'select * from items;')
    raw = data.fetchall()
    for i in raw:
        print(i)
    conn.close()

#insere dados na sequencia = id(int), nome(char), quantidade(int), comprar(char)
def insertAll(a, b, c, d):
    id = ''
    nome = '' 
    valor = ''
    data = ''
    tipo = ''
    table_principal = [id, nome, valor, data, tipo]
    querry = f'''insert into items({table_principal[0]}, {table_principal[0]}, {table_principal[0]}, {table_principal[0],}, ) 
                values(?, ?, ?, ?)''' 
    param = a, b, c, d
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(querry, param)
    conn.commit()
    conn.close()

#atualiza dados sequencia param1 = coluna; param2 = valor; param3 = id
def updateData(param1, param2, param3):
    querry = f'update items set {param1} = "{param2}" where id = {param3};'
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()
    conn.close()

#nao serve pra retornar dados, mas para executar "PERIGOSO"
def execute(querry):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()
    conn.close()

#deleta dados pela id 
def delete(param):
    execute(f"delete from items where id = {param}")
    conn = connection()
    conn.close()

#atualiza o id de certo dado aonde param1 = novo id; param2 = id do dado
def update_id(param1, param2):
    querry = f'update items set id = "{param1}" where id = {param2};'
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()
    conn.close()

#atualiza o nome de certo dado aonde param1 = novo nome; param2 = id do dado
def update_name(param1, param2):
    querry = f'update items set nome = "{param1}" where id = {param2};'
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()
    conn.close()

#atualiza a quantidade de certo dado aonde param1 = nova quantidade; param2 = id do dado
def update_quantd(param1, param2):
    querry = f'update items set quantidade = "{param1}" where id = {param2};'
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()
    conn.close()

#atualiza o parametro comprar de certo dado aonde param1 = nova inf; param2 = id do dado
def update_comprar(param1, param2):
    querry = f'update items set comprar = "{param1}" where id = {param2};'
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()
    conn.close()

def returnPd():
    conn = connection()
    df = pd.read_sql_query('select * from items', conn)
    return df

def return_x(id):
    conn = connection()
    df = pd.read_sql_query(f'select * from items where id = {id}', conn)
    return df