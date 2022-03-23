import os
import Conexao

class usuario:
    def __init__(self,dict_banco,dict_valores):
        self.banco = dict_banco
        self.valores = dict_valores
        
    def list_valores(self):
        from datetime import date
        data_log = date.today()
        usuario = os.getlogin()
        lista_select = Conexao.atualiza_banco('select',self.banco,str(self.valores['item']))
        list_valores = [self.banco['banco'] ,self.valores['item'],data_log,usuario,lista_select['count_row'],lista_select['sql_gerado']]
        print(list_valores)
        return list_valores

    def insert_usuario(self):
        import bancos
        dict_log = bancos.find_dict('log_usuario')
        Conexao.atualiza_banco('insert',dict_log,self.list_valores())
        print('Log atualizado com sucesso!')
   



