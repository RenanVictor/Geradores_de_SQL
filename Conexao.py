import psycopg2 as psy
from sqlparse import sql

conexao = psy.connect(
    host="postgres.ata",
    database="pedidos",
    port=5000,
    user="renan",
    password="rev@123"

)
cursor = conexao.cursor()
cursor.execute("update pedidos set complemento = 'teste' where id = 1502",)
conexao.commit()