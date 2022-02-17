from sqlite3 import Cursor
import psycopg2 as psy
import Mensagens as msg

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

def row_counts(sql):
    conexao = conectarBD()
    cursor = gera_cursor(conexao)
    cursor.execute(sql)
    num_registros = cursor.rowcount
    return num_registros

def retorna_sql(banco,item):
    if banco == 'Laser':
        sql = "select status from plan_laser where seq = "+item+';'
    else:
        sql = "select status from "+banco+" where OP_MAQ = '"+item+"';"
    return sql
    
def retorna_status(item,banco):
    conexao = conectarBD()
    cursor = gera_cursor(conexao)
    cursor.execute(retorna_sql(banco,item))
    if cursor.rowcount >1:
        return msg.registros_multiplos()
    status = cursor.fetchone()[0]
    print(status)
    cursor.close()
    return status

def retorna_termino(item):
    conexao = conectarBD()
    cursor = gera_cursor(conexao)
    sql = "select termino from pedidos where OP_MAQ = '"+item+"';"
    cursor.execute(sql)
    termino = cursor.fetchone()[0]
    print(termino)
    cursor.close()
    return termino


def gerar_update(sql):
    conexao = conectarBD()
    cursor = gera_cursor(conexao) 
    cursor.execute(sql)
    conexao.commit()
    print(cursor.rowcount)
    return msg.retorna_status_finalizado(cursor.rowcount)

def gerar_insert(insert,list_valores):
    conexao = conectarBD()
    cursor = gera_cursor(conexao) 
    cursor.execute(insert,list_valores)
    conexao.commit()
    print("log atualizado")
    

def status_montagem(status,sql):
    if status == 'Montagem':
        return gerar_update(sql)
    else:
        return msg.nao_montagem()

def status_programado(status,sql):
    if status == 'Programado':
        return gerar_update(sql)
    else:
        return msg.nao_montagem()

def terminado(termino,sql):
    if termino != None:
        return gerar_update(sql)
    else:
        return msg.nao_terminado()

def status_finalizado(status,sql):
    if status == "Finalizado":
        return gerar_update(sql)
    else:
        return msg.nao_terminado()


#print (retorna_termino('1.270.047'))

#conectarBD('select * from pedidos where id = 1766;')
#conectarBD("update pedidos set complemento = 'teste' where id = 1766")
#print(cursor.fetchall())

