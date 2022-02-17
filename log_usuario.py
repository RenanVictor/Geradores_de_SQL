import os
import Conexao

def retorna_usuario():
    return os.getlogin()

def list_valores(banco,item,sql):
    from datetime import date
    data_log = date.today()
    usuario = retorna_usuario()
    registros = retorna_registros(banco,item)
    list_valores = [banco,item,data_log,usuario,registros,sql]
    return list_valores

def retorna_registros(banco,item):
    select = Conexao.retorna_sql(banco,item)
    num_registros = Conexao.row_counts(select)
    return num_registros

def retorna_insert():
    insert = "insert into log_usuario (banco, item, data_log, usuario, num_registro, log_sql) values(%s, %s, %s, %s, %s, %s)"
    return insert

def atualiza_usuario(banco,item,sql):
    Conexao.gerar_insert(retorna_insert(),list_valores(banco,item,sql))
    



