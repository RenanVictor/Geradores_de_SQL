def dict_tabelas():
    pedidos = { 'banco': 'pedidos',
        'col_primaria': 'OP_MAQ',
        'nome':'Pedidos',
        'col_change':['status','termino'],
        'col_validacao': 'Montagem'
    }
    laser = { 'banco': 'plan_laser',
        'col_primaria': 'SEQ',
        'nome':'Laser',
        'col_change':['status','termino','maquina'],
        'col_validacao': 'Programado'
    }
    log = { 'banco': 'log_usuario',
        'col_primaria': 'ID',
        'nome':'log',
        'col_change':['banco','item','data_log','usuario','num_registro','log_sql'],
        'col_validacao': ''
    }
    componentes = { 'banco': 'pedidos',
        'col_primaria': 'ID',
        'nome':'Comp.',
        'col_change':['status','termino'],
        'col_validacao': 'Primários'
    
    }

    bancos = [pedidos,laser,log,componentes]
    return bancos

def create_dictOfDict(dicionario,chave):
    dict_valores = {}
    for i in dicionario[chave]:
        dict_valores[i] = ''
    return dict_valores


def find_dict(val):
    bancos = dict_tabelas()
    for dicti in bancos:
        for value in dicti.items():
            if value[1] == val:
                return dicti