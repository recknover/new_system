import main as sql

def return_table_all():
    raw = sql.returnPd()
    table = raw.to_html(index=0, border=0)
    div = Element("tabela")
    div.element.innerHTML = f"<br> {table} <br>"

def reset():
    div = Element("tabela")
    div.element.innerHTML = "<div></div>"

def return_especifc():
    id = Element("id").element.valueAsNumber
    raw = sql.return_x(id)
    data = raw.to_html(index=0, border=0)
    div = Element("tabela")
    div.element.innerHTML = f"<br> {data} <br>"
    
def getValues():
    id = Element("id").element.valueAsNumber
    nome = Element("nome").element.value
    valor = Element("valor").element.valueAsNumber
    data_ins = Element("data_insert").element.valueAsNumber
    tipo = Element("tipo").element.value
    raw = [id, nome, valor, data_ins, tipo]
    print(raw)
    return raw

def execute():
    querry = Element("executar").value
    sql.execute(querry)
    
def insertData():
    raw = getValues()
    sql.insertAll(raw[0], raw[1], raw[2], raw[3], raw[4])
    
