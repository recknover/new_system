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
    id = Element("numero").element.valueAsNumber
    raw = sql.return_x(id)
    data = raw.to_html(index=0, border=0)
    div = Element("tabela")
    div.element.innerHTML = f"<br> {data} <br>"
    
