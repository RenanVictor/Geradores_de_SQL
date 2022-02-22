from datetime import date

class gerenciamento_sql:
    def __init__(self,banco,item):
        self.banco = banco
        self.item = item

    def sql_finalizar_pedidos(self):
        sql_gerado = 'update '+self.banco+" set Status = 'Pronto', Termino = '"+str(date.today())+"' where OP_MAQ =  '"+self.item + "';"
        return sql_gerado

    def sql_finalizar_laser(self,maquina):
        sql_gerado = "update plan_laser set status = 'Finalizado', Termino = '"+str(date.today())+"', maquina = '"+maquina +"' where seq =  "+self.item + ";"
        return sql_gerado

    def sql_cancelar_pedidos(self):
        sql_gerado = 'update '+self.banco +" set status = 'Montagem', Termino = null where OP_MAQ =  '"+self.item+"';"
        return sql_gerado

    def sql_cancelar_laser(self):
        sql_gerado = "update plan_laser set status = 'Programado', Termino = null where seq =  "+self.item + ";"
        return sql_gerado
