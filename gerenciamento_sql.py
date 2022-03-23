from datetime import date

class gerador_sql:
    def __init__(self,registro):
        self.registro = registro
        

    def retorna_sql_update(self):
        update = "update "
        update = update + self.registro['banco']
        update = update + " set "
        for i in self.registro['col_change']: update = update + i+"= %s, "
        update = update[0:len(update)-2]
        update = update + " where "
        update = update + self.registro['col_primaria']+ "= %s"
        print(update)
        return update

    def retorna_sql_insert(self):
        insert = "insert into "
        insert = insert + self.registro['banco']
        insert = insert + " ("
        for i in self.registro['col_change']: insert = insert + i+", "
        insert = insert[0:len(insert)-2]
        insert = insert + ") values("
        value = str()
        for _ in range(len(self.registro['col_change'])): value = value + "%s, "
        insert = insert + value
        insert = insert[0:len(insert)-2]
        insert = insert + ");"
        print(insert)
        return insert
        
    def retorna_sql_select(self):
        select = "select "
        select = select + self.registro['col_change'][0]
        select = select + " from "
        select = select + self.registro['banco']
        select = select + " where "
        select = select + self.registro['col_primaria']
        select = select + "= %s"
        print(select)
        return select