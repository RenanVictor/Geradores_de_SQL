import psycopg2 as psy
import Mensagens as msg
import gerenciamento_sql as gtsql

def conectarBD():  # Se conecta no servidor
    conexao = psy.connect(
        host="postgres.ata",
        database="pedidos",
        port=5000,
        user="renan",
        password="rev@123"
    )
    return conexao
    
def gera_cursor(conexao: psy):  # retorna o cursor
    cursor = conexao.cursor()
    return cursor

def validacao_update(registro,dic_valores:dict):
    if 'item' in dic_valores:
        resultado = atualiza_banco('select',registro, dic_valores['item'])
    else:
        return msg.item_invalido()
    print(resultado)
    if resultado['count_row']>1:
        return msg.registros_multiplos()
    if registro['col_validacao'] in resultado['retorno']:
        if len(list(dic_valores.values())) >= len(registro['col_change']):
            valores = []
            for i in range(len(registro['col_change'])+1):
                if i ==len(registro['col_change']):
                    valores.append(list(dic_valores.values())[len(list(dic_valores.values()))-1])    
                else:
                    valores.append(list(dic_valores.values())[i])
            atualiza_banco('update',registro,valores)    
        else:
            return msg.item_invalido()
        return msg.retorna_status_finalizado(resultado['count_row'])
    else:
        return msg.nao_validado(registro['col_validacao'])


#Usado pelo log_usuario
def atualiza_banco(tipo,registro, list_valores):
    sql = gtsql.gerador_sql(registro)
    if tipo == 'update':
       sql_gerado = sql.retorna_sql_update()
    if tipo == 'select':
        sql_gerado = sql.retorna_sql_select()
    if tipo == 'insert':
        sql_gerado = sql.retorna_sql_insert()
    conexao = conectarBD()
    cursor = gera_cursor(conexao)
    resultado = {}
    if tipo == 'select':
        cursor.execute(sql_gerado,[list_valores])
        resultado['retorno'] = cursor.fetchone()
    else:
        cursor.execute(sql_gerado,(list_valores))
    resultado['count_row'] = cursor.rowcount
    resultado['sql_gerado'] = sql_gerado
    conexao.commit()
    return(resultado)

def select_log(sql):
    conexao = conectarBD()
    cursor = gera_cursor(conexao)
    cursor.execute(sql)
    return cursor.fetchall()

