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
    if banco == 'Laser':
        sql = "select status from plan_laser where seq = "+item+';'
    else:
        sql = "select status from "+banco+" where OP_MAQ = '"+item+"';"
    cursor.execute(sql)
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
    import Mensagens as msg
    conexao = conectarBD()
    cursor = gera_cursor(conexao) 
    cursor.execute(sql)
    conexao.commit()
    print(cursor.rowcount)
    return msg.retorna_status_finalizado(cursor.rowcount)

def status_montagem(status,sql):
    import Mensagens as msg
    if status == 'Montagem':
        return gerar_update(sql)
    else:
        return msg.nao_montagem()

def status_programado(status,sql):
    import Mensagens as msg
    if status == 'Programado':
        return gerar_update(sql)
    else:
        return msg.nao_montagem()

def terminado(termino,sql):
    import Mensagens as msg
    if termino != None:
        return gerar_update(sql)
    else:
        return msg.nao_terminado()

def status_finalizado(status,sql):
    import Mensagens as msg
    if status == "Finalizado":
        return gerar_update(sql)
    else:
        return msg.nao_terminado()


#print (retorna_termino('1.270.047'))

#conectarBD('select * from pedidos where id = 1766;')
#conectarBD("update pedidos set complemento = 'teste' where id = 1766")
#print(cursor.fetchall())
