import psycopg2 as psy

def conectarBD():
    conexao = psy.connect(
        host="postgres.ata",
        database="pedidos",
        port=5000,
        user="renan",
        password="rev@123"
    )
    return conexao
    
def gera_cursor(banco:psy):
    cursor = banco.cursor()
    return cursor


def retorna_status(item,banco):
    conexao = conectarBD()
    cursor = gera_cursor(conexao)
    if item is int:
        sql = "select status from "+banco+" where seq = "+item+';'
    else:
        sql = "select status from "+banco+" where OP_MAQ = '"+item+"';"
    cursor.execute(sql)
    print(cursor.fetchone()[0])
    status = cursor.fetchone()[0]
    return status


def gerar_update(sql):
    import Mensagens as msg
    conexao = conectarBD()
    cursor = gera_cursor(conexao) 
    cursor.execute(sql)
    conexao.commit()
    print(cursor.rowcount)
    return msg.retorna_status_finalizado(cursor.rowcount)

#retorna_status('1.220.677','Pedidos')
#conectarBD('select * from pedidos where id = 1766;')
#conectarBD("update pedidos set complemento = 'teste' where id = 1766")
#print(cursor.fetchall())
