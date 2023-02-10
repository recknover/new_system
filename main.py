import sqlite3
from sqlite3 import Error

db = 'items.db'
def connection():
    try:
        sqlite3.connect(db)
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)
    return conn 

def showValues():
    conn = connection()
    cursor = conn.cursor() 
    data = cursor.execute(r'select * from items;')
    raw = data.fetchall()
    for i in raw:
        print(i)

def insertAll(a, b, c, d):
    querry = '''insert into items(id, nome, quantidade, comprar) 
                values(?, ?, ?, ?)''' 
    param = a, b, c, d
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(querry, param)
    conn.commit()

def updateData(param1, param2, param3):
    querry = f'update items set {param1} = "{param2}" where id = {param3};'
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()
    print(querry)

#nao serve pra retornar dados, mas para executar
def execute(querry):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()


updateData(r'nome', "teste3", 3)
execute('update items set nome = "teste" where id = 1;') 


